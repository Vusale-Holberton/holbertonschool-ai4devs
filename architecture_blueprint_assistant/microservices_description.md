# Microservices Architecture – SmartTravel

This architecture transitions the SmartTravel application into a distributed system where each business capability is managed by a dedicated, independent service. This enables high availability and individual service scaling.

## Services & Responsibilities

- **API Gateway**: Acts as the single entry point. It manages routing, load balancing, and cross-cutting concerns like logging and security.
- **Identity Service (Auth)**:
    - **Purpose**: Handles all authentication and authorization requests.
    - **Database**: Dedicated **PostgreSQL** for user credentials and role management.
    - **Tech**: Uses OAuth2/JWT for stateless verification across other services.
- **AI Planning Service**:
    - **Purpose**: The brain of the app, generating travel itineraries based on machine learning models.
    - **Database**: **MongoDB** for flexible, unstructured travel data storage.
- **Gamification Service**:
    - **Purpose**: Manages points, streaks, and user rewards independently.
    - **Database**: **Redis** for fast, real-time leaderboard updates and session-based achievements.
- **Logistics Sandbox Service**:
    - **Purpose**: Executes heavy computational logic for travel routes in a secure, isolated environment.
- **Content Service (Curriculum)**:
    - **Purpose**: Serves travel guides, destination details, and maps.
    - **Database**: **Elasticsearch** for high-performance content searching.
- **Social & Review Service**:
    - **Purpose**: Manages peer interactions, reviews, and community feedback.

## System Interactions

- **Service Communication**: Services communicate asynchronously via a **Message Broker (RabbitMQ/Kafka)** to ensure that if one service is down, the system remains resilient.
- **Data Isolation**: No service can directly access another service's database. All data sharing happens through well-defined REST or gRPC APIs.

## Advantages of this Migration
- **Scalability**: During peak seasons, only the **Booking** and **AI Planning** services can be scaled up, saving cloud costs.
- **Fault Tolerance**: A failure in the **Social Service** does not prevent users from accessing their itineraries or logging in.
- **Faster Deployment**: Each team can deploy updates to their specific microservice without requiring a full system reboot.