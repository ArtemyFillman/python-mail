import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import time

def read_email_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def send_email(subject, message, to_email, smtp_server, smtp_port, smtp_user, smtp_password, template_path):
    # Создаем объект MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject

    # Читаем содержимое HTML-шаблона
    email_template = read_email_template(template_path)

    # Заменяем метку {{MESSAGE}} в шаблоне на фактическое сообщение
    email_body = email_template.replace('{{MESSAGE}}', message)

    # Добавляем HTML-часть сообщения
    msg.attach(MIMEText(email_body, 'html'))

    # Подключаемся к SMTP-серверу
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Входим в учетную запись
        server.login(smtp_user, smtp_password)

        # Отправляем сообщение
        sleep_seconds = random.randint(1, 10)
        print(f'Отправляем сообщение {to_email} через {sleep_seconds} секунд...')
        time.sleep(sleep_seconds)
        server.sendmail(smtp_user, to_email, msg.as_string())

# Чтение списка контактов из файла
with open('contacts.txt', 'r') as file:
    contacts = file.read().splitlines()

# Настройки SMTP-сервера
smtp_server = 'smtp.timeweb.ru'
smtp_port = 2525  # Порт для шифрованного соединения (TLS)
smtp_user = 'info@x-fighting.ru'
smtp_password = 'infoxfighting241005'

# Путь к файлу с HTML-шаблоном
template_path = 'email_template.html'

# Отправка сообщений
for contact in contacts:
    subject = 'ПИСЬМО ДЛЯ БОЙЦА!'
    message = 'Привет боец! На связи молодой промоушен X FIGHTING CHEMPIONSHIP! Мы давно наблюдаем за тобой и за твоими боями! И мы приглашаем вас поучаствовать в нашем турнире, который пройдёт 4 февраля, где у вас будет шанс побороться за главный приз - деньги! Если вас данное предложение заинтересовало, то дайте обратную связь и я расскажу вам поподробнее о предстоящем мероприятии! '
    send_email(subject, message, contact, smtp_server, smtp_port, smtp_user, smtp_password, template_path)
