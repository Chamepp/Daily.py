import requests

def generate_recipe(ingredients):
    # API endpoint for recipe search
    endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
    
    # API key for accessing Spoonacular API (Replace with your own API key)
    api_key = "YOUR_API_KEY"
    
    # Parameters for the API request
    params = {
        "apiKey": api_key,
        "ingredients": ",".join(ingredients),
        "number": 1,  # Number of recipes to generate
        "ranking": 1   # Ranking method for the generated recipes
    }
    
    try:
        # Sending the API request
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        
        # Parsing the JSON response
        recipe_data = response.json()
        
        if len(recipe_data) > 0:
            recipe = recipe_data[0]
            recipe_title = recipe["title"]
            recipe_id = recipe["id"]
            
            print("Recipe found:")
            print("Title:", recipe_title)
            print("ID:", recipe_id)
            print("You can find the full recipe at:", "https://spoonacular.com/recipes/" + str(recipe_id))
        else:
            print("No recipe found for the given ingredients.")
    
    except requests.exceptions.RequestException as e:
        print("Error occurred during API request:", str(e))

# Example usage
available_ingredients = ["chicken", "broccoli", "garlic", "soy sauce"]
generate_recipe(available_ingredients)
