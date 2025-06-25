# Recipe API

A small FastAPI application to manage cooking recipes. It stores data in a JSON file and exposes a simple CRUD API documented with Swagger.

## Requirements

- Docker

## Usage

Build the Docker image:

```bash
docker build -t recipe-api .
```

Run the container:

```bash
docker run -p 8000:8000 recipe-api
```

Access the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs).
