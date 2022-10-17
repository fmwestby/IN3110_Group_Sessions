# 1. Request
import requests

page = requests.get("https://raw.githubusercontent.com/fmwestby/IN3110_Group_Sessions/main/06_webScrapping/tags.html")

print(page.status_code)
# 200

print(page.content)