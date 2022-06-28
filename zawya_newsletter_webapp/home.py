from zawya_newsletter_webapp import app
from zawya_newsletter_webapp.scripts.html_parser import *
from flask import render_template, request

root_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = root_dir + "/templates/"
template_name = "template.html"
target_path = target_dir + template_name
output_path = target_dir + "output.html"
parsed = False

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":

        if os.path.exists(target_path):
            os.remove(target_path)
            print(target_path + " deleted")

        if os.path.exists(output_path):
            os.remove(output_path)
            print(output_path + " deleted")

        posts = [post[1] for post in request.form.items()]
        links = posts[0].splitlines()
        template = request.files["template"]
        template.save(target_path)
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
