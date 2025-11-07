# CFMS
My simple assignment from LITHAN for a Flask Web Development with Enhanced User Feedback Experience and I called it "Customer Feedback Management System (CFMS)".

🎯 Project Overview

CFMS is a web application developed using the Flask framework as part of the LITHAN "Flask Web Development with Enhanced User Feedback Experience" assignment.

The primary goal of this project is to create a dynamic and user-friendly platform for gathering customer insights. It demonstrates key Flask functionalities, including handling different HTTP methods (GET and POST), rendering dynamic data using Jinja templates, and implementing conditional logic to provide an Enhanced User Feedback Experience through visual cues.

✨ Features Implemented

This system successfully implements all key functionalities required by the assignment, focusing on a secure and engaging user flow:

1. User Registration & Handling (Task 1 & 2)

- Registration Form: Provides an HTML form for users to register with a username and password.
- Method Handling: Correctly handles GET for displaying the form and POST for submitting data.
- Data Processing: On submission, the server processes the data (and prints it to the console).
- Personalized Welcome: Redirects the user to a new page displaying a personalized welcome message that includes their submitted username.

2. Interactive Feedback Mechanism (Task 3 & 4)

- Feedback Form: Allows users to submit a numeric rating (1 to 5) and written feedback.
- Dynamic Confirmation: Displays a "Thank You" message alongside the exact rating and feedback submitted by the user.
- Visual Cues (Enhanced Feedback): Incorporates conditional rendering of graphical elements based on the rating:
    - Rating 4 or 5: Displays a Positive Smiley.
    - Rating 3: Displays a Neutral Smiley.
    - Rating Below 3: Displays a Negative Smiley.

3. Consistent Styling

- The entire application is styled using external CSS to ensure a consistent background color, font, and uniform placement/size of the smiley images across all pages, maximizing user experience and visual coherence.

🛠️ Technology Stack

- Backend Framework: Python Flask
- Frontend: HTML5, CSS3 (External Stylesheet)
- Templating Engine: Jinja2 (Built into Flask)
- Environment Management: venv (Python Virtual Environment)

📦 Installation and Setup

Follow these instructions to set up and run the CFMS application locally.

Prerequisites
- Python 3.8+
- pip (Python package installer)


Step 1: Clone the Repository

> git clone [https://github.com/your-username/cfms-project.git](https://github.com/your-username/cfms-project.git)
> cd cfms-project


Step 2: Create and Activate Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.

# Create environment
> python3 -m venv venv

# Activate the environment (Linux/macOS)
> source venv/bin/activate

# Activate the environment (Windows)
> .\venv\Scripts\activate


Step 3: Install Dependencies
Install Flask using the requirements.txt file (assuming it contains Flask).

> pip install -r requirements.txt


Step 4: Run the Application
Execute the main application file.

> export FLASK_APP=app.py
> export FLASK_ENV=development # Optional, for debugging
> flask run


The application will now be running on your local machine, typically accessible at:
👉 http://127.0.0.1:5000/register

🚀 Usage Walkthrough

1. Registration: Navigate to /register. Fill in the username and password and submit the form (POST handled).
2. Welcome: You are redirected to /welcome/<username>, displaying the personalized welcome message.
3. Feedback Form: From the welcome page, access the interactive feedback form at /feedback.
4. Submission: Input a rating (1-5) and written comments, and submit (POST handled).
5. Confirmation: The system displays the confirmation page (/thank_you) showing your submitted data along with the dynamically rendered visual cue (smiley image) corresponding to the rating.
