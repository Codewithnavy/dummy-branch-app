# Design Decisions

## Containerization
- **Multi-stage Build**: Used a multi-stage Dockerfile to keep the final image size small by excluding build dependencies.
- **Non-root User**: Created an `appuser` to run the application for better security.
- **Nginx Reverse Proxy**: Added Nginx to handle SSL termination and serve as a reverse proxy. This mimics a production setup where the application server (Gunicorn) shouldn't be directly exposed.

## Multi-Environment Setup
- **Docker Compose Overrides**: Used `docker-compose.override.yml` for development defaults (hot reload, debug mode) and specific files for staging and production. This avoids code duplication.
- **Environment Variables**: Configuration is driven by environment variables, allowing easy switching between environments without changing code.

## CI/CD Pipeline
- **GitHub Actions**: Chosen for its tight integration with the repository.
- **Trivy Scanning**: Added for security vulnerability scanning of the Docker image.
- **Conditional Push**: Images are only pushed to the registry on merges to the `main` branch to prevent unstable images from reaching production.

## Trade-offs
- **Self-Signed Certs**: Used self-signed certificates for local development. In a real production environment, we would use Let's Encrypt or a paid certificate authority.
- **Database Persistence**: Local volumes are used for persistence. In production, a managed database service (like AWS RDS) would be preferred over a containerized database.
- **Secrets Management**: Secrets are currently passed via environment variables. In a more advanced setup, a secret manager (like HashiCorp Vault or AWS Secrets Manager) should be used.
