token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjI1OWFhZTNhZTk2YzJlNjFkYzUzOWUxOWQxYzdkOTAyMjczNjhjOWYifQ.eyJpc3MiOiJodHRwczovL3Nzby1kZW1vLmRpZ2l0YWxlbmVyZ3ljbG91ZC5jb20iLCJzdWIiOiJDZ2h2Y0dWeVlYUnZjaElGYkc5allXdyIsImF1ZCI6Im56LW1kciIsImV4cCI6MTUzMzI2MTQxOCwiaWF0IjoxNTMzMTc1MDE4LCJhdF9oYXNoIjoiSnZBdUg3Mks0RjJId3BVYmdEaW5WdyIsImVtYWlsIjoib3BlcmF0b3JAbWVlcmF3b3JrLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiT3BlcmF0b3IifQ.E6Ps0WvvcxJnGgHiXNgfPiXPBrK8gqcJgFHoA6Td44sZNH_vKaCqf00f59oHrX6-mfj9Q_nMHXx0DbvTjmmIt0RuYrtCWNMIW3uI7W1D7s9n3x9J_LDT0Pv1C-4543p7GuW8KZ7wf6AwmA8p6o6Re-Vx_gVLTr5V5XV3PkT3Q8EY_xD4NHqa7V4L9FkU7fLwYwbTTer7h4QZ72v2QgxLGVObSWbhPCUpsjwo6iUWgwt5gbklwD-3OdyogxLS9cMBhbB0WMDOvaz23YbaKg-HZ8F4nQw6E4lg4xeW3o-FHFFQs_zgRKZK_LSj7ld8P4IxrhV8wLAATZmB__1qsqC_6w"
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
