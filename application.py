from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a string
    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """ This function displays the application form for the user to fill out and submit """

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application():
    """ This function processes the user's input """

    # get the user's input from each of these fields
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    position = request.form.get("position")

    return render_template("application-response.html", first_name=firstname, last_name=lastname, salary=salary, position=position)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
