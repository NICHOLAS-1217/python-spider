import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

kw = {
    'wd' : 'python'
}

keyword = {
    'keyword' : 'python'
}

url = 'https://www.facebook.com/'

data = {
    'wd' : 'python'
}

response = requests.get(url = url, headers = headers)

response.encoding = 'utf-8'

# print(response.content)
print(response.text)
print(response)
print(response.url)