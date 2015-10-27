import string
import cgi
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.+[\S]+$]")

def valid_name(username):
    return USER_RE.match(username)

def valid_passwd(password):
    return PASS_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

def match(password, verification):
    if password == verification:
        return False
