from agents.ticket_parser import parse_ticket
from utils.logger import log
from agents.code_analyzer import clone_repo, scan_files, search_related_files
from agents.root_cause_finder import analyze_code
from agents.fix_generator import generate_fix, apply_fix
from agents.test_generator import generate_test, save_test
from agents.sandbox_runner import run_tests


def load_ticket():
    with open("data/sample_ticket.txt", "r") as f:
        return f.read()


def main():

    log("Loading ticket...")
    ticket = load_ticket()

    log("Parsing incident ticket")
    result = parse_ticket(ticket)
    print(result)

    log("Cloning repository")
    repo_path = clone_repo()

    log("Scanning codebase")
    files = scan_files(repo_path)

    log(f"Total files found: {len(files)}")

    keywords = ["checkout", "price", "product"]

    related = search_related_files(files, keywords)

    print("\nPossible related files:")
    for f in related[:10]:
        print(f)

    log("Finding possible bug locations")

    related = search_related_files(files, keywords)

    print("\nPossible related files:")
    for f in related[:5]:
        print(f)

    log("Running root cause analysis")

    root_cause = analyze_code(ticket, related)

    print("\nRoot Cause Analysis:\n")
    print(root_cause)

    log("Generating fix")

    target_file = related[0]

    fixed_code = generate_fix(ticket, target_file)

    log("Applying fix")

    backup = apply_fix(target_file, fixed_code)

    print("\nFile fixed:")
    print(target_file)

    print("\nBackup saved at:")
    print(backup)

    log("Generating test case")

    test_code = generate_test(target_file)

    test_file = save_test(target_file, test_code)

    print("\nTest file created:")
    print(test_file)

    log("Running tests inside sandbox")

    tests_passed = run_tests(repo_path)

    if tests_passed:
        print("\nTests passed successfully")
    else:
        print("\nTests failed")


if __name__ == "__main__":
    main()