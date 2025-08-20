# UI & UX Documentation – Rules-generator

## Design System

- **Foundation:** Tailwind CSS utility classes with custom theme tokens (colors, spacing, typography) declared in `tailwind.config.ts`.
- **Component Library:** shadcn/ui components wrapped in `packages/ui` with project-specific variants and consolidated props API.
- **Iconography:** Lucide icons; consistent 1.5 px stroke width; stored in `packages/ui/icons`.

## UI Component Guidelines

1. Components are atomic and headless – logic separated from presentation.
2. Styling applied via Tailwind utility classes or variants generated with `class-variance-authority`.
3. All interactive components expose appropriate `aria-*` attributes and full keyboard interaction.
4. Props naming follows camelCase; boolean modifiers prefixed with `is` (e.g., `isLoading`).

## User Experience Flows

### 1. Onboarding & Authentication

- Landing screen offers **Login** and **Register** tabs.
- Form validation client-side and server-side.
- Successful auth redirects to **Dashboard**; JWT stored in http-only cookie.

### 2. New Generation Workflow

1. Click **“New Project”** in sidebar.
2. Enter PRD text in rich-text editor or upload document.
3. Press **Generate** – progress modal shows agent stages.
4. Upon completion, user is routed to **Project View** displaying file explorer and diagram.

### 3. Library Management

- Dashboard lists generations in table view (sortable by date, tags).
- Clicking a row opens detail view with version history side panel.
- Search bar filters by title and tags.

## Responsive Design Requirements

- Mobile-first breakpoints: `sm (640)`, `md (768)`, `lg (1024)`, `xl (1280)`.
- Sidebar collapses into bottom nav on `sm` screens.
- Diagram canvas supports pinch-zoom and pan gestures on touch devices.

## Accessibility Standards

- Target **WCAG 2.1 AA** compliance.
- Color contrast ratio ≥ 4.5:1.
- Focus traps in modal/dialog components using `@radix-ui/react-dialog`.
- Live region announcements via `useAriaLive` hook for generation progress.

## Style Guide & Branding

| Token           | Value                 | Usage                      |
| --------------- | --------------------- | -------------------------- |
| Primary Color   | `#4F46E5`             | Buttons, links, highlights |
| Secondary Color | `#6366F1`             | Hovers, active states      |
| Surface         | `#FFFFFF` / `#F9FAFB` | Backgrounds                |
| Text Primary    | `#111827`             | Body text                  |
| Border Radius   | `8px`                 | Inputs, cards              |
| Font Family     | `Inter, sans-serif`   | Global typography          |

## Component Library Organization

```text
packages/ui/
├── button/
│   ├── Button.tsx
│   └── button.stories.tsx
├── dialog/
├── tree-view/
└── …
```

Storybook runs at `/storybook` route in dev; visual regression via Chromatic.

## User Journey Maps

- Mermaid diagram stored at `/Docs/diagrams/user-journey.mmd` details primary flows.
- Updated when flows change.

## Wireframe References

Figma file (read-only link): https://www.figma.com/file/XXXXX/Rules-generator

## Design Tool Integration

- Figma → Storybook sync using **Figma Developer** plugin on `main` branch push.
- Chromatic publishes preview for every PR enabling UI review before merge.
