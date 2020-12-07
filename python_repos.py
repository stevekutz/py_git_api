import requests

# Create API calll and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f" Status code: {r.status_code}\n")

# store API response
response_dict= r.json()

# process dict info
print(response_dict.keys())
print(f" Total Python repositories >> {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f' Repositories returned : {len(repo_dicts)}')


# Examine first repository
repo_dict = repo_dicts[0]
print(f"\n keys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(f' key >> {key}')


print("\n Selected info on each repository")    
for repo_dict in repo_dicts:
    print(f' \n Name: {repo_dict["name"]}')
    print(f' Owner: {repo_dict["owner"]["login"]}')
    print(f' Stars: {repo_dict["stargazers_count"]}')
    print(f' Respository: {repo_dict["html_url"]}')
    print(f' Description: {repo_dict["description"]}')