# Copilot instructions for FootIQ

## Project context
This repository is a greenfield football analytics app described in `README.md`. The product vision is a full-stack platform for player/team analysis, comparison, scouting, and similarity-based recommendations. There is no production implementation checked in yet, so prefer preserving the intended architecture instead of inventing extra layers.

## Intended architecture
- Frontend: React for dashboards and user-facing analytics.
- Backend: Python with FastAPI for API endpoints and business logic.
- Persistence: PostgreSQL for player/team data, user state, and analytics results.
- Data layer: external football statistics API plus ingestion/normalization modules.

Keep these boundaries explicit: UI code should not contain database queries or business logic; API routes should stay thin; data ingestion and rating algorithms should live in dedicated modules rather than controller files.

## Suggested project structure
When adding code, use a conventional split that matches the stack: `frontend/`, `backend/`, `db/`, `data/`, and optional `services/` or `analytics/` directories. Avoid a single monolithic app unless the scope is tiny. The goal is to separate product UI, API, storage, and model logic.

## Domain-specific patterns
This repo is centered on football data and comparison workflows. Code should be organized around these domain concepts:
- player profiles and statistics
- team analytics and comparison
- similarity matching / player recommendation
- scouting signals and custom ratings

Good examples include a `players` or `teams` API surface, analytics helpers for similarity scoring, and a data-ingestion module that normalizes external football API payloads before they reach the database.

## Coding conventions to keep
- Prefer typed request/response models in FastAPI (Pydantic) and small route handlers.
- Prefer React function components and hooks over class-based UI patterns.
- Keep external API calls and fetch logic in dedicated service modules, not in components.
- Treat player rating and similarity logic as reusable analytics functions rather than ad hoc endpoint code.
- Store configuration in environment variables (`DATABASE_URL`, API keys, feature flags) and do not hardcode secrets.

## Workflow expectations
- Since the repo is still being scaffolded, prefer minimal standard tooling over custom abstractions.
- Validate with the smallest relevant command available once project files are added (`npm`, `pytest`, `python -m ...`, or a local FastAPI/React dev command).
- Update `README.md` whenever the intended architecture or feature scope changes; it is the clearest source of truth for this repo.

## Avoid
- Mixing backend, frontend, and database concerns in the same module.
- Building feature work without preserving the React + FastAPI + PostgreSQL split.
- Designing a custom data model without first considering player/team/statistics relationships.
- Hardcoding football API credentials or database connection details.
