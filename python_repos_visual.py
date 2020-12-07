import requests


from plotly.graph_objs import Bar
from plotly import offline

# Create API calll and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f" Status code: {r.status_code}\n")

# store API response and process results
response_dict= r.json()
repo_dicts = response_dict['items']

repo_names, stars = [],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Build visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

layout_plot = {
    'title': 'Most starred Python projects in Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},

}

figure = {'data': data, 'layout': layout_plot}
offline.plot(figure, filename = 'python_repos.html')
