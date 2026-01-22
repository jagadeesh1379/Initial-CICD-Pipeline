# deploy.py
import subprocess

IMAGE_NAME = "python-cicd-demo"
CONTAINER_NAME = "python-app"

def run_command(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, check=False)
    if result.returncode != 0:
        print(f"Warning: Command failed with exit code {result.returncode}")

def main():
    # Build Docker image
    run_command(f"docker build -t {IMAGE_NAME} .")

    # Stop old container
    run_command(f"docker stop {CONTAINER_NAME}")
    run_command(f"docker rm {CONTAINER_NAME}")

    # Run new container
    run_command(f"docker run -d -p 5000:5000 --name {CONTAINER_NAME} {IMAGE_NAME}")

if __name__ == "__main__":
    main()