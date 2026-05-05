# AI Meal Planner & Smart Grocery Assistant

## Description
This project is a web application that generates personalized meal plans using real recipe data and generative AI.

Users can input:
- dietary goals
- calorie targets
- grocery budget
- number of days
- ingredients to avoid

The app uses the Spoonacular API to fetch real recipes and the OpenAI API to generate structured meal plan explanations, grocery lists, and recommendations.

## Features
- Multi-day meal planning
- Diet restrictions
- Ingredient exclusions
- Budget tracking
- AI-generated explanations and scoring
- Downloadable grocery list (TXT + CSV)

## APIs Used
- Spoonacular API
- OpenAI API

## How to Run

1. Clone the repo  
2. Create a virtual environment:
-python -m venv .venv
3. Activate it:
.venv\Scripts\activate
4. Install dependencies:
pip install -r requirements.txt
5. Create a `.env` file:
SPOONACULAR_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
6. Run the app:
streamlit run app.py