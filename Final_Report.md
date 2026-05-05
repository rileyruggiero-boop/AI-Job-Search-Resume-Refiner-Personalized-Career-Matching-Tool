
AI Meal Planner & Smart Grocery Assistant
GitHub Repository:
 https://github.com/rileyruggiero-boop/AI-Meal-Planner

1. Introduction
Meal planning is a common problem for many people. It can be time-consuming and difficult, especially when trying to balance health goals, budget constraints, and dietary restrictions. Many existing tools either provide generic meal suggestions or require manual searching through recipes, which does not efficiently solve the problem.
This project, AI Meal Planner & Smart Grocery Assistant, was created to address this issue by combining real-world recipe data with generative AI. The goal of the project is to allow users to quickly generate personalized meal plans based on their preferences, while also receiving intelligent recommendations and a structured grocery list.
The application provides a working minimum viable product (MVP) that integrates external APIs and generative AI into a single, functional system that solves a real-world problem.

2. Problem Statement
Planning meals manually presents several challenges:
It takes time to find recipes that match goals (e.g., high protein or healthy)
Users must manually check ingredients and instructions
Budget considerations are often ignored
People with dietary restrictions have limited options
Grocery list creation is repetitive and inefficient
The objective of this project is to create a system that automates these tasks and enhances them using generative AI.

3. Solution Overview
The solution is a web-based application built using Streamlit that allows users to generate personalized meal plans.
Users can input:
Meal goal (e.g., high protein, healthy)
Daily calorie target
Grocery budget
Number of days for the plan
Dietary restrictions (e.g., vegetarian, vegan)
Ingredients to avoid
The system then:
Uses the Spoonacular API to retrieve real recipe data
Extracts ingredients, instructions, and nutritional information
Processes the data into a structured format
Sends the data to the OpenAI API
Generates a detailed AI-powered explanation, scoring, and recommendations
Produces a downloadable grocery list (TXT and CSV)
This creates a complete end-to-end workflow from user input to final output.

4. Technologies Used
This project uses the following tools and technologies:
Python – main programming language
Streamlit – web application framework
Spoonacular API – provides recipe and nutrition data
OpenAI API – generates explanations, scoring, and recommendations
Requests library – handles API calls
python-dotenv – manages environment variables securely
Git & GitHub – version control and project hosting

5. Generative AI Integration
Generative AI is a core component of this project.
The OpenAI API is used to:
Generate a structured meal plan summary
Explain why the plan fits the user’s goal
Evaluate whether the plan fits the user’s budget
Create a categorized grocery list
Provide improvement suggestions
Assign scores for:
Nutrition
Budget
Convenience
Overall quality
This demonstrates clear use of generative AI beyond simple text generation. The AI processes structured data from an external API and transforms it into meaningful, user-friendly insights.

6. System Workflow
The system operates in the following steps:
User inputs preferences into the Streamlit interface
The app sends a request to the Spoonacular API
The API returns a weekly meal plan
The app retrieves detailed recipe information for each meal
Ingredients and instructions are displayed to the user
A combined ingredient list is generated and cleaned
The data is sent to the OpenAI API
The AI generates a structured explanation and recommendations
The user can download a grocery list
This workflow demonstrates a complete and functional MVP.

7. Features
Key features of the application include:
Multi-day meal planning
Dietary restriction filtering
Ingredient exclusion
Budget input and evaluation
Real recipe ingredients and instructions
AI-generated explanations and recommendations
AI scoring system
Downloadable grocery lists (TXT and CSV)
Clean and interactive user interface
These features contribute to a strong and practical application.

8. Challenges and Limitations
Several challenges were encountered during development:
API Limitations
The Spoonacular API sometimes restricts access or limits the number of requests, which required careful handling of API calls.
Data Inconsistency
Some recipes did not include full instructions or consistent ingredient formats, requiring fallback handling.
Formatting Issues
Combining data from APIs and ensuring clean output required multiple iterations.
Debugging
Errors such as indentation issues, API errors, and environment setup problems were common and required troubleshooting.

9. Results
The final application successfully meets the project objectives:
The app runs correctly using Streamlit
It integrates two APIs (Spoonacular and OpenAI)
It produces meaningful outputs based on user inputs
It provides a complete meal planning workflow
It demonstrates clear use of generative AI
The application is functional, practical, and easy to use.

10. Conclusion
The AI Meal Planner & Smart Grocery Assistant demonstrates how generative AI can be combined with real-world data to solve everyday problems.
By integrating APIs, user input, and AI-generated output, the project provides a complete and useful application. It highlights the potential of generative AI in building tools that improve efficiency, decision-making, and user experience.
Overall, the project meets all requirements for a working MVP and showcases practical implementation of generative AI concepts.

