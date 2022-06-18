from zawya_newsletter_webapp import app
from zawya_newsletter_webapp.scripts.html_parser import *
from flask import render_template, request

root_dir = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        posts = [post[1] for post in request.form.items()]
        links = posts[0].splitlines()

        parser = Parser(links, root_dir)
        parser.generate_elements_dict()
        parser.output_html_file()

        return render_template(
            "home.html",
        )

    return render_template(
        "home.html",
    )
