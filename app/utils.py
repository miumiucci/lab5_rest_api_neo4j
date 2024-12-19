from neo4j import GraphDatabase
from app.database import driver

def get_nodes():
    query = "MATCH (n) RETURN ID(n) AS id, labels(n)[0] AS label"
    with driver.session() as session:
        result = session.run(query)
        return [{"id": record["id"], "label": record["label"]} for record in result]

def create_node(label, properties):
    query = f"CREATE (n:{label} $properties) RETURN ID(n) AS id, labels(n)[0] AS label"
    with driver.session() as session:
        result = session.run(query, properties=properties)
        return result.single()

def delete_node(node_id):
    query = "MATCH (n) WHERE ID(n) = $node_id DETACH DELETE n RETURN 'Node deleted' AS result"
    with driver.session() as session:
        result = session.run(query, node_id=node_id)
        return {"message": result.single()["result"]}

def get_node_with_relationships(node_id):
    query = '''
    MATCH (n)-[r]-(m)
    WHERE ID(n) = $node_id
    RETURN n AS node, COLLECT(r) AS relationships, COLLECT(m) AS connected_nodes
    '''
    with driver.session() as session:
        result = session.run(query, node_id=node_id)
        record = result.single()
        if not record:
            raise ValueError("Node not found")
        return {
            "node": dict(record["node"]),
            "relationships": [dict(rel) for rel in record["relationships"]],
            "connected_nodes": [dict(node) for node in record["connected_nodes"]]
        }
