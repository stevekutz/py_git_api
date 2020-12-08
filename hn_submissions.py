from operator import itemgetter
import time
import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store response data
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

res =requests.get(url)
print(f' Status Code: {res.status_code}')

# Process info about each submission
submission_ids = res.json()
submission_dicts = []




for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    res = requests.get(url)
    print(f' id: {submission_id}\t status: {res.status_code}')
    response_dict = res.json()

    # Create dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'time': response_dict['time'],
        # 'comments': response_dict['descendants'],
        'score': response_dict['score'],
    }
    submission_dicts.append(submission_dict)

# submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
submission_dicts = sorted(submission_dicts, key=itemgetter('score', 'time'), reverse=True)

article_links, score_val, labels = [], [], []

for submission_dict in submission_dicts:
    # print(f'\n Title: {submission_dict["title"]}')
    # print(f' Discussion link: {submission_dict["hn_link"]}')
    # # print(f' Comments: {submission_dict["comments"]}')
    # print(f' Score: {submission_dict["score"]}')
    # print(f' Date: {time.ctime(submission_dict["time"])}')

    article_link = f'<a> {submission_dict["hn_link"]} </a>'
    article_links.append(article_link)

    score_val.append(submission_dict['score'])

    labels.append(submission_dict['title'])

data_format = [{
    'type': 'bar',
    'x': article_links,
    'y': score_val,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(110, 10, 200)',
        'line': {'width': 1.5, 'color': 'rgb(15, 125, 45)'}
    },
    'opacity': 0.6,
}] 

label_format = {
    'title': 'Highest scored articles on HackerNews',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'HackerNews Articles',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Score',
        'titlefont': {'size': 24},
        'tickfont': {'size': 24},        
        },
}

figure = {'data': data_format, 'layout': label_format}
offline.plot(figure, filename = 'hacker_news.html')