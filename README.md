# User Management Application

A containerized user management application built with Docker, featuring a PostgreSQL database backend and a web application frontend.

## Prerequisites

- Docker installed on your system
- Docker Compose (optional, for alternative setup)

## Quick Start

Follow these steps to get the application running:

### 1. Build the Application Image

```bash
docker image build -t user_management .
```

### 2. Create Docker Network

```bash
docker network create user_management_network
```

### 3. Create Docker Volume

```bash
docker volume create user_management_volume
```

### 3. Start PostgreSQL Database

```bash
docker run -d \
  -p 8889:5432 \
  -e POSTGRES_USER=maissen \
  -e POSTGRES_PASSWORD=maissen \
  -e POSTGRES_DB=user_management \
  --network user_management_network \
  -v user_management_volume:/var/lib/postgresql/data \
  --name user_management_postgres \
  postgres:17-alpine
```

### 4. Start the Application

```bash
docker container run -d -p 8100:8000 --network user_management_network --name user_platform user_management:latest
```

## Access Information

- **Application**: http://localhost:8100
- **Database**: localhost:8889
  - Username: `maissen`
  - Password: `maissen`
  - Database: `user_management`

## Architecture

- **Database**: PostgreSQL 17 Alpine running on port 8889
- **Application**: User management service running on port 8100
- **Network**: Custom Docker network `user_management_network` for container communication

## Container Details

| Container Name | Image | Port Mapping | Purpose |
|----------------|-------|--------------|---------|
| user_management_postgres | postgres:17-alpine | 8889:5432 | Database server |
| user_platform | user_management:latest | 8100:8000 | Web application |

## Management Commands

### View Running Containers
```bash
docker ps
```

### View Container Logs
```bash
# Application logs
docker logs user_platform

# Database logs
docker logs user_management_postgres
```

### Stop Containers
```bash
docker stop user_platform user_management_postgres
```

### Remove Containers
```bash
docker rm user_platform user_management_postgres
```

### Remove Network
```bash
docker network rm user_management_network
```

### Complete Cleanup
```bash
# Stop and remove containers
docker stop user_platform user_management_postgres
docker rm user_platform user_management_postgres

# Remove network
docker network rm user_management_network

# Remove image (optional)
docker rmi user_management:latest
```

## Troubleshooting

### Container Won't Start
1. Check if ports are already in use:
   ```bash
   netstat -tlnp | grep :8100
   netstat -tlnp | grep :8889
   ```

2. View container logs:
   ```bash
   docker logs user_platform
   docker logs user_management_postgres
   ```

### Database Connection Issues
1. Ensure both containers are on the same network:
   ```bash
   docker network inspect user_management_network
   ```

2. Test database connectivity:
   ```bash
   docker exec -it user_management_postgres psql -U maissen -d user_management
   ```
