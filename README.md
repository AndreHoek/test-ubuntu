# HTML Hello World - Python Flask Docker Project

A simple Python Flask application that displays "Hello World" in an HTML page, running in a Docker container.

## Project Structure

```
HelloWorldHTML/
├── app.py                 # Flask application
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Prerequisites

- Docker Desktop installed and running
- Docker Compose (included with Docker Desktop)

## Quick Start

1. **Clone or navigate to the project directory:**
   ```bash
   cd HelloWorldHTML
   ```

2. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   - Open your browser and go to: `http://localhost:5000`
   - You should see the "Hello World!" page

4. **Stop the application:**
   ```bash
   docker-compose down
   ```

## Features

- Simple Flask web server
- Responsive HTML page with styling
- Volume mounting for live code changes (in development mode)
- Runs on port 5000

## Development

The container is configured with volume mounting, so any changes you make to `app.py` will be reflected immediately in the running container.

## Docker Commands

### Build and start
```bash
docker-compose up --build
```

### Run in background
```bash
docker-compose up -d
```

### View logs
```bash
docker-compose logs -f
```

### Stop services
```bash
docker-compose down
```

### Remove containers and images
```bash
docker-compose down -v
```

## Notes

- The Flask development server is enabled by default
- The application binds to all interfaces (0.0.0.0) on port 5000
- For production, consider disabling debug mode and using a production WSGI server like Gunicorn
