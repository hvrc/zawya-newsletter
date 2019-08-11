from fakeboy import app
from fakeboy.scripts.main import *
from flask import render_template, request

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        posts = [post[1] for post in request.form.items()]

        human = Human(
            full_name=posts[0],
            gender=posts[1],
            date_of_birth=posts[2],
        )

        photo = request.files["photo"]
        TARGET_DIR = os.path.join(ROOT_DIR, "/static/database/photos/")
        photo_path = os.path.join(TARGET_DIR, human.full_name_safe + "_photo.png")
        if not os.path.isdir(TARGET_DIR) os.mkdir(TARGET_DIR)
        photo.save(photo_path)

        card = AadhaarCard(
            font_path=os.path.join(ROOT_DIR, "/static/fonts/calibri_bold.ttf"),
            devanagari_font_path=os.path.join(ROOT_DIR, "/static/fonts/adobe_devanagari_bold.otf"),
            aadhaar_number_font_path=os.path.join(ROOT_DIR, "/static/fonts/open_sans_bold.ttf"),
            male_front_template_path=os.path.join(ROOT_DIR, "/static/templates/male_front_template.png"),
            female_front_template_path=os.path.join(ROOT_DIR, "/static/templates/female_front_template.png"),
            back_template_path=os.path.join(ROOT_DIR, "/static/templates/back_template.png"),
            front_save_path=os.path.join(ROOT_DIR, "/static/database/ids/" + human.full_name_safe + "_front.png"),
            back_save_path=os.path.join(ROOT_DIR, "/static/database/ids/" + human.full_name_safe + "_back.png"),
            photo_path=photo_path,
        )

        card.create()
        card.save()

        return render_template(
            "home.html",
            full_name_safe=human.full_name_safe,
        )

    return render_template(
        "home.html",
        full_name_safe="",
    )
