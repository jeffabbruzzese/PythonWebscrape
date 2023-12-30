import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('https://oxylabs.io/blog')
results = []
otherResults = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

blog_posts = soup.find_all(attrs='css-16nzj3b e1qkxeay1')
for post in blog_posts:
    title = post.find(attrs='css-rmqaiq e1dscegp1').text
    date = post.find(attrs='css-weczbu e1ymydvc2').text
    if title and date and title not in results:
        results.append(title)
        otherResults.append(date)
df = pd.DataFrame({'Blog Post Titles': results,
                   'Dates': otherResults})
df.to_csv('blogPosts.csv', index=False, encoding='utf-8')