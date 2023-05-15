#+++++++++++++
# Post Model +
#+++++++++++++


import requests
import facebook

id = 'page_id'
access_token = 'access_token'
graph = facebook.GraphAPI(access_token)

PostsGrph = graph.get_object(id=id, fields='posts')
Posts = PostsGrph['posts']['data']

authors = graph.get_object(id=id, fields='posts{from}')
postsAuthors = authors['posts']['data']

def get_post_author() :
    i=1
    for post in postsAuthors :
        print(f'''
                post number {i} Created by : {post['from']['name']}
                ''')
    i+=1


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_post_Time():
    i = 1
    for Time in Posts :
        print(f'''
            Post Number {i} created at "{Time['created_time']}"
            ''')
        i+=1
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_post_content():
    i = 1
    print(Posts)
    for Time in Posts :
        for k, v in Time.items() :
            if k == "story" :
                print(f'''
                    Post Number {i} has in content "{v}"
                    ''')
            elif k == "message" :
                print(f'''
                    Post Number {i} has in content "{v}"
                    ''')
        i+=1
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_post_likes():
    i = 1
    for post in Posts :
        x = post['id']
        url = f"https://graph.facebook.com/v13.0/{x}?fields=likes.summary(total_count)&access_token={access_token}"
        response = requests.get(url)
        data = response.json()
        likes_count = data['likes']['summary']['total_count']
        print(f'''
            Post : Number {i} has :"{likes_count}" likes
            ''')
        i += 1
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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


Shares = graph.get_object(id=id, fields='posts{shares}')
postsShares = Shares['posts']['data']
def get_post_shares():
    i = 1
    for post in postsShares:
        if next(iter(post)) == 'shares' :
            print(f'Post number {i} has {post["shares"]["count"]} shares')
        else:
            print(f'Post number {i} has no shares !')
        i+=1






#get_post_likes()
#get_post_Time()
#get_post_content()
#get_post_author()
get_post_comments()
get_post_shares()
