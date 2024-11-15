import pytesseract
from PIL import Image
import re
import os

# Specify the path to Tesseract executable (adjust as necessary)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Default abbreviation mapping
ABBREVIATION_MAPPING = {
    "tsp": "teaspoon",
    "tbsp": "tablespoon",
    "oz": "ounce",
    "lb": "pound",
    "pkg": "package",
    # Add more abbreviations as needed
}

def update_abbreviation_mapping(new_mappings):
    """
    Updates the abbreviation mapping with user-provided mappings.

    Args:
        new_mappings (dict): A dictionary of abbreviations to add or update.
    """
    ABBREVIATION_MAPPING.update(new_mappings)

def expand_abbreviations(line, abbreviation_mapping):
    """
    Expands abbreviations in a line using the abbreviation mapping.

    Args:
        line (str): A single line of text.
        abbreviation_mapping (dict): Dictionary mapping abbreviations to full terms.

    Returns:
        str: The line with abbreviations expanded.
    """
    words = line.split()
    expanded_words = [abbreviation_mapping.get(word, word) for word in words]
    return " ".join(expanded_words)

def filter_numeric_lines(ocr_lines):
    """
    Removes lines that are only numeric or mostly numeric.

    Args:
        ocr_lines (list): List of text lines extracted by OCR.

    Returns:
        list: Filtered list of lines with non-numeric descriptions.
    """
    filtered_lines = []
    for line in ocr_lines:
        # Remove lines with only numbers or mostly numbers
        if not re.fullmatch(r"[0-9\.\,\-\s]*", line):  # Exclude lines mostly numeric
            filtered_lines.append(line)
    return filtered_lines

def clean_ocr_output(ocr_text, abbreviation_mapping):
    """
    Cleans OCR output to extract likely ingredients, expanding abbreviations.

    Args:
        ocr_text (str): Raw text output from OCR.
        abbreviation_mapping (dict): Dictionary mapping abbreviations to full terms.

    Returns:
        list: Cleaned and filtered list of ingredients.
    """
    # Split text into lines and normalize
    ocr_lines = [line.strip().lower() for line in ocr_text.split("\n") if line.strip()]

    # Step 1: Remove numeric-only lines
    filtered_lines = filter_numeric_lines(ocr_lines)

    # Step 2: Expand abbreviations in each line
    expanded_lines = [expand_abbreviations(line, abbreviation_mapping) for line in filtered_lines]

    return expanded_lines

def extract_ingredients_from_image(image_path, abbreviation_mapping=ABBREVIATION_MAPPING):
    """
    Extract ingredients from an image using Tesseract OCR.

    Args:
        image_path (str): Path to the image file.
        abbreviation_mapping (dict): Dictionary mapping abbreviations to full terms.

    Returns:
        list: A list of cleaned and filtered ingredients.
    """
    try:
        # Open the image file
        image = Image.open(image_path)

        # Extract raw text using OCR
        raw_text = pytesseract.image_to_string(image)

        # Clean and filter the raw OCR output
        ingredients = clean_ocr_output(raw_text, abbreviation_mapping)

        return ingredients
    except Exception as e:
        print(f"Error during OCR processing: {e}")
        return []

if __name__ == "__main__":
    # Adjust the file path to reference the data folder at the project root
    image_path = r"../data/sample_receipt.jpg"

    # Check if the file exists
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
    else:
        # Optional: Update abbreviation mappings
        update_abbreviation_mapping({
            "gm": "gram",
            "ml": "milliliter",
            "ltr": "liter",
        })

        # Extract ingredients
        ingredients = extract_ingredients_from_image(image_path)
        print("Extracted Ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
