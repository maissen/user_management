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


### 4. Start the Application

```bash
docker compose up -d
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

### Stop Application
```bash
docker compose down
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
