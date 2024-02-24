from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired
from wtforms import TextAreaField, SubmitField
from cryptography.fernet import Fernet
import rsa
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import b64decode

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"


class EncryptionForm(FlaskForm):
    issue = TextAreaField(
        "Issue",
        render_kw={"rows": 10, "cols": 50},
        validators=[DataRequired()],
        default="Team Name : \nFile Name : \nBug Description : \nSolution : ",
    )


@app.route("/", methods=["GET", "POST"])
def index():
    form = EncryptionForm()
    if form.is_submitted():
        result = request.form
        print("Form is submitted\n", result["issue"])

        message = result["issue"]
        key = Fernet.generate_key()
        fernet = Fernet(key)

        encMessage = fernet.encrypt(message.encode())

        message = key

        public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCxMAP6Wcyz832JtlOH0Iy0U6+gHaHtMKO72JPzzDnrbTu5186iqDO32B2E2+vDcuyJ2u2KhlsGW/zLicB85g5V9d8XjJRILLDBusKkn5QJTtNg5zSnCvRdzNIVwWGOuzvtR7oRaS8NpMQePQ1U7BKFP/Goad2PzAu5RtdH2rDUkQIDAQAB"
        public_key = b64decode(public_key)
        public_key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_key = cipher.encrypt(message)
        print("\n\n")
        print(encrypted_key)
        print("\n\n")
        print(encMessage)

        output = [encrypted_key, encMessage]
        return render_template("result.html", output=output)
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
