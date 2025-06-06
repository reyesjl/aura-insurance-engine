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
| Backend     | Django + DRF           |
| Database    | SQLite (local/dev)     |

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
└── README.md
```

## 🧩 Core Models

- `InsuranceType`: Personal or Commercial
- `Carrier`: Associated with one or more insurance types
- `CoverageLine`: Coverage types (e.g., Auto, Cyber)
- `Question`: Associated with specific types/carriers/coverage
- `Template`: Defines a reusable submission blueprint
- `TemplateQuestionSnapshot`: Static copy of question tied to a template
- `ApplicationSession`: Tracks end-user filling out a template
- `ApplicationAnswer`: Stores answer to a question within a session

## 🧪 Getting Started (Dev)

### Backend

```bash
cd backend/
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