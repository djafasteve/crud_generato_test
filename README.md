# Recipe API

A small FastAPI application to manage cooking recipes. It stores data in a JSON file located at `data/recipes.json` and exposes a simple CRUD API documented with Swagger. The repository already contains an empty `data/recipes.json` file so the service can start without additional setup.

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
Recipe data will be stored in the `data/` directory on your host machine so it
persists across container runs.

### Manual Docker build

If you prefer the plain `docker` command, build the image and run it manually:

```bash
docker build -t recipe-api .
docker run -p 8000:8000 -v $(pwd)/data:/app/data recipe-api
```
=======
Build the Docker image:

```bash
docker build -t recipe-api .
```

Run the container:

```bash
docker run -p 8000:8000 recipe-api
```

Access the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs).