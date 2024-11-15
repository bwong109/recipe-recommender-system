from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from src.inventory import load_inventory, add_to_inventory, remove_from_inventory
from src.ingredient_matching import recommend_recipes
from src.ocr_integration import extract_ingredients_from_image

app = Flask(__name__)

# Path configurations
base_dir = os.path.dirname(os.path.abspath(__file__))
recipe_dataset_path = os.path.join(base_dir, "data/processed_recipe_dataset.csv")
uploads_dir = os.path.join(base_dir, "uploads")
os.makedirs(uploads_dir, exist_ok=True)

app.config["UPLOAD_FOLDER"] = uploads_dir
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/")
def index():
    """Home page for inventory management."""
    inventory = load_inventory()
    return render_template("index.html", inventory=sorted(inventory))

@app.route("/add", methods=["POST"])
def add_ingredient():
    """Add ingredients to the inventory."""
    ingredients = request.form.get("ingredients", "").split(",")
    add_to_inventory([ingredient.strip().lower() for ingredient in ingredients])
    return redirect(url_for("index"))

@app.route("/remove", methods=["POST"])
def remove_ingredient():
    """Remove ingredients from the inventory."""
    ingredients = request.form.get("ingredients", "").split(",")
    remove_from_inventory([ingredient.strip().lower() for ingredient in ingredients])
    return redirect(url_for("index"))

@app.route("/upload", methods=["POST"])
def upload_image():
    """Handle image upload and extract ingredients using OCR."""
    if "file" not in request.files:
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "" or not allowed_file(file.filename):
        return redirect(url_for("index"))

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    # Extract ingredients using OCR
    extracted_ingredients = extract_ingredients_from_image(filepath)
    add_to_inventory(extracted_ingredients)

    # Clean up uploaded file
    os.remove(filepath)

    return redirect(url_for("index"))

@app.route("/recommend", methods=["POST"])
def recommend():
    """Get recipe recommendations."""
    additional_ingredients = request.form.get("additional_ingredients", "").split(",")
    inventory = load_inventory()
    all_ingredients = list(inventory.union([ingredient.strip().lower() for ingredient in additional_ingredients if ingredient.strip()]))
    recommended = recommend_recipes(all_ingredients, recipe_dataset_path, top_n=5)
    return render_template("recommendations.html", recommendations=recommended.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
