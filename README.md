‌​​‌‌‌‌‌‌‌​‍‌​​‌​⁠‍‍‌​‍‍‌‍⁠⁠‌⁠​⁠‌‍‌‌​‍​​‌‌​‍‌‍‌‌‌⁠‍‌‌‍‌‌‌⁠​⁠​‍​​​‍‍​‌​​​‌⁠​‍‌‍‌‌‌⁠‍‌‌‍‌‌‌⁠​⁠‌‍‍‍‌‍⁠​​‍‍‌​⁠‍‍​⁠​‍​⁠​​​⁠​‍​⁠‌‌​‍⁠‌​⁠​​​⁠‌⁠​‍⁠‌​⁠​‍​⁠‌‍<div align="center">

# 🛡️ AURA - Unified Insurance Submission Intelligence

**A modern, full-stack insurance submission platform streamlining the application process for agents and carriers**

[![Vue 3](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D)](https://vuejs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

</div>

---

## 🌟 Overview

**AURA** is a sophisticated insurance submission platform designed to revolutionize how insurance agents and carriers handle applications. It provides a unified, intelligent system for creating dynamic insurance templates, managing application sessions, and streamlining the submission process for both Personal and Commercial lines.

### 🎯 Key Value Propositions

- **Unified Experience**: Single platform for all insurance submission types
- **Dynamic Intelligence**: Smart question selection based on carrier and coverage combinations
- **Audit Integrity**: Question snapshotting ensures consistency over time
- **Modern UX**: Intuitive, responsive interface built with Vue 3 and Tailwind CSS
- **Scalable Architecture**: Robust Django backend with RESTful API design

---

## 🚀 Features

### 🏢 **Agent Dashboard**

- **Multi-line Support**: Handle both Personal and Commercial insurance applications
- **Dynamic Template Creation**: Build custom submission templates by selecting insurance types, carriers, and coverage lines
- **Session Management**: Create tokenized application sessions for end-users
- **Real-time Progress Tracking**: Monitor application completion status
- **Question Preview**: See exactly which questions will be included before creating sessions

### 🎯 **Smart Question Engine**

- **Contextual Questions**: Questions dynamically filtered by insurance type, carrier, and coverage selections
- **Question Snapshotting**: Templates preserve static copies of questions for audit integrity
- **Multi-dimensional Filtering**: Questions associate with specific carriers, coverage lines, and insurance types
- **Automated Relevance**: Only relevant questions appear based on agent selections

### 👤 **Insured User Experience**

- **Tokenized Access**: Secure, unique links for each application session
- **Guided Completion**: Step-by-step application process
- **Progress Indicators**: Visual feedback on completion status
- **Mobile-Responsive**: Optimized for all device types

### 🔧 **Administrative Features**

- **User Management**: Agent profiles with levels, XP, and agency information
- **Carrier Management**: Flexible carrier-to-insurance type associations
- **Coverage Configuration**: Customizable coverage lines with abbreviations
- **Question Management**: Comprehensive question library with multi-dimensional tagging

---

## 🛠️ Technology Stack

| Layer                | Technology                | Purpose                               |
| -------------------- | ------------------------- | ------------------------------------- |
| **Frontend**         | Vue 3 + TypeScript        | Reactive, type-safe user interface    |
| **Styling**          | Tailwind CSS 4.x          | Utility-first CSS framework           |
| **State Management** | Pinia                     | Modern Vue state management           |
| **HTTP Client**      | Axios                     | API communication                     |
| **Backend**          | Django 5.2 + DRF          | Robust REST API framework             |
| **Database**         | PostgreSQL                | Production database                   |
| **Authentication**   | JWT                       | Secure token-based auth               |
| **Development**      | SQLite                    | Local development database            |
| **Containerization** | Docker                    | Consistent deployment environments    |
| **Code Quality**     | ESLint + Prettier + Black | Automated code formatting and linting |
| **Testing**          | Vitest + Playwright       | Unit and E2E testing                  |

---

## 🏗️ Architecture Overview

### 📁 Project Structure

```
aura-insurance-engine/
├── 🎨 aura_frontend/          # Vue 3 + TypeScript Frontend
│   ├── src/
│   │   ├── api/               # API client and interfaces
│   │   ├── components/        # Reusable Vue components
│   │   ├── pages/             # Route-level components
│   │   ├── router/            # Vue Router configuration
│   │   ├── stores/            # Pinia state management
│   │   ├── types/             # TypeScript type definitions
│   │   └── views/             # Application views
│   ├── e2e/                   # Playwright E2E tests
│   └── public/                # Static assets
├── 🐍 aura_backend/           # Django REST Framework Backend
│   ├── core/                  # Core application logic
│   │   ├── models.py          # Database models
│   │   ├── serializers.py     # DRF serializers
│   │   ├── views.py           # API viewsets
│   │   ├── application_views.py # Specialized application logic
│   │   ├── auth_views.py      # Authentication endpoints
│   │   └── management/        # Custom commands (data seeding)
│   └── aura_backend/          # Django project settings
├── 🐳 Docker Files            # Container configurations
└── 📋 Configuration Files     # Project setup and tooling
```

### 🧩 Core Data Models

#### **Foundation Models**

- **`User`**: Custom user model with agent capabilities (level, XP, agency info)
- **`InsuranceType`**: Personal vs Commercial classification
- **`Carrier`**: Insurance carriers with type associations
- **`CoverageLine`**: Coverage types (GL, Auto, Cyber, etc.) with abbreviations

#### **Intelligence Models**

- **`Question`**: Master questions tagged with carriers, coverages, and insurance types
- **`ApplicationTemplate`**: Agent-created submission blueprints
- **`TemplateQuestionSnapshot`**: Static question copies for audit integrity

#### **Session Models**

- **`ApplicationSession`**: Tokenized application instances for end-users
- **`ApplicationAnswer`**: User responses to template questions
- **`Submission`**: Completed application submissions

---

## 🚀 Quick Start

### 🐳 **Option 1: Docker (Recommended)**

```bash
# Clone the repository
git clone https://github.com/reyesjl/aura-insurance-engine.git
cd aura-insurance-engine

# Start development environment
docker-compose -f docker-compose.dev.yaml up --build

# The application will be available at:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
```

### 🛠️ **Option 2: Manual Setup**

#### Backend Setup

```bash
cd aura_backend

# Create and activate virtual environment
python -m venv aura_env
source aura_env/bin/activate  # On Windows: aura_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations and seed data
python manage.py migrate
python manage.py seed_aura

# Start development server
python manage.py runserver
```

#### Frontend Setup

```bash
cd aura_frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

---

## 🌐 API Architecture

### 🔑 **Authentication Endpoints**

- `POST /auth/login/` - Agent authentication
- `POST /auth/refresh/` - Token refresh
- `GET /auth/me/` - Current user profile

### 🏢 **Core Data Endpoints**

- `GET /insurance-types/` - Available insurance types
- `GET /carriers/` - Insurance carriers
- `GET /coverage-lines/` - Coverage line types
- `GET /questions/` - Question library

### 🎯 **Application Management**

- `GET /carriers-by-coverage/` - Carriers organized by coverage lines
- `GET /preview-questions/` - Preview questions for selections
- `POST /create-application-session/` - Create new application session
- `GET /application-sessions/` - List agent's sessions
- `GET /application-session-details/{id}/` - Session details with answers

### 🔄 **Session Operations**

- `POST /application-session/{id}/roll-token/` - Generate new session token
- `GET /application-session/verify-token/{token}/` - Verify session token

---

## 🧪 Development Workflow

### 🎨 **Frontend Development**

```bash
cd aura_frontend

# Development with hot reload
npm run dev

# Type checking
npm run type-check

# Linting and formatting
npm run lint
npm run format

# Testing
npm run test:unit      # Unit tests with Vitest
npm run test:e2e       # E2E tests with Playwright

# Production build
npm run build
```

### 🐍 **Backend Development**

```bash
cd aura_backend

# Code formatting
black .
isort . --profile black

# Run specific management commands
python manage.py seed_aura              # Seed sample data
python manage.py createsuperuser        # Create admin user

# Database operations
python manage.py makemigrations
python manage.py migrate
```

### 🔧 **Code Quality Tools**

```bash
# Format entire codebase
./format_all.sh

# Frontend linting
cd aura_frontend && npm run lint

# Backend formatting
cd aura_backend && black . && isort . --profile black
```

---

## 🔐 Security & Compliance

### 🛡️ **Authentication & Authorization**

- JWT-based authentication with refresh tokens
- Role-based access control (Agent vs. Standard users)
- Secure session token generation for insured users
- Custom permission classes for API endpoints

### 📋 **Data Integrity**

- Question snapshotting ensures audit trail consistency
- Template versioning maintains historical accuracy
- Comprehensive foreign key relationships prevent orphaned data
- Database constraints enforce business rules

### 🔒 **Authorship Protection**

This repository includes multiple layers of authorship protection:

- Copyright headers in all source files
- Git commit history and timestamps
- Technical watermarking system using zero-width Unicode characters
- Comprehensive documentation of development methodology

See `WATERMARK_SYSTEM.md` for technical details on the watermarking implementation.

---

## 🚀 Deployment

### 🐳 **Production Docker**

```bash
# Build and start production containers
docker-compose -f docker-compose.prod.yaml up --build -d

# Run production migrations
docker-compose -f docker-compose.prod.yaml exec backend python manage.py migrate

# Create production superuser
docker-compose -f docker-compose.prod.yaml exec backend python manage.py createsuperuser
```

### ⚙️ **Environment Configuration**

Create `.env` files for environment-specific settings:

```env
# Backend (.env)
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:pass@localhost/aura_prod
ALLOWED_HOSTS=yourdomain.com

# Frontend (.env)
VITE_API_BASE_URL=https://api.yourdomain.com
VITE_APP_TITLE=AURA Insurance Platform
```

---

## 🎯 Usage Examples

### 🏢 **Creating an Application Session**

1. **Select Insurance Type**: Choose Personal or Commercial
2. **Select Carriers**: Pick carriers for each coverage line
3. **Preview Questions**: Review which questions will be included
4. **Create Session**: Generate tokenized link for insured user
5. **Share with Insured**: Send secure link to applicant

### 📊 **Managing Questions**

Questions are intelligently filtered based on:

- **Insurance Type**: Personal vs Commercial
- **Carriers**: Specific insurance companies
- **Coverage Lines**: GL, Auto, Cyber, etc.

Example: A Commercial Auto application with Travelers will only show questions relevant to that specific combination.

---

## 🔮 Future Roadmap

### 📈 **Enhanced Features**

- [ ] **Document Upload**: File attachment capabilities for applications
- [ ] **E-signature Integration**: Digital signature workflows
- [ ] **Automated Underwriting**: Basic risk assessment algorithms
- [ ] **Multi-language Support**: Internationalization features
- [ ] **Advanced Analytics**: Application completion metrics and insights

### 🔧 **Technical Improvements**

- [ ] **Caching Layer**: Redis for improved performance
- [ ] **Real-time Updates**: WebSocket integration for live progress
- [ ] **Mobile Apps**: Native iOS/Android applications
- [ ] **Advanced Testing**: Comprehensive test coverage
- [ ] **Performance Monitoring**: Application performance insights

### 🌐 **Integration Capabilities**

- [ ] **CRM Integration**: Connect with popular insurance CRM systems
- [ ] **Email Marketing**: Automated follow-up campaigns
- [ ] **Third-party APIs**: Rating engines and carrier APIs
- [ ] **Workflow Automation**: Advanced business process automation

---

## 🤝 Contributing

This is a proprietary project developed by Jose Reyes. External contributions are not currently accepted, but feedback and suggestions are welcome.

### 📝 **Development Guidelines**

- Follow TypeScript best practices for frontend code
- Use Django REST Framework conventions for backend APIs
- Maintain comprehensive test coverage
- Follow established code formatting standards
- Document all new features and API endpoints

---

## 📄 License

This software is proprietary and confidential. All rights reserved.

**Copyright © 2025 Jose Reyes (GitHub: @reyesjl)**

This code is proprietary and confidential. Unauthorized use, reproduction, distribution, or modification is strictly prohibited.

---

## 🙏 Acknowledgments

- **Jose Reyes** - Full-stack engineer and designer, primary developer
- **Jacob Powers** - Licensed insurance agent, domain expertise and project guidance
- **Vue.js Team** - For the excellent frontend framework
- **Django Team** - For the robust backend framework
- **Tailwind CSS** - For the outstanding utility-first CSS framework

---

## 📞 Contact

**Project Repository**: [https://github.com/reyesjl/aura-insurance-engine](https://github.com/reyesjl/aura-insurance-engine)

**Documentation**: [https://app.devin.ai/wiki/reyesjl/aura-insurance-engine](https://app.devin.ai/wiki/reyesjl/aura-insurance-engine)

**Developer**: Jose Reyes ([@reyesjl](https://github.com/reyesjl))

---

<div align="center">

**Built with 💙 for the insurance industry**

_Streamlining submissions, one application at a time_

</div>
