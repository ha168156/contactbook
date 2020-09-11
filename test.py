import urllib.request as req
url="http://tw.class.uschoolnet.com/class/?csid=css000000249169&id=model16&cl=1565107501-5427-5178"
request=req.Request(url,headers={
     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"})
with req.urlopen (request) as response:
     data=response.read().decode("utf-8")
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("td",class_="contacting_book_list_exam",width="97%")
for title in titles:	print(title.string)
