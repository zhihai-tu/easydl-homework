import urllib3,base64
import json
import requests 

urllib3.disable_warnings()

# 调用第一个接口，获取access_token
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=GmBhFIIFWEjjhLhFQyHcD0Dn&\
client_secret=h4oKYyKoFnsGz1QPfLpnKf2wApFhNs0Q'
response = requests.get(host)
if response:
    access_token=response.json()["access_token"]
    
http=urllib3.PoolManager()
url='https://aip.baidubce.com/rpc/2.0/ai_custom_pro/v1/text_cls/emotion0313?access_token='+access_token

word=''
while word != "exit" and word != "quit":
	#输入需要识别的文本
	word = input("Input key word: ")
	params={"text": word}

	#对参数params数据进行json处理
	encoded_data = json.dumps(params).encode('utf-8')

	request=http.request('POST', 
	                      url,
	                      body=encoded_data,
	                      headers={'Content-Type':'application/json'})
	result = str(request.data,'utf-8')
	print(result)

print("program exit!")
