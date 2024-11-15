
# **Recipe Recommender System**  
**Location:** Los Angeles, CA  
**Type:** Personal Project  

## **Overview**  
This project is a mobile app that leverages machine learning and OCR technology to create a recipe recommender system. It suggests recipes based on available ingredients, allows manual recipe searches, and automatically updates user ingredient inventories by scanning grocery receipts.

---

## **Features**  
1. **User Authentication**  
   - Secure login and sign-up functionality using Firebase Authentication or JWT.

2. **Ingredient Inventory Management**  
   - **Manual Input**: Users can manually add or remove ingredients.  
   - **OCR Integration**:  
     - Uses Tesseract OCR to scan grocery receipts.  
     - Preprocesses text to extract ingredient names and quantities.  
     - Automatically updates the user’s inventory.  

3. **Recipe Recommendation**  
   - Suggests recipes based on the user's available ingredients.  
   - Implements ingredient-to-recipe matching using natural language processing (NLP).  
   - Utilizes a machine learning-powered recommendation engine to optimize suggestions.  

4. **Recipe Search**  
   - Manual search functionality for recipes by keyword or cuisine.  
   - Filters recipes by dietary restrictions or preferences (e.g., vegetarian, gluten-free).  

5. **User Preferences**  
   - Collects and stores user preferences for personalized recommendations.  

---

## **Technology Stack**  
### **Frontend**  
- React Native (cross-platform compatibility for iOS and Android).

### **Backend**  
- Flask or FastAPI for building RESTful APIs.

### **Database**  
- Firebase (real-time and user-friendly) or PostgreSQL for secure data storage.

### **OCR**  
- Tesseract OCR for grocery receipt scanning.

### **Machine Learning & NLP**  
- Python libraries such as Scikit-learn, TensorFlow, or Hugging Face for ingredient matching and recommendation optimization.

### **Recipe API**  
- Spoonacular or Edamam APIs for recipe data.

---

## **Architecture**  
```plaintext
Mobile App (React Native)
    ↓
Backend APIs (Flask/FastAPI)
    ↓
Database (Firebase/PostgreSQL)
    ↓
OCR (Tesseract) & ML Model (Python)
    ↓
External Recipe API (Spoonacular/Edamam)
```

---

## **Modules**  
### **1. User Authentication**  
- Secure login/sign-up functionality using Firebase Authentication or JWT tokens.  

### **2. Ingredient Inventory Management**  
- Dynamic list to display and manage ingredients.  
- **OCR Integration**:  
  - Extracts text from receipts using Tesseract OCR.  
  - Processes text to identify ingredients and quantities.  

### **3. Recipe Recommendation**  
- Uses NLP to tokenize and match recipe ingredients with user inventory.  
- ML-based recommendation system (collaborative filtering or content-based filtering).  

### **4. Recipe Search**  
- Allows manual recipe search using keywords or filters.  
- Integrates external recipe APIs for comprehensive search results.  

### **5. User Preferences**  
- Customizes recipe recommendations based on dietary restrictions and preferences.  

---

## **Implementation Details**  
### **Backend APIs**  
- RESTful API endpoints for:  
  - User authentication.  
  - Ingredient inventory management.  
  - Recipe recommendation and search.  

### **Machine Learning & NLP**  
- Ingredient matching uses cosine similarity or Jaccard index.  
- Recipe recommendation engine trains on public datasets like Recipe1M+.  

### **OCR Integration**  
- Tesseract OCR extracts grocery receipt data.  
- Text preprocessing identifies and updates ingredient inventories.  

### **Frontend**  
- Built with React Native for seamless cross-platform performance.  
- Key interfaces:  
  - Ingredient Inventory: Dynamic list with add/remove functionality.  
  - Recipe Recommendations: Personalized recipe feed.  
  - Recipe Search: Manual keyword or filter-based search.  

---

## **How to Run the Project**  
### **Frontend**  
1. Install dependencies:  
   ```bash
   npm install
   ```
2. Run the development server:  
   ```bash
   npm start
   ```

### **Backend**  
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
2. Start the Flask/FastAPI server:  
   ```bash
   flask run
   ```

### **OCR Setup**  
1. Install Tesseract OCR:  
   - macOS:  
     ```bash
     brew install tesseract
     ```  
   - Ubuntu:  
     ```bash
     sudo apt install tesseract-ocr
     ```
2. Integrate Tesseract with Python using the `pytesseract` library:  
   ```bash
   pip install pytesseract
   ```

---

## **Future Improvements**  
1. Enhance the recommendation engine with deep learning (e.g., transformers).  
2. Add a shopping list feature for missing recipe ingredients.  
3. Implement real-time inventory sync across multiple devices.  
4. Incorporate user feedback loops for better personalization.

---

## **Acknowledgments**  
- **Tesseract OCR** for text extraction.  
- **Spoonacular/Edamam APIs** for recipe data.  
- **Public Datasets** like Recipe1M+ for training the recommendation system.  

---

## **License**  
This project is licensed under the MIT License.  
