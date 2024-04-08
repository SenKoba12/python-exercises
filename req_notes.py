import requests

#FOR GET PARAMS
params = {
    "name" : "Keith",
    "age" : 21
}

#FOR POST DATA
payLoad = {
    "name" : "Blake",
    "age" : 21
}

##FOR GET REQUEST##
#response = requests.get("https://httpbin.org/get")
#get response from url

#response = requests.get("https://httpbin.org/get", params=params)
#print(response.url)
#get response with additional parameters

##FOR POST REQUEST##
#response = requests.post("https://httpbin.org/post", data=payLoad)
#print(response.url)


##FOR STATUS CODES EG. ERROR 404
#response = requests.get("https://httpbin.org/status/404")

#if response.status_code == requests.codes.not_found:
    #print("Not Found")
#else:
    #print(response.status_code)
## RETURNS STATUS CODE VALUE


#FOR USER AGENTS && IMAGES
headers = {
    "User-Agent" : "HelloWorld/1.1",
    "Accept": "image/jpeg"
}

#response = requests.get("https://httpbin.org/user-agent", headers=headers)
#print(response.text)

#FOR IMAGES
#response = requests.get("https://httpbin.org/image", headers=headers)
##SOME SITES PROHIBIT USER AGENTS LIKE PYTHON. TO ALLOW THIS, CHANGING THE USER AGENT MAY PRODUCE RESULTS
#with open('myimage.jpg',"wb") as f:
    #f.write(response.content)


#FOR REQUEST TIMEOUTS
#response = requests.get("https://httpbin.org/delay/2", timeout=3)
#ALTENATIVELY...
#for _ in [1,2,3]:
    #try:
        #response = requests.get("https://httpbin.org/delay/2", timeout=3)
    #except:
        #continue

#PROXY SERVERS
proxies = {
    "http": "139.99.237.62:80",
    "https": "139.99.237.62:80"
}

response = requests.get("http://httpbin.org/get", proxies=proxies)
print(response.text)

#print(response.status_code)
#get status code

#print(response.text)
#obtain response as a json file that is read as a dictionary from url

res_json = response.json()
del res_json['origin']
print(res_json)
#obtain json file but no origin(remove ip add)

