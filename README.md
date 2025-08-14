# 🐾 Kenya Pet Hub API

Kenya Pet Hub API is a backend service that allows users to **list, browse, and manage pets for sale or adoption** in Kenya.  
It’s built with **FastAPI** and returns clean **JSON responses** for easy integration into web or mobile applications.

---

## 🚀 Features
- Add new pets with details (name, type, breed, age, location, price).
- Retrieve a list of all pets in JSON format.
- Fetch pets by their unique ID.
- Designed for scalability and integration with databases.
- Developer-friendly API endpoints.

---

## 🛠 Tech Stack
- **Python 3.12+**
- **FastAPI**
- **Uvicorn** (ASGI server)
- **Pydantic** (data validation)

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/kenya-pet-hub-api.git
cd kenya-pet-hub-api

2️⃣ Create & activate a virtual environment
bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
------------


3️⃣ Install dependencies
pip install -r requirements.txt
------------

4️⃣ Run the server
uvicorn main:app --reload
Your API will be live at:

http://127.0.0.1:8000
--------------------
 API Endpoints

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | `/`              | Welcome message          |
| GET    | `/pets`          | Get all pets             |
| GET    | `/pets/{pet_id}` | Get a specific pet by ID |
| POST   | `/pets`          | Add a new pet            |

Right now you can also check:

Swagger docs: http://127.0.0.1:8000/docs

Redoc docs: http://127.0.0.1:8000/redoc

That’s where you’ll see all your API endpoints in a nice UI.

📄 Example JSON Response
json
[
  {
    "id": 1,
    "name": "Bosco",
    "type": "Dog",
    "breed": "German Shepherd",
    "age": 2,
    "location": "Nairobi",
    "price": 15000
  }
]


