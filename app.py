from flask import Flask, redirect, url_for, render_template
# render_templage grabs html from render page
# Folder names must be template
app = Flask(__name__)
@app.route("/")  # Default first Page
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()