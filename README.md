# 🧮 Flask Calculator App (Dockerized)

A simple web-based calculator built with **Flask (Python)** and fully containerized using **Docker**.  
It performs basic arithmetic operations (addition, subtraction, multiplication, division) and is designed following clean architecture principles with clear separation between **application logic** and **infrastructure**.

---

## 📁 Project Structure

```
calculator/
│
├── app/                         # Core Flask application
│   ├── __init__.py              # Flask app factory
│   ├── routes.py                # Application routes (calculator logic)
│   ├── templates/               # HTML templates (Jinja2)
│   │   └── index.html
│   └── static/                  # Static assets (CSS, JS)
│
├── docker/                      # Docker & deployment files
│   ├── Dockerfile               # Docker image definition
│   ├── docker-compose.yaml      # Service definition for container orchestration
│   ├── .dockerignore            # Files/folders excluded from Docker context
│   └── README.md                # Docker usage notes (optional)
│
├── run.py                       # Flask entry point
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
└── venv/                        # Local virtual environment (not committed)
```

---

## 🚀 Features

- 🧮 Perform addition, subtraction, multiplication, and division  
- 🌐 Browser-based UI built with Bootstrap 5  
- 🐳 Fully Dockerized — one command to build and run  
- 🧩 Modular folder structure for scalability  
- ⚙️ Uses Flask Blueprints and App Factory pattern  

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Python 3.13 + Flask |
| Frontend | HTML, Bootstrap 5 |
| Containerization | Docker, Docker Compose |
| Deployment-ready | Works locally and in any Docker-compatible cloud environment |

---

## ⚙️ Installation (Local without Docker)

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/flask-calculator.git
   cd flask-calculator
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate    # On Windows
   # or
   source venv/bin/activate # On Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python run.py
   ```

5. Open your browser at:  
   👉 http://127.0.0.1:5000

---

## 🐳 Run with Docker

1. Navigate into the Docker folder:
   ```bash
   cd docker
   ```

2. Build and run the container:
   ```bash
   docker compose up --build
   ```

3. Visit your app in the browser:  
   👉 http://127.0.0.1:5000

4. To stop and clean up:
   ```bash
   docker compose down -v
   ```

---

## 🧾 Example UI

![Calculator Screenshot](https://user-images.githubusercontent.com/yourgithubusername/calculator-example.png)

*(Screenshot optional — add after your first push to GitHub)*

---

## 🧩 Example Routes

| Route | Method | Description |
|--------|---------|-------------|
| `/` | GET | Render calculator page |
| `/` | POST | Process form and return result |

---

## 🧹 Useful Docker Commands

| Action | Command |
|---------|----------|
| Build & Run | `docker compose up --build` |
| Stop & Remove Containers | `docker compose down` |
| Stop + Delete Everything | `docker compose down -v --rmi all` |
| View Logs | `docker logs calculator_app` |
| List Containers | `docker ps -a` |

---

## 📦 Requirements

- **Python** ≥ 3.10  
- **Docker** ≥ 20.x  
- **pip** (Python package manager)

---

## 🧠 Future Improvements

- Add scientific calculator functions (square root, power, etc.)
- Store recent calculations in session
- Add a REST API endpoint (`/api/calculate`)
- Include unit tests and CI/CD pipeline (GitHub Actions)
- Deploy to Render, AWS ECS, or Azure App Service

---

## 👨‍💻 Author

**Movahed Abdolahi**  
📍 Based in Canada  
💼 Data & Business Intelligence Professional  
🔗 [LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/)  

---

## 🪪 License

This project is open-source and available under the **MIT License**.  
You are free to use, modify, and distribute it.
