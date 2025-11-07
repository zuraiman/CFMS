from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# +-----------------------------------------------------------------------------+
# | Task 1: User Registration Form                                              |
# +-----------------------------------------------------------------------------+
# | Create a user registration page using HTML forms. The page should include   |
# | fields for username and password. Implement the GET method to display the   |
# | form and the POST method to submit the form data to the server. On the      |
# | server side (in Flask), simply print the received data to the console.      |
# +-----------------------------------------------------------------------------+

@app.route('/', methods=['GET', 'POST'])
def register():
    """
    Handles user registration.
    GET: Displays the registration form (Task 1).
    POST: Processes the form data (Task 2).
    """
    if request.method == 'POST':
        # Retrieve data from the submitted form
        username = request.form.get('username')
        password = request.form.get('password')

        # Task 1: Print the received data to the console
        print(f"--- Registration Data Submitted ---")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"---------------------------------")

        # Task 2: Redirect to the welcome page with the username
        return redirect(url_for('welcome', username=username))

    # Task 1: Display the registration form on GET request
    return render_template('register.html')

# +-----------------------------------------------------------------------------+
# | Task 2: Displaying a Welcome Message                                        |
# +-----------------------------------------------------------------------------+
# | After the user submits the registration form, display a welcome message     |
# | using a new HTML template. This message should include the username         |
# | submitted from the form. This task requires handling POST data in Flask and |
# | sending this data to a template for rendering.                              |
# +-----------------------------------------------------------------------------+

@app.route('/welcome/<username>')
def welcome(username):
    """
    Displays a welcome message to the registered user.
    """
    return render_template('welcome.html', username=username)

# +-----------------------------------------------------------------------------+
# | Task 3: Building an Interactive Feedback Form                               |
# +-----------------------------------------------------------------------------+
# | Create an interactive feedback form accessible from the welcome page. This  |
# | form should allow users to:                                                 |
# |                       Submit a rating on a scale of 1 to 5.                 |
# |                       Provide written feedback in a text box.               |
# +-----------------------------------------------------------------------------+

# --- Task 3 & 4: Interactive Feedback Form and Enhanced Feedback Display ---
@app.route('/feedback/<username>', methods=['GET', 'POST'])
def feedback(username):
    """
    Handles the feedback form.
    GET: Displays the feedback form (Task 3).
    POST: Processes the feedback and displays the thank you page with visual cues (Task 4).
    """
    if request.method == 'POST':
        # Retrieve data from the submitted form
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        
        # Convert rating to an integer for comparison
        try:
            rating = int(rating)
        except ValueError:
            # Handle case where rating might not be an integer
            rating = 0 

# +------------------------------------------------------------------------------+
# | Task 4: Enhanced User Feedback Form with Visual Cues                         |
# +------------------------------------------------------------------------------+
# | Upon submission of feedback using POST, display a thank you message along    |
# | with the feedback and rating provided by the user. Additionally, incorporate |
# | visual cues:                                                                 |
# |              Display a positive smiley image if the rating is 4 or 5.        |
# |              Show a neutral smiley for a rating of 3.                        |
# |              Use a negative smiley image for ratings below 3.                |
# |                                                                              |
# | Ensure that the entire pages are styled with a consistent background color   |
# | and font using CSS. It is important to maintain uniformity in the size and   |
# | placement of the smiley images across all pages. Utilize the provided CSS    |
# | file and images to achieve this styling.                                     |
# +------------------------------------------------------------------------------+

        # Task 4: Determine the smiley image based on the rating
        smiley_image = ''
        if rating >= 4:
            # Positive smiley for 4 or 5
            smiley_image = 'positive.png' 
        elif rating == 3:
            # Neutral smiley for 3
            smiley_image = 'neutral.png'
        else: # rating < 3
            # Negative smiley for ratings below 3
            smiley_image = 'negative.png' 
            
        # Task 4: Display thank you message with feedback, rating, and visual cue
        return render_template('thank_you.html',
                               username=username,
                               rating=rating, 
                               comment=comment, 
                               smiley=smiley_image)

    # Task 3: Display the interactive feedback form on GET request
    return render_template('feedback.html', username=username)

# About Us page
@app.route('/about/<username>')
def about(username):
    """
    Displays the About page to the registered user.
    """
    return render_template('about.html', username=username)

# Run the application if this script is executed directly--------------------------------------

if __name__ == '__main__':
    # For automatic reloading during development
    app.run(host='0.0.0.0', port=5000, debug=True) 

# Note: In a production environment, debug should be set to False.
# --------------------------------------------------------------------------------------------
