# CLAUDE.md — Saleor Backend

## Project structure

- Backend: `C:\development\saleor_project\saleor\`
- Docker platform: `C:\development\saleor_project\saleor_platform\`
- Frontend: `C:\development\saleor_project\front_store\`

## Stack

- Python 3.12, Django 5.2.13
- GraphQL API: graphene 2.x, graphql-core 2.x
- PostgreSQL (psycopg 3.x), Redis 5.x
- Celery (redis + sqs), uvicorn ASGI server
- Pydantic 2.x, OpenTelemetry
- Package manager: uv (lockfile: `uv.lock`)

## Docker setup

- Images: `ghcr.io/saleor/saleor:3.23.1` (api + worker)
- Compose file: `saleor_platform/docker-compose.yml`
- To apply a Python file change without rebuild:
  ```
  docker compose cp <local_file> api:/app/<path>
  docker compose restart api
  ```

## How to apply backend changes

Do NOT use `build: context` in docker-compose.yml — the pre-built image works.
To patch a file:
1. Edit the file locally in `saleor/`
2. Copy it into the running container: `docker compose cp ...`
3. Restart the service: `docker compose restart api`

## Running tests

```
pytest --reuse-db                          # full suite with db reuse
pytest path/to/test_file.py --reuse-db    # single file
```

## Pending tasks

- [ ] Fix Arabic search: modify `saleor/graphql/product/filters.py` to include
      `ProductTranslation.name` in the search query when language != EN
      (see `front_store/CLAUDE.md` for full context)

## Known issues

- `authorizenet==1.1.6` and `pybars3==0.9.7` fail to build on Python 3.12
  with modern setuptools — do NOT attempt local Docker build from source
  until this is resolved. Use the pre-built `ghcr.io` image instead.

## Rules

- DO NOT modify `uv.lock` manually
- DO NOT change `requires-python` in `pyproject.toml`
- DO NOT change build strategy in `docker-compose.yml` without approval
- Always use `docker compose cp` + `restart` for single-file changes
- See `AGENTS.md` for GraphQL versioning conventions and test guidelines
