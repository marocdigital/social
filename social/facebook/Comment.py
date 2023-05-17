#++++++++++++++++
# Comment Model +
#++++++++++++++++
import requests
import facebook
id = 'page_id'
access_token = 'access_token'
graph = facebook.GraphAPI(access_token)
posts = graph.get_object(id=id, fields='posts')
Posts = posts['posts']['data']

#get Count of comments
def get_post_comments():
    i = 1
    for post in Posts :
        x = post['id']
        url = f"https://graph.facebook.com/v13.0/{x}?fields=comments.summary(total_count)&access_token={access_token}"
        response = requests.get(url)
        data = response.json()
        for k, v in data.items():
            if k == "comments" :
                print(f'''
                    post number {i} has {v['summary']['total_count']} comments
                ''')
            elif k == "error":
                print(f'''
                    post number {i} has no comments
                ''')
        i+=1

get_post_comments()




