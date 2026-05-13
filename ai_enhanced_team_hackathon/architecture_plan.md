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
```mermaid
graph TD
    subgraph Client_Layer [CLIENT LAYER]
        direction TB
        React_SPA["React SPA (Vite + TailwindCSS)
        - Dashboard / Projects / Tasks / Notifications
        - AI-powered UI components (summaries, hints)"]
    end

    subgraph API_Layer [API LAYER]
        direction TB
        subgraph Express_API [Node.js / Express REST API]
            Auth[Auth Module]
            Proj[Projects Module]
            Task[Tasks Module]
            Comm[Comments Module]
            Notif[Notif. Module]
            AISvc[AI Service Module]
        end
    end

    subgraph External_API [External API]
        Claude[Anthropic Claude API\n(claude-sonnet-4)]
    end

    subgraph Data_Layer [DATA LAYER]
        DB["PostgreSQL Database
        Users | Projects | Tasks | Comments | Notifs"]
    end

    Client_Layer -- "HTTPS / WebSocket" --> API_Layer
    AISvc -- "HTTPS" --> Claude
    API_Layer -.-> Data_Layer