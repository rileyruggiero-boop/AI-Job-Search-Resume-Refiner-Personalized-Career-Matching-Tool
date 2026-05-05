# AI Meal Planner & Smart Grocery Assistant

## Description
This project is a Streamlit web application that creates personalized meal plans using real recipe data and generative AI.

Users can enter a meal goal, diet restriction, calorie target, grocery budget, number of days, and ingredients to avoid. The app uses the Spoonacular API to retrieve recipe data and the OpenAI API to generate meal plan explanations, grocery lists, budget checks, scores, and improvement tips.

## Features
- Multi-day meal planning
- Diet restrictions
- Ingredient exclusions
- Budget input
- Recipe ingredients and instructions
- AI-generated meal plan explanation
- AI scoring system
- Downloadable grocery list as TXT and CSV

## APIs Used
- Spoonacular API
- OpenAI API

## How to Run

1. Create a virtual environment:
python -m venv .venv

2. Activate it:
.venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Create a `.env` file:
SPOONACULAR_API_KEY=your_key_here  
OPENAI_API_KEY=your_key_here  

5. Run the app:
streamlit run app.py