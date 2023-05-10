#++++++++++++++++
# Comment Model +
#++++++++++++++++
#This includes the comment's content, date, time, author, and engagement metrics (likes, replies, etc.).
import requests
import facebook
id = '109105195512089'
access_token = 'EAALGGR827TQBAMGCv7KaTgwJFJ7ApQfbaFYhrfGJblcjv5iUug5QxwVG1A7MCr6OsN1F2uRORf61jMKeqcMYMbaIkollZCYMoxv9nNjxFhkxWfrSsW4zeDX6JCFvQasd2HbdZAd53b9oDwzxKPjGutFdmOs8BM1EdXGjIcuFiH0M83RWKXJy2FkHO4UokZBxgFKuZAWPvEzSLK06Jwh9'
graph = facebook.GraphAPI(access_token)
posts = graph.get_object(id=id, fields='posts')
Posts = posts['posts']['data']
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




