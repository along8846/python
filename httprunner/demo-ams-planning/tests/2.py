
import requests
import re

url = 'https://sso-demo.digitalenergycloud.com/auth?client_id=nz-mdr&redirect_uri=https%3A%2F%2Fdemo-ams-01.digitalenergycloud.com%2Fsso%2Fcallback&scope=openid%20email%20groups%20profile%20offline_access&response_type=code&state='
auth_session = requests.Session()

response = auth_session.get(url)

pattern = re.compile(r'req=(.*)" target')
result = pattern.search(response.text)
req = result.groups()[0]
print(req)




auth_url = "https://sso-demo.digitalenergycloud.com/auth/local?req={0}".format(req)
print("auth_url {}".format(url))
account, pwd = 'regulator@yopmail.com', 'regulator'
data = {'login': account, 'password': pwd}
# auth_session_1 = requests.Session()

r = auth_session.post(auth_url,data=data,allow_redirects=False)
# r = auth_session.post(auth_url,data=data)

print(r.status_code)
print(r.url)
print(r.history)
print(r.headers)
# pattern_code = re.compile(r'<code>(.*)<\/code>')
# result = pattern_code.search(res.text)
# code = result.groups()[0]
# print(code)

approval_url = "https://sso-demo.digitalenergycloud.com/approval?req={0}".format(req)
print("approval_url {}".format(approval_url))
approval = auth_session.get(approval_url,allow_redirects=False)
print(approval.status_code)
print(approval.headers)
headersinfo = str(approval.headers)
pattern = re.compile(r'code=(.*)\&')
result = pattern.search(headersinfo)
code = result.groups()[0]
print(code)


# pattern = re.compile(r'req=(.*)" target')
# result = pattern.search(response.text)
# req = result.groups()[0]
# print(req)


token_url = "https://sso-demo.digitalenergycloud.com/token"
data = {'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': 'https://demo-ams-01.digitalenergycloud.com/sso/callback'
        }
headers = {'Authorization' : 'Basic bnotbWRyOkR6WFp4eURPYlNwc25SN3FMcVE0cDFMRVZvSWlFNDll',
           'Content-Type': 'application/x-www-form-urlencoded'
        }
token = auth_session.post(token_url,data=data,headers=headers)
print(token.content)