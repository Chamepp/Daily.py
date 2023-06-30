import scipy.stats as stats

def hypothesis_testing(sample_data, hypothesis_mean):
    # Perform one-sample t-test
    t_statistic, p_value = stats.ttest_1samp(sample_data, hypothesis_mean)

    # Compare p-value with significance level (e.g., 0.05)
    if p_value < 0.05:
        result = "Reject the null hypothesis"
    else:
        result = "Fail to reject the null hypothesis"

    # Return the test result and other statistics
    return {
        "t_statistic": t_statistic,
        "p_value": p_value,
        "hypothesis_mean": hypothesis_mean,
        "result": result
    }

# Example usage
sample_data = [1.8, 1.6, 2.2, 1.9, 2.3, 1.7, 1.5, 1.8, 2.1, 1.7]
hypothesis_mean = 2.0

result = hypothesis_testing(sample_data, hypothesis_mean)
print("One-sample t-test result:")
print("Hypothesis Mean:", result['hypothesis_mean'])
print("t-statistic:", result['t_statistic'])
print("p-value:", result['p_value'])
print("Result:", result['result'])

