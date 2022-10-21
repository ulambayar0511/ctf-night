from  bs4  import  BeautifulSoup
import  requests
import  hashlib
arr=[]
for  i  in  range(0, 100):
	hash = str(i)
	result = hashlib.md5(hash.encode('utf-8'))
	arr.append(result.hexdigest())

def  find(num):
	for  i  in  range(0, 100):
		if(arr[i] == num):
			return  i

def  calc(num1, num2, c):
	if  c == "+":
		return  num1 + num2
	if  c == "-":
		return  num1 - num2
	if  c == "*":
		return  num1 * num2
	if  c == "/":
		return  num1 / num2

URL = "http://localhost:8000"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
numbers = soup.find("form")
txt = numbers.text.split()
sum = calc(find(txt[6][1:]), find(txt[8][:-1]), txt[7])
sum1 = calc(find(txt[0]), find(txt[2]), txt[1])
sum2 = calc(sum1, find(txt[4]), txt[3])
total = calc(sum2, sum, txt[5])
url = 'http://localhost:8000/sum'
mathResult = {'sum': total}
res = requests.post(url, data = mathResult)
print(res.text)
