import bs4
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
with urllib.request.urlopen("http://www.bbc.com/news")as response:
   # print(response.read())
    #text_file = open("Output.html", "w")
    x=str(response.read())
    #text_file.write(x)

    #text_file.close()
    soup=bs4.BeautifulSoup(x,"html.parser")
    title_collection=set()
    for y in soup.find_all("h3"):
        title_collection.add(y.string)
        #print(y.string)
    title_collection_list = list(title_collection)
    title_collection_list.sort()
    print("\n".join(title_collection_list))