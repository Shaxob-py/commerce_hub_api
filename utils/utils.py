import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

import aiofiles
from jinja2 import Environment, FileSystemLoader

from root.config import settings

env = Environment(loader=FileSystemLoader("templates"))


def generate_code() -> int:
    return randint(100000, 999999)


def send_email(to_email, subject, body):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = settings.EMAIL_USER
    message["To"] = to_email
    part2 = MIMEText(body, "html")
    message.attach(part2)

    with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.login(settings.EMAIL_USER, settings.EMAIL_PASSWORD)
        server.sendmail(settings.EMAIL_USER, to_email, message.as_string())


def verification_send_email(to_email, code: str):
    subject = "Verification email"

    template = env.get_template("verification_email.html")
    context = {
        "code": code
    }

    body = template.render(context)
    send_email(to_email, subject, body)

async def save_photo(image):
    today = datetime.now()

    save_dir = os.path.join("media", "product", today.strftime("%Y"), today.strftime("%m"), today.strftime("%d"))
    os.makedirs(save_dir, exist_ok=True)

    filename = f"tour_{today.strftime('%H%M%S')}.jpg"
    file_path = os.path.join(save_dir, filename)

    async with aiofiles.open(file_path, "wb") as f:
        content = await image.read()
        await f.write(content)

    return os.path.join(
        "/media/tours",
        today.strftime("%Y"),
        today.strftime("%m"),
        today.strftime("%d"),
        filename
    )
