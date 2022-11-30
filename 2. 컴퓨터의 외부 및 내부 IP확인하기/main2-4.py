import requests
import re
req = requests.get("http://ipconfig.kr")  #http://ipconfig.kr 사이트에서 가져오기

out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1] #'페이지 내에서 해당하는 부분을 찾고 텍스트로 받아오기
print(out_addr)
