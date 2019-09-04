import sys, os, random, csv, shutil, time
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

class Human:
    def __init__(self, full_name, gender, date_of_birth):
        Human.full_name = full_name
        Human.full_name_safe = full_name.replace(" ", "_") + "_" + str(time.time())
        Human.full_name_devanagri = transliterate(Human.full_name.lower(), sanscript.ITRANS, sanscript.DEVANAGARI)
        Human.gender = gender
        Human.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").strftime("%d/%m/%Y")
        Human.aadhaar_number = "  ".join([str(random.randint(1000, 9999)) for x in range(3)])
        # Human.address = "Piccadilly 4, Royal Palms Estate, Aarey Colony, Goregaon, Mumbai 400065"
        # Human.address_devanagri = "पिकाडिली 4, रॉयल पाम्स एस्टेट, आरे कॉलोनी, गोरेगांव, मुंबई 400065"

class AadhaarCard(Human):
    def __init__(self, font_path, devanagari_font_path, aadhaar_number_font_path, male_front_template_path, female_front_template_path, back_template_path, front_save_path, back_save_path, photo_path):
        self.font_size = 40
        self.aadhaar_number_font_size = 58
        self.black = (0, 0, 0)

        self.photo_size = (260, 300)
        self.photo_location = (66, 171)
        self.full_name_devanagri_location = (364, 167)
        self.full_name_location = (364, 207)
        self.date_of_birth_location = (612, 251)
        self.aadhaar_number_location_front = (422, 630)
        self.aadhaar_number_location_back = (416, 630)

        self.font_path = font_path
        self.devanagari_font_path = devanagari_font_path
        self.aadhaar_number_font_path = aadhaar_number_font_path
        self.male_front_template_path = male_front_template_path
        self.female_front_template_path = female_front_template_path
        self.back_template_path = back_template_path
        self.front_save_path = front_save_path
        self.back_save_path = back_save_path
        self.photo_path = photo_path

    def create(self):
        self.image_front = Image.open(self.male_front_template_path) if Human.gender == "Male" else Image.open(self.female_front_template_path)
        self.image_back = Image.open(self.back_template_path)
        draw_front = ImageDraw.Draw(self.image_front)
        draw_back = ImageDraw.Draw(self.image_back)

        photo = Image.open(self.photo_path)
        photo = photo.resize(self.photo_size)
        photo.save(self.photo_path, "PNG", optimize=True)
        self.image_front.paste(photo, self.photo_location)

        draw_front.text(
            xy=self.full_name_devanagri_location,
            text=Human.full_name_devanagri,
            fill=self.black,
            font=ImageFont.truetype(self.devanagari_font_path, self.font_size),
            # language="hi"
        )

        draw_front.text(
            xy=self.full_name_location,
            text=Human.full_name,
            fill=self.black,
            font=ImageFont.truetype(self.font_path, self.font_size)
        )

        draw_front.text(
            xy=self.date_of_birth_location,
            text=Human.date_of_birth,
            fill=self.black,
            font=ImageFont.truetype(self.font_path, self.font_size)
        )

        draw_front.text(
            xy=self.aadhaar_number_location_front,
            text=Human.aadhaar_number,
            fill=self.black,
            font=ImageFont.truetype(self.aadhaar_number_font_path, self.aadhaar_number_font_size)
        )

        draw_back.text(
            xy=self.aadhaar_number_location_back,
            text=Human.aadhaar_number,
            fill=self.black,
            font=ImageFont.truetype(self.aadhaar_number_font_path, self.aadhaar_number_font_size)
        )

    def save(self):
        self.image_front.save(self.front_save_path)
        self.image_back.save(self.back_save_path)
