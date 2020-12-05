# Create API calll and store repose
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f" Status code: {r.status_code}")

# store APU response
response_dict= r.json()

# process dict info
print(response_dict.keys())
