import subprocess
import os


def run_tests(repo_path):

    service_path = os.path.join(repo_path, "node-service")

    print("\nStarting Docker build...")

    subprocess.run(
        ["docker", "build", "-t", "shopstack-test", "."],
        cwd=service_path
    )

    print("\nRunning tests inside container...")

    result = subprocess.run(
        ["docker", "run", "--rm", "shopstack-test"],
        cwd=service_path,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    print("\nTest STDOUT:\n")
    print(result.stdout)

    print("\nTest STDERR:\n")
    print(result.stderr)

    return result.returncode == 0
