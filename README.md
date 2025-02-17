# learn-flask

find env name with "conda info", then:
"conda env export -n learn_flask > env.yml"
but make sure current directory is the local repo

change flask to run in dev mode for live changes:
https://stackoverflow.com/questions/16344756/auto-reloading-python-flask-app-upon-code-changes/40150705#40150705

Explanation of Key Concepts:

- What is Flask and why is it used?
  Flask is a lightweight and flexible web framework for Python. It's designed to be
  easy to use and allows developers to quickly build web applications, APIs, and more.
  It's used because it provides the essential tools and features needed for web development
  without imposing too much structure or complexity.

- Explain the app instance and its purpose.
  The app instance (app = Flask(**name**)) is the core of your Flask application.
  It represents the WSGI (Web Server Gateway Interface) application, which is the
  interface between your Python code and the web server. It's used to configure
  the application, define routes, and handle requests.

- Explain routing and how it works in Flask.
  Routing is the process of mapping URLs to specific functions in your application.
  In Flask, this is done using the @app.route decorator. When a user visits a URL
  that matches a route, the corresponding function is executed. Routes can also
  include variable parts, allowing you to create dynamic URLs.

- Explain the significance of debug mode.
  Debug mode (debug=True) is a development feature that provides helpful error messages
  and automatically reloads the server when you make changes to the code. This makes
  it easier to debug and develop your application. It should NOT be used in production
  environments, as it can expose sensitive information.

Best Practices and Common Pitfalls to Avoid:

- Suggest a good project structure for larger Flask apps.
  For larger Flask apps, it's recommended to use a modular project structure. This
  typically involves organizing your code into separate modules for different parts
  of the application (e.g., models, views, forms). A common structure is:

  myproject/
  ├── app.py # Main application file
  ├── config.py # Configuration settings
  ├── models.py # Database models
  ├── views/ # Route handlers (views)
  │ ├── **init**.py
  │ ├── home.py
  │ └── user.py
  ├── templates/ # HTML templates
  │ ├── index.html
  │ └── form.html
  ├── static/ # Static files (CSS, JavaScript, images)
  │ ├── style.css
  │ └── script.js
  └── requirements.txt # Dependencies

- Explain how to handle errors and exceptions gracefully.
  Use try-except blocks to catch potential errors and exceptions. You can also use
  Flask's error handling features to define custom error pages for different HTTP
  status codes. For example:

  @app.errorhandler(404)
  def page_not_found(error):
  return render_template('404.html'), 404

* Recommend ways to organize routes and views.
  For larger applications, it's best to organize routes and views into separate modules
  or blueprints. Blueprints allow you to group related routes and views together,
  making your code more modular and maintainable.

* Advise on secure coding practices in Flask.
  - Always sanitize user input to prevent cross-site scripting (XSS) attacks.
  - Use parameterized queries to prevent SQL injection attacks.
  - Protect against cross-site request forgery (CSRF) attacks by using a CSRF token.
  - Use HTTPS to encrypt communication between the client and server.
  - Store passwords securely using a strong hashing algorithm.
  - Avoid storing sensitive information in cookies or local storage.
  - Keep your Flask and its dependencies up to date to patch security vulnerabilities.

Setup and Execution Instructions:

Setup and Execution Instructions:

1. Install Flask and any dependencies:
   ```bash
   pip install Flask
   # If you want to use Jinja2 templates, it's usually included with Flask, but you can install it separately:
   # pip install Jinja2
   ```
