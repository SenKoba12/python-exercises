######BEAUTIFUL SOUP########
########REQUESTS############

from bs4 import BeautifulSoup

with open("scrape.html","r") as f:
    doc = BeautifulSoup(f, "html.parser")

#to print the whole html file:
    #print(doc.prettify())

#tag = doc.title - get the title of the html file
        #also includes for other tags
#print(tag) - includes the tag
#print(tag.string) - only the string

#modify the tag:
    #tag.string = "hello"
    #print(tag)
    #Note: doing this will change the name of the tag from the html itself

#find tags:
    #tags = doc.find_all("p") - find() only looks for the first instance of the tag
    #print(tags)

#find nested tags
    #tags = doc.find_all("p")
    #print(tags.find_all("b")) - looks for an instance of "p" tags where there are "b" tags



#______FOR REQUESTS________#
#page = requests.get(url)
#print(page)

#html_text = BeautifulSoup(page.text,'html')
#print(html_text.prettify())
#tag = BeautifulSoup(page.text, 'title')
#print(tag.prettify())