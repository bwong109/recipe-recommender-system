import os
from inventory import add_to_inventory, remove_from_inventory, view_inventory, load_inventory
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def calculate_similarity(user_ingredients, recipe_ingredients):
    # Similarity calculation logic remains the same
    user_ingredients_str = " ".join(user_ingredients)
    recipe_ingredients_str = recipe_ingredients.apply(lambda x: " ".join(x))
    vectorizer = CountVectorizer().fit_transform([user_ingredients_str] + recipe_ingredients_str.tolist())
    vectors = vectorizer.toarray()
    similarity_scores = cosine_similarity([vectors[0]], vectors[1:])[0]
    return pd.Series(similarity_scores, index=recipe_ingredients.index)

def recommend_recipes(user_ingredients, recipe_dataset_path, top_n=5):
    # Recommendation logic remains the same
    if not os.path.exists(recipe_dataset_path):
        raise FileNotFoundError(f"Recipe dataset not found: {recipe_dataset_path}")

    recipes = pd.read_csv(recipe_dataset_path)
    if 'Processed_Ingredients' not in recipes.columns:
        raise ValueError("The dataset must contain a 'Processed_Ingredients' column.")

    recipes['Processed_Ingredients'] = recipes['Processed_Ingredients'].apply(eval)
    recipes['Similarity_Score'] = calculate_similarity(user_ingredients, recipes['Processed_Ingredients'])
    recommended_recipes = recipes.sort_values(by='Similarity_Score', ascending=False).head(top_n)
    return recommended_recipes

def display_recommendations(recommended_recipes):
    # Display recommendations
    print("\nRecommended Recipes:")
    for idx, row in recommended_recipes.iterrows():
        print(f"{idx}. {row['Title']} (Score: {row['Similarity_Score']:.2f})")

def show_recipe_details(recipe_row):
    # Show details of a selected recipe
    print("\nRecipe Details:")
    print(f"Title: {recipe_row['Title']}")
    print("\nIngredients:")
    print(recipe_row['Ingredients'])
    print("\nInstructions:")
    print(recipe_row['Instructions'])

def get_user_ingredients():
    # Prompt the user to enter ingredients
    print("Enter additional ingredients (comma-separated), or press Enter to skip:")
    additional_ingredients = input("Ingredients: ").strip().split(",")
    return [ingredient.strip().lower() for ingredient in additional_ingredients if ingredient.strip()]

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    recipe_dataset_path = os.path.join(base_dir, "../data/processed_recipe_dataset.csv")

    try:
        while True:
            print("\nWhat would you like to do?")
            print("1. Add ingredients to inventory")
            print("2. Remove ingredients from inventory")
            print("3. View inventory")
            print("4. Get recipe recommendations")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                print("Enter ingredients to add (comma-separated):")
                ingredients = input("Ingredients: ").strip().split(",")
                add_to_inventory([ingredient.strip().lower() for ingredient in ingredients])

            elif choice == "2":
                print("Enter ingredients to remove (comma-separated):")
                ingredients = input("Ingredients: ").strip().split(",")
                remove_from_inventory([ingredient.strip().lower() for ingredient in ingredients])

            elif choice == "3":
                view_inventory()

            elif choice == "4":
                inventory = load_inventory()
                user_ingredients = get_user_ingredients()
                all_ingredients = list(inventory.union(user_ingredients))
                print("\nUsing the following ingredients for recommendations:")
                print(", ".join(all_ingredients))

                recommended = recommend_recipes(all_ingredients, recipe_dataset_path, top_n=5)
                display_recommendations(recommended)

                print("\nEnter the number of the recipe you'd like to view:")
                recipe_index = int(input("Recipe Number: ").strip())
                if recipe_index in recommended.index:
                    selected_recipe = recommended.loc[recipe_index]
                    show_recipe_details(selected_recipe)
                else:
                    print("Invalid selection.")

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
