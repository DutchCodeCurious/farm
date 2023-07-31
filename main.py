# Import what we need from flask
from flask import Flask

# Create a Flask app inside `app`
app = Flask(__name__)


# Assign a function to be called when the path `/` is requested
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Under Construction</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }

            .container {
                text-align: center;
            }

            h1 {
                color: #333;
            }

            p {
                color: #777;
            }

            img {
                max-width: 100%;
            }
        </style>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script>
            $(document).ready(function() {
                // Animation for the "Under Construction" text
                const animateText = function() {
                    $('h1').animate({ opacity: 0.2 }, 1000, function() {
                        $(this).animate({ opacity: 1 }, 1000, animateText);
                    });
                };

                animateText();
            });
        </script>
    </head>
    <body>
        <div class="container">
            <h1>We're Under Construction</h1>
            <p>We are currently working on something awesome. Please check back later!</p>
        </div>
    </body>
    </html>
    '''


@app.route('/cow')
def cow():
    return 'MOoooOo!, this is the test file'
