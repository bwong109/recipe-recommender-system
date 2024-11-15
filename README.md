
# **Recipe Recommender System**

A user-friendly, interactive recipe recommender application that allows users to manage their ingredient inventory, extract ingredients from images using OCR, and receive recipe recommendations based on available ingredients. Designed with simplicity and modularity in mind, this project combines a Flask-powered backend with a sleek, food-themed frontend.

---

## **Features**

1. **Inventory Management**:
   - Add ingredients to your inventory.
   - Remove ingredients you no longer have.
   - View your inventory in an interactive web interface.

2. **OCR-Based Ingredient Extraction**:
   - Upload images (e.g., grocery receipts or handwritten notes).
   - Automatically extract ingredients using OCR.

3. **Recipe Recommendations**:
   - Get recipe recommendations based on your inventory and additional ingredients.
   - View detailed recipe instructions and required ingredients.

4. **Interactive Web Interface**:
   - Simple and intuitive design inspired by food companies.
   - Responsive and visually appealing layout.

---

## **Project Structure**

```
recipe-recommender-system/
├── app.py                      # Main Flask application
├── data/                       # Data directory
│   ├── inventory.json          # Persistent storage for the inventory
│   ├── processed_recipe_dataset.csv # Preprocessed recipe dataset
│   └── sample_receipt.jpg      # Sample image for OCR testing
├── uploads/                    # Temporary directory for uploaded images
├── static/                     # Static assets
│   ├── css/
│   │   └── styles.css          # Custom CSS for the frontend
├── templates/                  # HTML templates
│   ├── index.html              # Main page template
│   ├── recommendations.html    # Recipe recommendations page
├── src/                        # Backend modules
│   ├── __init__.py             # Makes src a package
│   ├── ingredient_matching.py  # Recipe recommendation logic
│   ├── inventory.py            # Inventory management
│   ├── ocr_integration.py      # OCR functionality
```

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.7 or higher
- Tesseract-OCR installed on your system
  - [Download Tesseract](https://github.com/tesseract-ocr/tesseract)

### **2. Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/recipe-recommender-system.git
   cd recipe-recommender-system
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Linux/Mac
   venv\Scripts\activate         # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure Tesseract-OCR is installed and update the path in `src/ocr_integration.py`:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

5. Prepare directories:
   ```bash
   mkdir uploads
   ```

### **3. Running the Application**
1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## **Usage**

### **1. Inventory Management**
- **Add Ingredients**: Enter a comma-separated list of ingredients to add.
- **Remove Ingredients**: Specify the ingredients to remove from your inventory.
- **View Inventory**: See a complete list of your current ingredients.

### **2. Upload Images for OCR**
- Upload an image of a grocery receipt or ingredient list.
- The application will extract ingredients and add them to your inventory.

### **3. Get Recipe Recommendations**
- Use your inventory and optionally add extra ingredients to find the best-matching recipes.
- View recipe details, including ingredients and instructions.

---

## **Demo**

### **Home Page**
- Manage inventory.
- Upload images for OCR-based ingredient extraction.
- Request recipe recommendations.

### **Recipe Recommendations**
- See a list of recommended recipes based on your inventory.
- Click to view detailed instructions and ingredients.

---

## **Technologies Used**

1. **Backend**:
   - Flask (Python)
   - Tesseract-OCR (OCR functionality)

2. **Frontend**:
   - HTML5
   - CSS3 (with custom styling)

3. **Libraries**:
   - `pandas`: For data manipulation.
   - `scikit-learn`: For calculating similarity scores.
   - `pytesseract`: For OCR integration.

---

## **Future Enhancements**

- **User Authentication**: Allow users to create accounts and manage their inventories individually.
- **Advanced Filtering**: Filter recipes by cuisine, cooking time, or dietary preferences.
- **Database Integration**: Replace JSON storage with a relational database like SQLite or PostgreSQL.
- **Mobile-Friendly Design**: Optimize the interface for mobile users.

---

## **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## **Contributors**

- **Your Name**: Initial development and design.
- Contributions welcome! Feel free to submit pull requests or raise issues.
