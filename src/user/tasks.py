import asyncio

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from celery import Celery
from celery import shared_task

""" Настройка Celery"""
celery = Celery('tasks', broker='redis://localhost:6379/0')



""" Настройка отправления почты"""

# валидация почты
class EmailSchema(BaseModel):
    email: EmailStr


# Настройки электронной почты
conf = ConnectionConfig(
    MAIL_USERNAME='ystas2019@mail.ru',
    MAIL_PASSWORD='7zPkj6PxU7NUjngp6fhV',
    MAIL_FROM="ystas2019@mail.ru",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.mail.ru",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


# Определяем функцию для отправки письма
@shared_task
def send_email(user_email: EmailStr):
    message = MessageSchema(
        subject="Регистрация",
        recipients=[user_email],
        body="Вы зарегистрированы",
        subtype=MessageType.plain
    )

    fm = FastMail(conf)

    async def send_message_async():
        await fm.send_message(message)

    asyncio.run(send_message_async())

