def build():
    print("Building the application...")
    # Add your build steps here
    print("Build successful.")

def test():
    print("Running tests...")
    # Add your test steps here
    print("All tests passed.")

def deploy():
    print("Deploying the application...")
    # Add your deployment steps here
    print("Deployment successful.")

def ci_cd_pipeline():
    build()
    test()
    deploy()

# Run the CI/CD pipeline
ci_cd_pipeline()

