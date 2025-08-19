# Rules Generator

A monorepo containing a Next.js frontend and FastAPI backend for generating project rules and configurations from PRD inputs using LangChain and LangGraph.

## Features

- Email/password authentication via Supabase
- PRD input handling (rich-text and file uploads)
- Multi-agent pipeline: Supervisor, Folder Structure, Rules & Configs, Visualization
- Dashboard with file explorer and interactive diagrams
- Storage of generation results with version history

## Tech Stack

- Frontend: Next.js 15, Tailwind CSS, shadcn/ui
- Backend: FastAPI, LangChain, LangGraph
- Database & Auth: Supabase (PostgreSQL)
- CI/CD: GitHub Actions, Docker, Vercel (frontend), Render/Fly.io (backend)

## Getting Started

### Prerequisites

- Node.js v18+, pnpm
- Python 3.11
- Docker
- Supabase account and CLI

### Installation

1. Clone the repository

```bash
git clone <repo-url>
cd rules-creating-agents
```

2. Install dependencies

```bash
pnpm install
```

3. Configure environment variables

- Backend: Copy `infra/env/.env.example` to `apps/backend/.env` and fill in values
- Frontend: Create `.env.local` in `apps/frontend` with SUPABASE_URL and SUPABASE_ANON_KEY

4. Run Supabase locally

```bash
infra/scripts/provision_supabase.sh
```

5. Start development servers

```bash
pnpm dev
```

Open the frontend at http://localhost:3000 and backend at http://localhost:8000.

## Testing

- Frontend

```bash
pnpm --filter frontend lint && pnpm --filter frontend build
```

- Backend

```bash
cd apps/backend
ruff .
black --check .
```

## Deployment

- Frontend is deployed to Vercel on push to `main`
- Backend Docker image is built and pushed to GitHub Container Registry and deployed to Render/Fly.io

## Contributing

Please follow the guidelines in `CODING_STANDARDS.md` for code style, commit messages, and branching.

## License

MIT
