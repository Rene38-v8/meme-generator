
from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    # Preberemo podatke iz obrazca
    image_file = request.files["image"]
    top_text = request.form["top_text"]
    bottom_text = request.form["bottom_text"]

    # Odpremo nalozeno sliko
    image = Image.open(image_file).convert("RGB")

    # Pripravimo risanje po sliki
    draw = ImageDraw.Draw(image)

    # Dolocimo velikost pisave
    font_size = max(12, image.width // 12)

    # Nalozimo pisavo
    font = ImageFont.load_default(size=font_size)

    # Funkcija za izpis besedila
    def add_text(text, y):
        text = text.upper()

        # Izracunamo sirino besedila
        box = draw.textbbox((0, 0), text, font=font)
        text_width = box[2] - box[0]

        # Besedilo postavimo na sredino
        x = (image.width - text_width) / 2

        draw.text(
            (x, y),
            text,
            font=font,
            fill="white",
            stroke_width=3,
            stroke_fill="black"
        )

    # Dodamo zgornje besedilo
    add_text(top_text, 10)

    # Dodamo spodnje besedilo
    add_text(bottom_text, image.height - font_size - 20)

    # Shranimo sliko v pomnilnik
    output = BytesIO()
    image.save(output, format="PNG")
    output.seek(0)

    # Vrnemo ustvarjeno sliko
    return send_file(output, mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
