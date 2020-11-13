import requests

webpage_response = requests.get("https://www.thinkful.com/blog/top-30-u-s-cities-to-become-a-web-developer-in/")

webpage = webpage_response.content

print(webpage)