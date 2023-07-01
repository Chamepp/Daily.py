def generate_code(template, values):
    """
    Generate code based on a template by replacing placeholders with provided values.
    
    Args:
        template (str): The template string containing placeholders.
        values (dict): A dictionary mapping placeholders to their corresponding values.
    
    Returns:
        str: The generated code with placeholders replaced by values.
    """
    for placeholder, value in values.items():
        template = template.replace(placeholder, str(value))
    return template

# Example usage
template = """
def greet(name):
    print("Hello, {name}!")

greet("{person}")
"""

values = {
    "{person}": "John Doe"
}

generated_code = generate_code(template, values)
print(generated_code)
