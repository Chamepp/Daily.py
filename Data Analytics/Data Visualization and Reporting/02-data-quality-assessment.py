import pandas as pd

def assess_data_quality(data):
    # Calculate data quality metrics
    completeness = data.count() / len(data)
    accuracy = data.dropna().apply(lambda col: col.astype(str).str.isnumeric()).mean()
    consistency = data.apply(lambda col: col.nunique() / len(col))
    uniqueness = data.apply(lambda col: len(col.unique()) / len(col))

    # Create data quality report
    report = pd.DataFrame({
        'Completeness': completeness,
        'Accuracy': accuracy,
        'Consistency': consistency,
        'Uniqueness': uniqueness
    })

    return report

# Example usage
data = pd.read_csv('data.csv')  # Replace 'data.csv' with your data file

data_quality_report = assess_data_quality(data)
print(data_quality_report)

