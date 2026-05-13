# Architecture Plan

**Project: AI-Enhanced Team Collaboration Platform**

---

## 1. Overview

This document describes the high-level architecture for an AI-Enhanced Team Collaboration Platform — a web application that enables teams to manage projects and tasks, communicate in context, and leverage AI-powered features such as task description improvement, project summarization, and sprint planning recommendations.

The system follows a **client-server architecture** with a decoupled frontend, a RESTful backend API, a relational database, and integration with an external AI provider (Anthropic Claude API).

---

## 2. Architecture Style

**Pattern:** Monolithic Backend with Service Separation (modular monolith)

This approach is chosen for hackathon-scale development speed while keeping the codebase organized enough to extract microservices later if needed.

*   **Frontend:** Single Page Application (SPA)
*   **Backend:** REST API server (Node.js / Express)
*   **AI Layer:** Dedicated service module within the backend that interfaces with the Anthropic Claude API
*   **Database:** PostgreSQL (relational)
*   **Real-time:** WebSockets for live notifications
*   **Auth:** JWT-based stateless authentication

## 3. High-Level Component Diagram
graph TD
    subgraph CLIENT_LAYER ["CLIENT LAYER"]
        direction TB
        React_Node["React SPA (Vite + TailwindCSS)
        - Dashboard / Projects / Tasks / Notifications
        - AI-powered UI components (summaries, hints)"]
    end

    subgraph API_LAYER ["API LAYER"]
        direction TB
        subgraph Express_Node ["Node.js / Express REST API"]
            Auth["Auth
            Module"]
            Proj["Projects
            Module"]
            Task["Tasks
            Module"]
            Comm["Comments
            Module"]
            Notif["Notif.
            Module"]
            AISvc["AI Service
            Module"]
        end
    end

    subgraph External_Node [" "]
        Claude["Anthropic Claude API
        (claude-sonnet-4)"]
    end

    subgraph DATA_LAYER ["DATA LAYER"]
        DB["PostgreSQL Database
        Users | Projects | Tasks | Comments | Notifs"]
    end

    CLIENT_LAYER -- "HTTPS / WebSocket" --> API_LAYER
    AISvc -- "HTTPS" --> Claude
    API_LAYER -.-> DATA_LAYER