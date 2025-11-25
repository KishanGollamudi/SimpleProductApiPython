# 🛍️ SimpleProductApiPython

A lightweight FastAPI-based product microservice with a beautiful frontend UI for listing products.

## 🚀 Features

* FastAPI backend (Python 3)
* REST product API
* JSON output & HTML UI
* Premium CSS Frontend
* Runs locally or on server
* Deployable via Nginx + Gunicorn
* Fully open-source & customizable

---

## 🧠 Project Structure

```
SimpleProductApiPython/
│
├── app.py
├── static/
│   ├── index.html
│   └── style.css
├── venv/   (ignored in Git)
└── README.md
```

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/KishanGollamudi/SimpleProductApiPython.git
cd SimpleProductApiPython
```

### 2️⃣ Create virtual environment

```bash
sudo apt install python3.12-venv -y
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn
```

---

## ▶️ Run App Locally

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 5000
```

Open in browser:

```
http://localhost:5000
```

or on EC2:

```
http://YOUR_PUBLIC_IP:5000
```

---

## 🔥 API Endpoints

| Method | Endpoint        | Description               |
| ------ | --------------- | ------------------------- |
| GET    | `/api/products` | Returns JSON product list |
| GET    | `/`             | Renders HTML UI           |

---

## 💻 Sample API Output

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 1200,
    "description": "High performance laptop"
  },
  {
    "id": 2,
    "name": "Headphones",
    "price": 200,
    "description": "Noise cancelling headphones"
  }
]
```

---

## 🔐 .gitignore

We exclude Python venv from Git:

```
venv/
__pycache__/
```

---

## ☁️ Deployment

This app can be deployed using:

* FastAPI + Uvicorn
* Gunicorn
* Nginx Reverse Proxy
* Docker
* Kubernetes
* GitHub Actions CI/CD

---

## 👨‍💻 Author

**Kishan Gollamudi**

GitHub:
[https://github.com/KishanGollamudi](https://github.com/KishanGollamudi)

---

## 🤝 Contributing

Pull requests welcome.
Major features or improvements — open an issue first.

---

## 📝 License

This project is open-source and available under the MIT License.

---
