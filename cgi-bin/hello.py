#!/usr/bin/env python3

import os
from http.cookies import SimpleCookie
from random import choices

cookies = SimpleCookie(os.getenv("HTTP_COOKIE"))

try:
    visits = int(cookies["visits"].value) + 1
except KeyError:
    visits = 1

cookies["visits"] = str(visits)
cookies["visits"]["max-age"] = 5 # Expire after 5 seconds

print(
    """\
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<body>
<h1>Hello, World!</h1>
</body>
</html>"""
)