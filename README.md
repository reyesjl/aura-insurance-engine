# AURA – Unified Insurance Submission Intelligence

**AURA** is a modern insurance intake and processing platform designed to streamline insurance submissions for agents and carriers. It centralizes intake across lines of coverage, dynamically builds templates with relevant questions, and enables insured users to complete applications in a unified, guided way.

## 🚀 Features

- **Multi-line Support:** Supports both Personal and Commercial lines.
- **Dynamic Templates:** Agents create submission templates by selecting insurance type, carriers, and coverage lines.
- **Question Snapshotting:** Templates snapshot relevant questions at creation time for audit integrity.
- **Application Sessions:** Create tokenized sessions for end-users to fill out submissions.
- **Progress Tracking:** Track how many answers are completed in real time.
- **Seamless UX:** Modern Vue 3 frontend with Tailwind styling.

## 🛠️ Stack

| Layer       | Tech                   |
|-------------|------------------------|
| Frontend    | Vue 3 + TypeScript     |
| Styling     | Tailwind CSS           |
| Backend     | Django                 |
| Database    | SQLite (local/dev)     |
| Containerization | Docker, Docker Compose |

## 📁 Project Structure

```
/aura-insurance-engine/
├── aura_backend/                 # Django project
│   ├── core/                # App containing models and logic
│   ├── manage.py
│   └── ...
├── aura_frontend/                # Vue 3 app
│   ├── components/
│   ├── views/
│   ├── assets/
│   └── ...
├── docker-compose.dev.yaml       # Docker Compose for development
├── docker-compose.prod.yaml      # Docker Compose for production
└── README.md
```

## 🐳 Dockerized Setup

This project uses Docker and Docker Compose for both development and production environments.

### Shared Static Volume in Production

In production, Django and Nginx run in separate containers. To ensure Django's static files (such as admin CSS/JS) are available to Nginx for serving, a **shared Docker volume** (`static_volume`) is used. Both the backend and frontend containers mount this volume at `/app/static/`. When Django runs `collectstatic`, it writes all static files to this shared location, and Nginx serves them at the `/static/` URL.

This setup ensures that static assets are always up-to-date and available to the web server, without manual copying or rebuilding.

### Development

- **Frontend**:  
  Uses `aura_frontend/Dockerfile.dev` (Node 18). Runs the Vite dev server with hot reload on port **5173**. Local code is mounted for instant feedback.
- **Backend**:  
  Uses `aura_backend/Dockerfile` (Python 3.11). Runs Django's development server on port **8000**. Local code is mounted for live reload.
- **Networking**:  
  Both services are on the `aura` Docker network for easy API communication.

#### Quick Start (Dev)

1. **Create your backend environment file:**

   Copy `.env.example` (if present) or create `.env` in `aura_backend/` with your settings.

   ```bash
   cp aura_backend/.env.example aura_backend/.env
   # Edit aura_backend/.env as needed
   ```

2. **Start the dev environment:**

   ```bash
   docker compose -f docker-compose.dev.yaml up --build
   ```

   - Frontend: [http://localhost:5173](http://localhost:5173)
   - Backend: [http://localhost:8000](http://localhost:8000)

### Production

- **Frontend**:  
  Uses `aura_frontend/Dockerfile` (multi-stage: Node 18 for build, Nginx for serving static files). Exposes port **80**.
- **Backend**:  
  Uses `aura_backend/Dockerfile` (Python 3.11, runs Gunicorn WSGI server). Exposes port **8000** internally.
- **Networking**:  
  Both services are on the `aura` Docker network.

Start the production environment:

```bash
docker compose -f docker-compose.prod.yaml up --build
```

### Frontend Dockerfile Details

The production frontend Dockerfile uses a multi-stage build:

1. **Build Stage** (`node:18`):
    - Installs dependencies and builds the Vue app.
2. **Serve Stage** (`nginx:alpine`):
    - Copies the built static files to Nginx and serves them on port 80.
    - Uses a custom `nginx.conf` for routing and caching.

#### Example Commands

Build the frontend image manually:

```bash
docker build -t aura-frontend ./aura_frontend
docker run -p 80:80 aura-frontend
```

---

## 🧩 Core Models

- `InsuranceType`: Personal or Commercial
- `Carrier`: Associated with one or more insurance types
- `CoverageLine`: Coverage types (e.g., Auto, Cyber)
- `Question`: Associated with specific types/carriers/coverage
- `Template`: Defines a reusable submission blueprint
- `TemplateQuestionSnapshot`: Static copy of question tied to a template
- `ApplicationSession`: Tracks end-user filling out a template
- `ApplicationAnswer`: Stores answer to a question within a session

## 🧪 Getting Started (Manual Setup - Optional)

If you prefer not to use Docker, you can still run the backend and frontend manually:

### Backend

```bash
cd aura_backend/
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Wipe and rebuild db (dev only)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate

# Seed development data
python manage.py seed_aura
```

### Frontend

```bash
cd aura_frontend/
npm install
npm run dev
```

> Vue is served on port 5173, Django on 8000. Configure CORS/Proxy if needed.

## 🌐 API Endpoints (Sample)

- `POST /api/templates/` – Create a new submission template
- `GET /api/templates/:id/` – Get template + questions
- `POST /api/sessions/` – Start a new application session
- `GET /api/sessions/:token/` – Retrieve session
- `POST /api/sessions/:token/answers/` – Submit answers
- `GET /api/sessions/:token/progress/` – Get completion %

## 🧠 Future Plans

- [ ] Add field-level validations per question
- [ ] Export completed sessions to PDF
- [ ] Multi-agent organizations
- [ ] Real-time collaboration on sessions
- [ ] AI-assisted intake suggestions

## 🤝 Contributing

Coming soon – this repo is currently in private development. If you're interested in helping shape the future of AURA, contact the maintainer.

## 📄 License

MIT – see online.

## 🙏 Acknowledgements

Inspired by real-world inefficiencies in the insurance intake process. AURA is built to modernize and unify what has been fragmented and slow for too long.
