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
    subgraph "CLIENT LAYER"
        A["React SPA (Vite + TailwindCSS)
        - Dashboard / Projects / Tasks / Notifications
        - AI-powered UI components (summaries, hints)"]
    end

    A -- "HTTPS / WebSocket" --> B

    subgraph "API LAYER"
        direction TB
        B["Node.js / Express REST API"]
        
        subgraph Modules
            direction LR
            M1[Auth Module]
            M2[Projects Module]
            M3[Tasks Module]
            M4[Comments Module]
            M5[Notif. Module]
            M6[AI Service Module]
        end
        
        B --- M1
        B --- M2
        B --- M3
        B --- M4
        B --- M5
        B --- M6
    end

    M6 -- "HTTPS" --> C["Anthropic Claude API (claude-sonnet-4)"]
    B -- "HTTPS" --> D

    subgraph "DATA LAYER"
        D["PostgreSQL Database
        Users | Projects | Tasks | Comments | Notifs"]
    end