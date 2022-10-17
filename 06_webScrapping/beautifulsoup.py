# 1. Request
import requests

page = requests.get("https://raw.githubusercontent.com/fmwestby/IN3110_Group_Sessions/main/06_webScrapping/tags.html")

print(page.status_code)
# 200

print(page.content)
# b'<!DOCTYPE html>\n\n<html>\n    <body>\n        <h1>This is the first heading</h1>\n        <p>And here is a paragraph.</p>\n        <h2>This is my second heading</h2>\n        <p>Here is a table:</p>\n        <table>\n            <tr>\n                <th>Name</th>\n                <th>Course</th> \n                <th>Points</th>\n            </tr>\n            <tr>\n                <td>Peter</td>\n                <td>INF3331</td> \n                <td>50</td>\n            </tr>\n            <tr>\n                <td>George</td>\n                <td>INF4331</td> \n                <td>94</td>\n            </tr>\n        </table>\n        <p>And here are some lists:</p>\n        <p>The first one, is a unordered list.</p>\n        <ul>\n            <li>Coffee</li>\n            <li>Tea</li>\n            <li>Milk</li>\n        </ul>\n        <p>And the second one is ordered.</p>\n        <ol>\n            <li>Coffee</li>\n            <li>Tea</li>\n            <li>Milk</li>\n        </ol>\n        <p>Links are kind of cool! <a href="https://nbviewer.org/github/UiO-IN3110/UiO-IN3110.github.io/blob/HEAD/lectures/07-web-programming/Introduction%20to%20HTML.ipynb">Just look here!</a></p>\n    </body>\n</html>\n\n\n\n\n\n'

# 2. Beautiful Soup
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
# <!DOCTYPE html>
# <html>
#  <body>
#   <h1>
#    This is the first heading
#   </h1>
#   <p>
#    .....

print(soup.find_all('p'))
# [<p>And here is a paragraph.</p>, <p>Here is a table:</p>, <p>And here are some lists:</p>, <p>The first one, is a unordered list.</p>, <p>And the second one is ordered.</p>, <p>Links are kind of cool! <a href="https://nbviewer.org/github/UiO-IN3110/UiO-IN3110.github.io/blob/HEAD/lectures/07-web-programming/Introduction%20to%20HTML.ipynb">Just look here!</a></p>]

