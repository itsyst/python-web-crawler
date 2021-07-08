from bs4 import BeautifulSoup
import requests
import config

response = requests.get(config.url)
soup = BeautifulSoup(response.text, "html.parser")


questions = soup.select(".question-summary")
# print(type(questions[0]))
# print(questions[0].attrs)
# print(questions[0].["id"])
# print(questions[0].get("id", 0))
# print(questions[0].select(".question-hyperlink"))

for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
