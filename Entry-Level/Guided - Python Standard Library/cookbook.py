import pickle # 

recipes = []

def load_recipes(filename):
    try:
        with open(filename, 'rb') as file:
            unpickler = pickle.Unpickler(file)
            return unpickler.load()
    except FileNotFoundError:
        return []

def save_recipes(recipes, filename):
    try:
        with open(filename, 'wb') as file:
            pickler = pickle.Pickler(file)
            pickler.dump(recipes)
    except pickle.PicklingError:
        print(f"Failed to save recipes.")

def add_recipe():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    instructions = input("Enter the instructions: ")
    prep_time = int(input("Enter the preparation time (in minutes): "))
    
    recipe = {
        "name": name,
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "instructions": instructions,
        "prep_time": prep_time
    }
    
    recipes.append(recipe)
    print("Recipe added successfully!")

def query_recipe():
    query_name = input("Enter the name of the recipe you want to search for: ")
    
    found_recipes = [recipe for recipe in recipes if query_name.lower() in recipe["name"].lower()]
    
    if found_recipes:
        print(f"Found {len(found_recipes)} matching recipes:")
        for recipe in found_recipes:
            print(f"\nRecipe: {recipe['name']}\nIngredients: {', '.join(recipe['ingredients'])}\nInstructions: {recipe['instructions']}\nPrep Time: {recipe['prep_time']} minutes\n")
    else:
        print("No matching recipes found.")
        
def find_recipes_by_ingredients(available_ingredients):
    matching_recipes = []
    for recipe in recipes:
        if all(ingredient in recipe['ingredients'] for ingredient in available_ingredients):
            matching_recipes.append(recipe)
    return matching_recipes

def pickle_to_bytes(recipes):
    """
    🎯 Task
    1. Define a function named `pickle_to_bytes` with a parameter `recipes`.
    2. Use the `pickle.dumps` function to serialize the `recipes` data into a byte string.
    3. Return the serialized byte string.
    """
    return pickle.dumps(recipes)

def unpickle_from_bytes(pickled_data):
    """
    🎯 Task
    1. Define a function named `unpickle_from_bytes` with a parameter `pickled_data`.
    2. Use the `pickle.loads` function to deserialize the byte string back into Python data.
    3. Return the deserialized data.
    """
    return pickle.loads(pickled_data)
    
def main():
    global recipes # Ensure we can modify the global recipes list
    filename = 'recipes.pkl'
    recipes = load_recipes(filename)

    print("Welcome to the Recipe Book CLI Application!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add a new recipe")
        print("2. Query recipes")
        print("3. Search by ingredients")
        print("4. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            add_recipe()
        elif choice == "2":
            query_recipe()
        elif choice == "3":
            available_ingredients = input("Enter the ingredients you have (comma-separated): ").split(',')
            available_ingredients = [ingredient.strip() for ingredient in available_ingredients]
            
            matching_recipes = find_recipes_by_ingredients(available_ingredients)
            
            if matching_recipes:
                print("You can make the following recipes:")
                for recipe in matching_recipes:
                    print(recipe['name'])
            else:
                print("No recipes found with the given ingredients.")
        elif choice == "4":
            save_recipes(recipes, filename) # Saving recipes before exiting
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()