import requests
import pandas as pd

api_url_post = 'https://jsonplaceholder.typicode.com/posts'
api_url_user = 'https://jsonplaceholder.typicode.com/users'

res_posts = requests.get(api_url_post)
res_users = requests.get(api_url_user)
# display(res_posts)
# display(res_users)

if res_posts.status_code == 200:
    # Convert JSON response to a Python dictionary
    data = res_posts.json()
    df_posts = pd.DataFrame(data)

if res_users.status_code == 200:
    # Convert JSON response to a Python dictionary
    data = res_users.json()
    df_users = pd.DataFrame(data)
