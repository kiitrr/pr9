import re

def parse_email(email):
    """Разбирает email на имя пользователя и доменное имя."""
    # Регулярное выражение для проверки и разбора email
    pattern = r'^(?P<username>[a-zA-Z][\w.-]*)@(?P<domain>[\w.-]+\.\w+)$'
    match = re.match(pattern, email)
