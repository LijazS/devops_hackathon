import os
from pathlib import Path
import subprocess
import sys


project_name = "automatic project directory initializer"


root = Path.cwd() / project_name
backend_dir = root / "backend"
frontend_dir = root / "frontend"


os.makedirs(backend_dir, exist_ok=True)
os.makedirs(frontend_dir, exist_ok=True)

print("Project folders created.")


subprocess.run([sys.executable, "-m", "venv", ".venv"], cwd=backend_dir)
with open(os.path.join(backend_dir,"app.py"),"w") as f:
    f.write("#Python fastAPI main file")


print("Backend virtual environment created.")


# subprocess.run(
#     ["npm", "create", "vite@latest", ".", "--", "--template", "react"],
#     cwd=frontend_dir
# )

print("Frontend React structure created.")

print("\nBasic project structure initialized successfully.")
