from pathlib import Path

# Base path
BASE_PATH = Path("P:/FastAPI_Roadmap")

roadmap = {
    "Week01_Fundamentals": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/routes.py",
        "app/models.py",
    ],
    "Week02_CRUD_Pydantic_Routers": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/routers/posts.py",
        "app/models.py",
        "app/schemas.py",
        "app/crud.py",
    ],
    "Week03_Database_SQLAlchemy": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/database.py",
        "app/models.py",
        "app/schemas.py",
        "app/crud.py",
        "app/routers/posts.py",
        "app/routers/users.py",
    ],
    "Week04_Authentication_JWT": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/database.py",
        "app/models.py",
        "app/schemas.py",
        "app/crud.py",
        "app/routers/auth.py",
        "app/core/security.py",
    ],
    "Week05_Async_BackgroundTasks": [
        "main.py",
        "README.md",
        "app/__init__.py",
        "app/routers/tasks.py",
        "app/services/email.py",
        "app/services/external_api.py",
    ],
    "Week06_Testing_Env_Config": [
        "main.py",
        "README.md",
        ".env",
        "app/__init__.py",
        "app/config.py",
        "tests/test_auth.py",
        "tests/test_posts.py",
    ],
    "Week07_Docker_Deployment": [
        "main.py",
        "README.md",
        "Dockerfile",
        "docker-compose.yml",
        "app/__init__.py",
        "app/main.py",
    ],
}

def create_file(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {path.name}\n")
        print(f"Created: {path}")

for week, files in roadmap.items():
    week_dir = BASE_PATH / week
    week_dir.mkdir(parents=True, exist_ok=True)

    for file in files:
        file_path = week_dir / file
        create_file(file_path)

# Base README
base_readme = BASE_PATH / "README.md"

if not base_readme.exists():
    base_readme.write_text(
        "# FastAPI Roadmap\n\nStructured weekly roadmap for learning FastAPI.\n"
    )

print("FastAPI roadmap structure created successfully.")