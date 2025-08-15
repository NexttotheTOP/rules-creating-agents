# Product Requirement Document (PRD) 
# Product Name: Rules-generator

## Objective 
To create a clean, intuitive web-based app for users (targeted to developers) that advices them on the best project structure/architecture setups including the best IDE rules setups in order to develop with AI in a safely, guided manner. Users can get advice based on their PRD (or similar) input and can store, view and edit everything seamlessly in a personal library. 

## Tech-Stack
- Langchain/Langgraph eco-system for backend. 
- Nextjs frontend
- Supabase for storage and authentication

Core Features (MVP)

1. User Authentication & Account Management
	•	Authentication: Secure email/password authentication powered by Supabase Auth.
	•	Account Isolation: Each user’s projects, generated rules, and visualizations are private and only accessible to them.
	•	Session Management: Persistent sessions to avoid frequent logins.
	•	Scalability: Designed to extend to OAuth (GitHub, Google, etc.) and MFA in future versions.

⸻

2. Multi-Agent Graph Architecture (Backend)
	•	LangGraph Workflow:
A stateful, context-aware LangGraph handles generation in a pipeline of specialized AI agents:
	1.	Supervisor Agent
	•	Orchestrates the process, routes data between agents, and ensures consistency across outputs.
	•	Maintains overall context and memory throughout a generation session.
	2.	Folder Structure Agent
	•	Generates the optimal project folder hierarchy based on the PRD input.
	•	Follows best practices for scalability, maintainability, and AI-safe development.
	•	Passes results to the Visualization Agent for rendering.
	3.	Visualization Agent
	•	Converts the Folder Structure Agent’s output into an interactive, navigable diagram (e.g., collapsible folder tree).
	•	Outputs are web-friendly, supporting zoom, expand/collapse, and export options.
	4.	Rules & Configs Agent
	•	Generates IDE and project-specific rules, configs, and AI guardrails (e.g., ESLint, Prettier, .editorconfig, AI code usage policies).
	•	Tailors configs to the tech stack mentioned in the PRD.
	5.	Review/Refinement Agent (optional for MVP, but highly recommended)
	•	Reviews all outputs for internal consistency and alignment with best practices.
	•	Suggests refinements or automatically applies improvements before final delivery.
	•	Scalable by Design:
Agents can be added, removed, or specialized further without breaking the core workflow.

⸻

3. Rules Generator & Project Structure Visualization (Frontend)
	•	Input Methods:
	•	Direct text entry via a rich-text prompt box.
	•	File upload (.txt, .md, .docx, .pdf) containing the PRD or project description.
	•	Generation Process:
	1.	Supervisor Agent reads the input and sends it to the relevant agents.
	2.	Folder Structure Agent produces the architecture, which is visualized by the Visualization Agent.
	3.	Rules & Configs Agent produces IDE and workflow guardrails.
	4.	(Optional) Review Agent polishes outputs before delivery.
	•	User Dashboard:
	•	File Explorer View: Displays generated outputs in a system-like folder tree UI.
	•	Interactive Visualization: Clickable architecture diagram synced with the file explorer.
	•	Rules & Config Preview: In-browser editors for configs (JSON, YAML, etc.) with syntax highlighting.
	•	Library Storage: All generations are saved under the user’s account with timestamps and tags.
	•	Versioning: Basic version history so users can revisit or duplicate previous generations.




