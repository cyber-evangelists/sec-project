import re
from bs4 import BeautifulSoup
html_file="Report.html"
def remove_from_html(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()
      

    soup = BeautifulSoup(html_content, 'html.parser')

   
    for img_tag in soup.find_all('img'):
        img_tag.extract()

    modified_html = soup.prettify()

   
    modified_html = re.sub(r'\b[zZ][aA][pP]\b', '', modified_html)

    with open(html_file, 'w') as file:
        file.write(modified_html)
remove_from_html(html_file)

