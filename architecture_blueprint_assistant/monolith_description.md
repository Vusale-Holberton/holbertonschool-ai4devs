# Monolithic Architecture – SmartTravel

This monolithic architecture centralizes all business logic into a single codebase and deployment unit. While this approach simplifies cross-module communication, it creates tight coupling between the components.

## Components & Responsibilities

- **Web & Mobile Frontend**: The primary interface for users to interact with travel plans, view itineraries, and access rankings.
- **Auth & Session Module**: Manages secure access, verifying identity before any other module is engaged.
- **Gamification Engine**: The core logic for tracking user progress, distributing rewards (CO2 points/badges), and maintaining travel streaks.
- **AI Adaptive Learning Path**: Evaluates user travel history to dynamically update the difficulty and relevance of the next travel curriculum or suggestion.
- **Code Execution Sandbox**: A secure environment that executes travel logic calculations and sends pass/fail signals to the gamification engine.
- **Curriculum Manager**: Acts as the content repository, delivering travel tasks and destination projects to the user via the Sandbox.
- **Peer Review System**: Allows users to validate each other's travel tips, triggering rewards in the Gamification Engine upon successful review.
- **Battle Arena Module**: Facilitates real-time logic competitions or community challenges, updating scores directly in the central database.
- **Central Database**: A shared Relational Database (PostgreSQL) where all modules store and retrieve persistent data.

## System Interactions

- **Authentication Flow**: Users must be verified by the **Auth Module** before the **Curriculum Manager** serves any content.
- **Learning Cycle**: The **AI Path** analyzes data in the **DB**, then tells the **Curriculum Manager** which travel task to provide.
- **Execution & Reward**: When a user runs logic in the **Sandbox**, the result is sent to the **Gamification Engine** to update rewards and streaks in the **DB**.

## Drawbacks of this Architecture
- **Tight Coupling**: Changes in one module (e.g., Auth) may require re-deploying the entire application.
- **Scalability Issues**: The entire monolith must be scaled even if only the AI module is under heavy load.
- **Single Point of Failure**: A bug in any single component can cause the entire system to crash.