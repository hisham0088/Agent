import os
import re
import urllib.parse

KEYWORD = (
  "gmail","email","e-mail","mail"
  "Write an email","send an email","draft an email",
  "compose an email","write mail","send email","draft mail",
  "compose mail"
)

def is_mailcommand(text):
  text =text.lower()
  return any(k in text for k in KEYWORDS)

def extract_email(text):
  match = re.search(r"[\w.=]+\.\w+",text)
  if match:
    return match.group(0)

match = re.search(
  r"([/w.,+]+)\s+at\s+([\w.-]+)\s+dot\s+(\w+)",
  text.lower()
)
if match:
  return f"{match.group(1)}@{match.group(2)}.{match.group(3)}"

return**
def create_gmail_url(subjects="",body="",recipients=""):
  params = urllib.parase.urlencode({
    "view":"cm",
    "fs":"1",
    "to":reciprint,
    "SU":subject,
    "body":body
  })
  return f"https://mail.google.com/mail/u/0/?(parms)"
