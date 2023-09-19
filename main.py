import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

url = 'https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjk1MTI2OTI2LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D'

data = {
    'jazoest': '2951',
    'lsd' : 'AVpia6DT_lM',
    'email': '0177183063',
    'login_source': 'comet_headerless_login',
    'next': '',
    'encpass': '#PWD_BROWSER:5:1695126932:ASlQAB7cw32vUvvul+cFXlrJlSIuLLzaN9ap88lIDOP4qRhi0X5eRA3fnwwyYYPWFPpco7+6zGSyrNTdKt54cir1CabCFNxakCbmCTMPIl2N1bqYQCLC9ADTTIK7UufXFzR9wgnFldnghbpKbiMFU78aUA=='
}

response = requests.post(url = url, headers = headers, data = data)

response.encoding = 'utf-8'

# print(response.content)
print(response.text)
print(response)
print(response.url)