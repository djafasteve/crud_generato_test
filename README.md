# Recipe API

A small FastAPI application to manage cooking recipes. It stores data in a JSON file and exposes a simple CRUD API documented with Swagger.

## Requirements

- Docker

## Usage

### With Docker Compose

Start the API using [Docker Compose](https://docs.docker.com/compose/):

```bash
docker compose up --build
```

The service exposes port `8000`. Access the interactive API docs at
[http://localhost:8000/docs](http://localhost:8000/docs).

### Manual Docker build

If you prefer the plain `docker` command, build the image and run it manually:

```bash
docker build -t recipe-api .
docker run -p 8000:8000 recipe-api
```
