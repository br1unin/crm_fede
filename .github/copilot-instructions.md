# AI Agent Instructions for CRM Tractores

## Project Overview
This is a CRM system for tractor sales with a FastAPI backend and React+TypeScript frontend.

## Architecture

### Backend (`/backend`)
- FastAPI-based REST API with SQLAlchemy ORM
- Key components:
  - `app/models/`: SQLAlchemy models (client.py, sale.py, tractor.py, user.py)
  - `app/routes/`: API endpoints organized by domain
  - `app/schemas/`: Pydantic models for request/response validation
  - `app/utils/`: Shared utilities including auth and security

### Frontend (`/frontend`)
- React + TypeScript + Vite stack
- Key patterns:
  - Component organization: `components/{domain}/` for domain-specific components
  - Shared components in `components/common/`
  - Global state management via React Context (`context/AuthContext.tsx`)
  - API communication centralized in `services/api.ts`
  - Type definitions in `types/index.ts`

## Development Workflows

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
python run.py
```
- API runs on http://localhost:8000

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
- Dev server runs on http://localhost:5173
- Build with `npm run build`

## Key Integration Points

1. API Communication
- All API calls go through `services/api.ts` using axios
- JWT authentication via Authorization header
- Base URL configured as http://localhost:8000

2. Authentication Flow
- Login/Register handled by `components/auth/{Login,Register}.tsx`
- JWT stored in localStorage
- Protected routes in frontend check AuthContext
- Backend validates JWT via `utils/auth.py`

## Project-Specific Patterns

1. Component Structure:
- Each domain (clients, sales, tractors) follows pattern:
  - List component (`{Domain}List.tsx`)
  - Form component (`{Domain}Form.tsx`)
  - Detail component where applicable

2. Role-Based Dashboards:
- Separate dashboards for admin/employee roles
- Role-specific components in `components/dashboard/`

3. Form Handling:
- Consistent form structure across all create/edit operations
- Validation handled by backend schemas

## File/Directory References

Key files for understanding the codebase:
- Backend API setup: `backend/app/main.py`
- Database models: `backend/app/models/`
- Frontend auth flow: `frontend/src/context/AuthContext.tsx`
- API client: `frontend/src/services/api.ts`