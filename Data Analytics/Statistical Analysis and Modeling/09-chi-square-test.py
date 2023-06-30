import scipy.stats as stats

def perform_ab_test(control_group, experimental_group):
    # Perform A/B test using chi-square test
    _, p_value = stats.chisquare(control_group, experimental_group)
    
    # Compare p-value with significance level
    significance_level = 0.05
    
    if p_value < significance_level:
        print("Statistically significant results: There is a significant difference between the groups.")
    else:
        print("Not statistically significant results: There is no significant difference between the groups.")

# Example usage
control_group = [20, 25, 22, 19, 24]  # Number of conversions in control group
experimental_group = [18, 23, 25, 21, 20]  # Number of conversions in experimental group

perform_ab_test(control_group, experimental_group)

