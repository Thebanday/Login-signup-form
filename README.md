# Login-signup-form
An application to enable signup and login for different types of users. On login redirect users to their respective dashboards.



To run the a code, you will need to have Python and the Flask library installed on your computer. You will also need to create template files for the signup, login, patient dashboard, and doctor dashboard pages.

First, open a terminal or command prompt and navigate to the directory where you have saved the above code.

Run the following command to start the Flask development server:

Copy code
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
The server should now be running on your localhost at port 5000. You can access the signup page by navigating to http://localhost:5000/signup in your web browser.

Fill out the signup form and submit it. The user information will be stored in the users list and you will be redirected to the login page.

On the login page, enter the username and password you used to sign up and submit the form. If the information is correct, you will be redirected to the appropriate dashboard page.

To log out, you can simply close the browser or navigate to http://localhost:5000/logout.

Note: You will need to create template files for the signup, login, patient dashboard, and doctor dashboard pages in order for the code to work properly. These templates should include the appropriate HTML and Flask template tags to display the user information.
