import subprocess

def run_unit_tests():
    # Run unit tests using your preferred test runner or framework
    subprocess.run(['python', '-m', 'unittest', 'discover', 'tests/'])

def run_integration_tests():
    # Run integration tests using your preferred test runner or framework
    subprocess.run(['python', '-m', 'pytest', 'tests/integration/'])

def run_ci():
    # Execute the CI pipeline steps
    print("Running Continuous Integration...")

    # Step 1: Fetch the latest code from the repository
    subprocess.run(['git', 'pull'])

    # Step 2: Install project dependencies
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

    # Step 3: Run unit tests
    run_unit_tests()

    # Step 4: Run integration tests
    run_integration_tests()

    # Additional steps: Code analysis, linting, etc.

    print("Continuous Integration completed successfully.")

# Execute the CI script
if __name__ == "__main__":
    run_ci()

