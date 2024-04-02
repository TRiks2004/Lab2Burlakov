from bottle import post, request, HTTPError
import re
from datetime import datetime, timezone

from typing import Iterable


def проверка_все_заполнено(поля: Iterable[str | None]):
    """Проверяет, что все поля заполнены"""
    for поле in поля:
        if поле == "":
            raise HTTPError(status=401, body="Заполните все поля.")


def проверка_вопрос(вопрос: str):
    """Проверяет длину вопроса и наличие символов"""
    if len(вопрос) < 10:
        raise HTTPError(
            status=401, body="Вопрос должен быть не менее 10 символов."
        )
    elif len(вопрос) > 100:
        raise HTTPError(
            status=401, body="Вопрос должен быть не более 100 символов."
        )


def проверка_имя(имя: str):
    """Проверяет имя на валидность и длину"""
    шаблон_имя = re.compile("^[a-zA-Z0-9_]+$")
    if not шаблон_имя.match(имя):
        raise HTTPError(
            status=401, body="Невалидное имя. Введите валидное имя."
        )

    if len(имя) < 3:
        raise HTTPError(
            status=401, body="Имя должно быть не менее 3 символов."
        )

    if len(имя) > 20:
        raise HTTPError(
            status=401, body="Имя должно быть не более 20 символов."
        )


def проверка_email(email: str):
    """Проверяет email на валидность"""

    if len(email) > 50:
        raise HTTPError(
            status=401, body="Невалидный email. Введите валидный email."
        )

    pattern_email = re.compile(
        r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,10}$"
    )
    if not pattern_email.match(email):
        print(pattern_email.match(email))
        raise HTTPError(
            status=401, body="Невалидный email. Введите валидный email."
        )

    if len(email.split("@")[1].split(".")) > 3:
        raise HTTPError(
            status=401, body="Невалидный email. Введите валидный email. "
        )


@post("/home")
def форма_покуп():
    вопрос = request.forms.get("QUEST")
    имя = request.forms.get("NAME")
    email = request.forms.get("ADRESS")

    проверка_все_заполнено((вопрос, имя, email))
    проверка_вопрос(вопрос)
    проверка_имя(имя)
    проверка_email(email)

    return f"Спасибо {имя}! Ответ будет отправлен на email {email} Дата доступа: {datetime.now(timezone.utc)}"
