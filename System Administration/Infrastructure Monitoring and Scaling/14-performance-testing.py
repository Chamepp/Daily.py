import subprocess

def run_performance_test(test_plan_path, jmeter_path, jmeter_opts):
    # Construct the JMeter command
    command = [jmeter_path, '-n', '-t', test_plan_path]
    command.extend(jmeter_opts)

    try:
        # Run the JMeter command
        subprocess.run(command, check=True)
        print("Performance test completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Performance test failed with error:", e)

# Example usage
test_plan_path = '/path/to/test_plan.jmx'
jmeter_path = '/path/to/jmeter/bin/jmeter.sh'
jmeter_opts = ['-l', '/path/to/results.jtl']

run_performance_test(test_plan_path, jmeter_path, jmeter_opts)

