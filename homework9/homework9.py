import re

def parse_email(email):
    """Разбирает email на имя пользователя и доменное имя."""
    
    pattern = r'^(?P<username>[a-zA-Z][\w.-]*)@(?P<domain>[\w.-]+\.\w+)$'
    match = re.match(pattern, email)

    if match:
        username = match.group('username')
        domain = match.group('domain')
        return username, domain
    else:
        return None, None

