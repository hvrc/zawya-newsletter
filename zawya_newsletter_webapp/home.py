from zawya_newsletter_webapp import app
from zawya_newsletter_webapp.scripts.html_parser import *
from flask import render_template, request

root_dir = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        posts = [post[1] for post in request.form.items()]
        links = posts[0].splitlines()
        template_name = posts[1]
        parser = Parser(root_dir, links, template_name)
        parser.generate_elements_dict()
        parser.output_html_file()

        return render_template(
            "home.html",
            parsed=True,
        )

    return render_template(
        "home.html",
        parsed=False
    )

@app.route("/template", methods=["POST", "GET"])
def template():
    return render_template(
        "template.html",
    )

@app.route("/output", methods=["POST", "GET"])
def output():
    return render_template(
        "output.html",
    )
