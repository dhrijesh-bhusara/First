import os
import subprocess

REPO_URL = "https://github.com/Rezinix-AI/shopstack-platform.git"
REPO_PATH = "repo/shopstack-platform"

def clone_repo():

    if not os.path.exists(REPO_PATH):
        print("Cloning repository...")

        subprocess.run([
            "git",
            "clone",
            REPO_URL,
            REPO_PATH
        ])

        print("Repository cloned.")

    else:
        print("Repository already exists.")

    return REPO_PATH


def scan_files(repo_path):

    code_files = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith((".js", ".ts", ".py")):

                full_path = os.path.join(root, file)
                code_files.append(full_path)

    return code_files

def search_related_files(files, keywords):

    matched_files = []

    for file in files:

        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

                for word in keywords:

                    if word.lower() in content.lower():
                        matched_files.append(file)
                        break

        except:
            pass

    return matched_files

