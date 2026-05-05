import os
import csv
import io
import requests
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

st.title("AI Meal Planner & Smart Grocery Assistant")

st.write(
    "Generate a personalized meal plan using real recipe data, nutrition information, "
    "budget goals, and AI-powered recommendations."
)

goal = st.selectbox(
    "Meal goal",
    ["High protein", "Budget friendly", "Healthy", "Quick meals", "Balanced"]
)

diet = st.selectbox(
    "Diet restriction",
    ["None", "Vegetarian", "Vegan", "Gluten Free", "Ketogenic"]
)

exclude_ingredients = st.text_input(
    "Ingredients to avoid",
    placeholder="Example: peanuts, seafood, mushrooms"
)

calories = st.number_input(
    "Target calories per day",
    min_value=1000,
    max_value=4000,
    value=2000
)

budget = st.number_input(
    "Grocery budget ($)",
    min_value=10,
    max_value=200,
    value=50
)

days = st.slider(
    "How many days?",
    min_value=1,
    max_value=5,
    value=3
)

st.divider()

with st.expander("Project Summary for Demo"):
    st.write("**Project Name:** AI Meal Planner & Smart Grocery Assistant")
    st.write("**Problem:** Meal planning takes time and can be hard when people have goals, budgets, or diet restrictions.")
    st.write("**Solution:** This app uses recipe API data and generative AI to create personalized meal plans.")
    st.write("**APIs Used:** Spoonacular API and OpenAI API")
    st.write("**AI Role:** The AI explains the plan, checks the budget, scores the plan, creates a grocery list, and suggests improvements.")
    st.write("**Practical Impact:** Helps users save time, plan meals, and make better food choices.")

if st.button("Generate Meal Plan"):

    if not SPOONACULAR_API_KEY:
        st.error("Missing Spoonacular API key. Check your .env file.")
        st.stop()

    if not OPENAI_API_KEY:
        st.error("Missing OpenAI API key. Check your .env file.")
        st.stop()

    meal_url = "https://api.spoonacular.com/mealplanner/generate"

    meal_params = {
        "apiKey": SPOONACULAR_API_KEY,
        "timeFrame": "week",
        "targetCalories": calories
    }

    if diet != "None":
        meal_params["diet"] = diet

    if exclude_ingredients.strip():
        meal_params["exclude"] = exclude_ingredients

    response = requests.get(meal_url, params=meal_params)

    if response.status_code != 200:
        st.error("Spoonacular API error")
        st.write(response.text)
        st.stop()

    data = response.json()

    st.subheader("Meal Plan")

    recipe_details = []
    all_ingredients = []

    day_count = 0

    for day, meals in data["week"].items():

        if day_count >= days:
            break

        st.write(f"## {day.capitalize()}")

        for meal in meals["meals"]:
            recipe_id = meal["id"]

            info_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"

            info_params = {
                "apiKey": SPOONACULAR_API_KEY
            }

            info_response = requests.get(info_url, params=info_params)

            if info_response.status_code != 200:
                st.warning(f"Could not load details for {meal['title']}")
                continue

            recipe_info = info_response.json()

            title = recipe_info.get("title", "Untitled Recipe")
            ready_time = recipe_info.get("readyInMinutes", "N/A")
            servings = recipe_info.get("servings", "N/A")
            ingredients = recipe_info.get("extendedIngredients", [])
            instructions = recipe_info.get("instructions")

            st.write(f"### {title}")
            st.write(f"Ready in {ready_time} minutes")
            st.write(f"Servings: {servings}")

            st.write("**Ingredients:**")

            ingredient_list = []

            for ingredient in ingredients:
                item = ingredient.get("original", "")
                if item:
                    ingredient_list.append(item)
                    all_ingredients.append(item)
                    st.write(f"- {item}")

            st.write("**Instructions:**")

            if instructions:
                st.markdown(instructions, unsafe_allow_html=True)
            else:
                st.write("No instructions available from API.")

            recipe_details.append({
                "day": day.capitalize(),
                "title": title,
                "ready_time": ready_time,
                "servings": servings,
                "ingredients": ingredient_list
            })

            st.divider()

        day_count += 1

    unique_ingredients = sorted(list(set(all_ingredients)))

    grocery_text = "AI Meal Planner Grocery List\n\n"
    grocery_text += f"Goal: {goal}\n"
    grocery_text += f"Diet: {diet}\n"
    grocery_text += f"Days: {days}\n"
    grocery_text += f"Target Calories: {calories}\n"
    grocery_text += f"Budget: ${budget}\n"
    grocery_text += f"Excluded Ingredients: {exclude_ingredients if exclude_ingredients else 'None'}\n\n"
    grocery_text += "Grocery Items:\n"

    for item in unique_ingredients:
        grocery_text += f"- {item}\n"

    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["Grocery Item"])

    for item in unique_ingredients:
        writer.writerow([item])

    st.subheader("Download Grocery List")

    st.download_button(
        label="Download Grocery List as TXT",
        data=grocery_text,
        file_name="grocery_list.txt",
        mime="text/plain"
    )

    st.download_button(
        label="Download Grocery List as CSV",
        data=csv_buffer.getvalue(),
        file_name="grocery_list.csv",
        mime="text/csv"
    )

    prompt = f"""
You are a smart meal planning assistant.

User preferences:
- Goal: {goal}
- Diet restriction: {diet}
- Excluded ingredients: {exclude_ingredients if exclude_ingredients else "None"}
- Grocery budget: ${budget}
- Days: {days}
- Target calories per day: {calories}

Meals from Spoonacular API:
{recipe_details}

Clean ingredient list:
{unique_ingredients}

Create a clear response with these sections:

1. **Meal Plan Summary**
Give a short overview of the meal plan.

2. **Why It Fits the Goal**
Explain how the meals match the user's selected goal.

3. **Budget Check**
Explain whether the plan seems realistic for the user's grocery budget.
If it may be too expensive, suggest cheaper swaps.

4. **AI Meal Scores**
Give scores from 1 to 10 for:
- Nutrition Score
- Budget Score
- Convenience Score
- Overall Score

Briefly explain each score.

5. **Grocery List**
Group the grocery list into categories like produce, protein, dairy, grains, pantry items, and other.

6. **Swap Suggestions**
Suggest 2 simple meal or ingredient swaps that could improve cost, health, or convenience.

7. **Improvement Tip**
Give one final practical suggestion.

Keep the response organized and easy to read.
"""

    ai_response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    st.subheader("AI Meal Plan Explanation")
    st.markdown(ai_response.output_text)