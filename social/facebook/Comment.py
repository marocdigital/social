#++++++++++++++++
# Comment Model +
#++++++++++++++++
import requests
import facebook
id = '109105195512089'
access_token = 'EAALGGR827TQBAPjDJ4iPkWE0g3GaDAzVlFLfjlciPlF74ZCyvshyYxsu9ZCVfnlymcQGDUoVjZBPYwNL4sn5n1pvZBhphTsQ6K26ZCgJO6C9zWu0S8SG5jI2EUSbkFhWNlZCsLSgYJZBxbVEY3HS5qUsuwyIeu2E3XZAHpaSem9vYmMCc7zOemsGnJL0KtdePSZBIh1uWGGLwzMTZAlfADEsrr'
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




