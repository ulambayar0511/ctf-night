import  requests
from  bs4  import  BeautifulSoup

newLink = "/"
for  i  in  range(0, 1010):
	URL = "http://localhost:10000" + newLink
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")
	content = soup.find("div")
	txt = content.text.split()
	newLink = txt[2]
	print(i, content.text)
