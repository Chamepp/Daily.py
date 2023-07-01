import subprocess

def build():
    # Perform build operations (e.g., compiling code, running tests)
    subprocess.run(["./build.sh"])

def test():
    # Run automated tests
    subprocess.run(["./run_tests.sh"])

def deploy():
    # Deploy the application to a specific environment
    subprocess.run(["./deploy.sh", "--environment", "production"])

def main():
    build()
    test()
    deploy()

if __name__ == "__main__":
    main()

