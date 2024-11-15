import pandas as pd
import ast

# Load the dataset
file_path = r"C:\Users\brand\Projects\Recipe Recommender\recipe-recommender-system\data\Food Ingredients and Recipe Dataset with Image Name Mapping.csv"
data = pd.read_csv(file_path)

# Function to clean and standardize ingredients
def preprocess_ingredients(ingredients_str):
    try:
        # Convert string representation of list to an actual list
        ingredients = ast.literal_eval(ingredients_str)
        # Clean and standardize each ingredient
        cleaned = [ingredient.lower().strip() for ingredient in ingredients]
        return cleaned
    except Exception as e:
        return []  # Return an empty list in case of any error

# Apply the preprocessing function to the 'Cleaned_Ingredients' column
data['Processed_Ingredients'] = data['Cleaned_Ingredients'].apply(preprocess_ingredients)

# Save the preprocessed dataset for future use
output_file_path = "processed_recipe_dataset.csv"
data.to_csv(output_file_path, index=False)

print(f"Preprocessing complete. Processed data saved to {output_file_path}.")
