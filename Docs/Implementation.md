# Implementation Plan for Rules-generator

## Feature Analysis
### Identified Features:
- **User Authentication & Account Management**  
  Secure email/password login via Supabase Auth with session persistence.
- **Multi-Agent Graph Architecture**  
  Supervisor orchestrates specialized agents (Folder Structure, Visualization, Rules & Configs, optional Review) using LangGraph.
- **PRD Input Handling**  
  Rich-text editor and file upload (.txt, .md, .docx, .pdf) accepted.
- **Rules Generator & Project Structure Visualization UI**  
  File explorer-like tree, interactive diagram, IDE rule previews with syntax highlighting.
- **Library Storage & Versioning**  
  Store all generations per user with timestamps and basic version history.
- **Scalability & Extensibility**  
  Architecture permits adding agents and auth providers (OAuth, MFA) without breaking workflow.

### Feature Categorization:
**Must-Have Features**  
- Email/password Authentication  
- Supervisor, Folder Structure, Visualization, Rules & Configs Agents  
- PRD input (text & file)  
- Dashboard with file explorer + interactive diagram  
- Storage of generations in user library  

**Should-Have Features**  
- Versioning of generations  
- Review/Refinement Agent  
- OAuth provider extension (GitHub, Google)  

**Nice-to-Have Features**  
- MFA  
- Export diagram & configs  
- Tagging & advanced search  

## Recommended Tech Stack
### Frontend
- **Next.js 14** – Hybrid rendering, powerful routing, great DX  
  Docs: https://nextjs.org/docs
- **Tailwind CSS** – Utility-first styling, fast prototyping  
  Docs: https://tailwindcss.com/docs
- **shadcn/ui** – Accessible, headless UI primitives  
  Docs: https://ui.shadcn.com/docs 

### Backend
- **LangChain + LangGraph (Python)** – Composable LLM chains and stateful graphs  
  Docs: https://python.langchain.com/docs , https://python.langchain.com/docs/ecosystem/langgraph
- **FastAPI** – Async, automatic docs, high performance  
  Docs: https://fastapi.tiangolo.com/

### Database & Authentication
- **Supabase (PostgreSQL)** – Managed Postgres, row-level security, Auth, Storage  
  Docs: https://supabase.com/docs

### Cloud & DevOps
- **Vercel** (frontend) & **Fly.io** or **Render** (backend)  
- **GitHub Actions** – Automated lint, test, deploy  
- **Docker** – Consistent runtime for backend

### Additional Tools
- **Zustand** – Lightweight React state management (https://github.com/pmndrs/zustand)  
- **Mermaid.js** – Diagram generation (https://mermaid.js.org/)  
- **Playwright** – E2E testing (https://playwright.dev/)  
- **Sentry** – Monitoring & error tracking (https://sentry.io/)  

## Implementation Stages

### Stage 1: Foundation & Setup [completed]
**Duration:** 2 weeks  
**Dependencies:** None

#### Sub-steps
- [done] Set up monorepo (pnpm workspaces) containing `apps/frontend` and `apps/backend`
- [done] Configure TypeScript (frontend) and Python (backend) linting & formatting (ESLint, Prettier, Ruff, Black)
- [done] Initialize GitHub repository with conventional commits & branch protection
- [done] Provision Supabase project; create Auth settings and initial schema (`users`, `generations`)
- [done] Scaffold Next.js app with Tailwind & shadcn/ui; set up absolute import aliases
- [done] Scaffold FastAPI service; add LangChain, LangGraph, Pydantic, Uvicorn
- [done] Implement basic email/password auth flow; store JWT in secure http-only cookies
- [done] Add Dockerfiles and docker-compose for local development
- [done] Configure GitHub Actions workflows for test & preview deployments
- [done] Draft initial engineering documentation (README, Coding Standards)

### Stage 2: Core Features
**Duration:** 4 weeks  
**Dependencies:** Stage 1 completion 

#### Sub-steps
- [done] Build a basic text or file upload page using `@shadcn/ui`; setup Supabase Storage connection for file uploads (no auth and RLS yet)
- [ ] setup modern and functional login and signup pages for the user. (larger task)
- [ ] Design the file upload layout, style, colors etc... in a comprehensive and detailled way, no implmementations, only creating a verbal visualization of our page and how we can set this up modern 
- [ ] Implement Supervisor Agent orchestrating other agents through LangGraph
- [ ] Develop Folder Structure Agent generating hierarchical JSON structure
- [ ] Create Rules & Configs Agent producing `.eslintrc`, `.prettierrc`, etc.
- [ ] Implement Visualization Agent converting folder JSON to Mermaid diagram definition
- [ ] Expose `/generate` API endpoint in FastAPI to trigger pipeline; stream progress via Server-Sent Events
- [ ] Build dashboard: file explorer component (headless-ui Tree) synced with generation output
- [ ] Render interactive diagram with `react-mermaid2` and `react-zoom-pan-pinch`
- [ ] Persist generation results in `generations` table with RLS per user
- [ ] Implement optimistic UI updates & error boundaries

### Stage 3: Advanced Features
**Duration:** 3 weeks  
**Dependencies:** Stage 2 completion

#### Sub-steps
- [ ] Integrate Review/Refinement Agent for auto-improvement suggestions
- [ ] Implement generation version history using `supabase.functions` triggers
- [ ] Add OAuth (GitHub, Google) via Supabase Auth
- [ ] Provide export options (SVG, PDF, ZIP) for diagrams and configs
- [ ] Implement tagging & search (Postgres Full-Text) across user library
- [ ] Add realtime generation progress updates via Supabase Realtime channels

### Stage 4: Polish & Optimization
**Duration:** 2 weeks  
**Dependencies:** Stage 3 completion

#### Sub-steps
- [ ] Write unit & integration tests for agents; E2E tests with Playwright
- [ ] Bundle & performance optimization (code-splitting, image optimization)
- [ ] Accessibility audit and fixes (focus management, ARIA, color contrast)
- [ ] UI/UX refinement based on user testing feedback
- [ ] Add Sentry monitoring & logging throughout stack
- [ ] Configure production environments; automate migrations via `supabase migration`
- [ ] Create onboarding guided tour and in-app documentation

## Resource Links
- Next.js Documentation: https://nextjs.org/docs
- Tailwind CSS Documentation: https://tailwindcss.com/docs
- shadcn/ui Guide: https://ui.shadcn.com/
- LangChain Documentation: https://python.langchain.com/docs
- LangGraph Documentation: https://python.langchain.com/docs/ecosystem/langgraph
- FastAPI Documentation: https://fastapi.tiangolo.com/
- Supabase Documentation: https://supabase.com/docs
- GitHub Actions Documentation: https://docs.github.com/en/actions
- Docker Documentation: https://docs.docker.com/
- Playwright Documentation: https://playwright.dev/
