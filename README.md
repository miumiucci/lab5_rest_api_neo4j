# Lab 5: REST API for Neo4j Graph Database

## **Описание проекта**
Этот проект представляет серверное REST API на основе FastAPI для работы с графовой базой данных Neo4j. 
API позволяет выполнять CRUD-операции с узлами и связями, а также включает защиту некоторых точек доступа с использованием токена.

---

## **Функции API**

### **1. Получение всех узлов**
**GET /nodes/**  
Возвращает список всех узлов с их `id` и `label`.

### **2. Получение узла и его связей**
**GET /nodes/{node_id}**  
Возвращает узел с указанным `id` и все его связи со всеми атрибутами.

### **3. Добавление узла**
**POST /nodes/**  
Добавляет новый узел в граф. Требуется токен для авторизации.




### **4. Удаление узла**
**DELETE /nodes/{node_id}**  
Удаляет узел по его `id`. Требуется токен для авторизации.


---

## **Развёртывание на VDS без контейнера**

1. **Установите Python и зависимости:**


2. **Настройте Neo4j:**
   - Убедитесь, что Neo4j установлен и запущен.
   - Укажите параметры подключения к Neo4j в файле `.env`.

3. **Склонируйте репозиторий:**
   ```bash
   git clone <https://github.com/KalimovaAltynai/lab5_rest_api_neo4j.git>
   cd lab5_rest_api_neo4j
   ```

4. **Запустите сервер:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

5. **Проверьте работу API:**
   Откройте в браузере:
   ```
   http://<IP_СЕРВЕРА>:8000/docs
   ```

---

## **Запуск тестов**

1. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Запустите сервер (в одном терминале):**
   ```bash
   uvicorn app.main:app --reload
   ```

3. **Запустите тесты (в другом терминале):**
   ```bash
   pytest tests/test_routes.py
   ```

---

## **Примеры токенов и узлов**
Токен для доступа: `749f233e4ff64dda08c3132a8766656c`  

**Пример данных для узлов:**
```json
{
    "label": "User",
    "properties": {
        "name": "Example User"
    }
}
```
