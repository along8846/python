token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImJlMTliN2E1M2QyZTUxM2EwZTExYzQ0MmRjZWM0OTk5ZjZlNzZjMGMifQ.eyJpc3MiOiJodHRwczovL3Nzby1kZW1vLmRpZ2l0YWxlbmVyZ3ljbG91ZC5jb20iLCJzdWIiOiJDZ2h2Y0dWeVlYUnZjaElGYkc5allXdyIsImF1ZCI6Im56LW1kciIsImV4cCI6MTUzNjkwODY5MSwiaWF0IjoxNTM2ODIyMjkxLCJhdF9oYXNoIjoiWk9mMDk1WnZnb1RIc2lrakZQWDRydyIsImVtYWlsIjoib3BlcmF0b3JAbWVlcmF3b3JrLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiT3BlcmF0b3IifQ.BNkJJ-Ah8ZP78QHYureeai474ZdOauiBUp2YcIeIbWuu1vMz2cZh7z4zMQCLE70B61rFAKpNHbYyDgzy548pOk09PI-TvgNCRajxmG0-AV57kI5guLyItGQeR_Z3j_NRRDpl7O6NGs40kQNR5XSQW38jS0xuoolNno2PPnNTY6wgfHvGA-fOAih5OiyaZwDkXU1Xt0xSHhnEBdq-DUQInXhw3XQ_Y44ASAyecGQGeq9yldY-mgbPp9E0tNJ4arigi6GHB1BBGMlABGad-BTzkO0ZlgM_ZAtNZ1N6ixpwYEUdYpfZ2nVaJGCNc2L8kbCV5vt325TeiMwTEYsmJ5eWsw"
# files = {'file': open('/Users/apple/Downloads/AMS-WPB-REV01-PDO2017-V2.xlsx', 'rb')}


def post_xls(path):
    files = {'file': open(path, 'rb')}
    return files



base_url = "https://sso-demo.digitalenergycloud.com"


def login_account(user):
    accounts = {
        "regulator": [{'login': 'regulator@yopmail.com','password':'regulator' }],
        "operator" : [{'login': 'operator@meerawork.com','password':'operator' }],
        "admin" : [{'login': 'admin@example.com','password':'password' }]
    }
    return accounts[user]    
