from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Sample transaction dataset
transactions = [['bread', 'milk', 'eggs'],
                ['bread', 'diapers', 'beer', 'eggs'],
                ['milk', 'diapers', 'beer', 'cola'],
                ['bread', 'milk', 'diapers', 'beer'],
                ['bread', 'milk', 'diapers', 'cola']]

# Convert the transaction dataset to a one-hot encoded DataFrame
def encode_transactions(transactions):
    encoded_vals = []
    for transaction in transactions:
        encoded_vals.append({item: True for item in transaction})
    return encoded_vals

encoded_transactions = encode_transactions(transactions)

# Generate frequent itemsets using the Apriori algorithm
frequent_itemsets = apriori(encoded_transactions, min_support=0.3, use_colnames=True)

# Generate association rules from frequent itemsets
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Print the association rules
print("Association Rules:")
print(rules)

