from fastapi import APIRouter, HTTPException, Depends
from app.utils import get_nodes, create_node, delete_node, get_node_with_relationships
from app.auth import verify_token
from pydantic import BaseModel

router = APIRouter()

class NodeRequest(BaseModel):
    label: str
    properties: dict

@router.get("/nodes/", response_model=list)
def get_all_nodes():
    return get_nodes()

@router.get("/nodes/{node_id}", response_model=dict)
def get_node_and_relationships(node_id: int):
    return get_node_with_relationships(node_id)

@router.post("/nodes/", response_model=dict)
def add_node(node: NodeRequest, token: str = Depends(verify_token)):
    return create_node(node.label, node.properties)

@router.delete("/nodes/{node_id}", response_model=dict)
def remove_node(node_id: int, token: str = Depends(verify_token)):
    return delete_node(node_id)
