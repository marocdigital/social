import facebook
import requests

id = "109105195512089"
access_token = "EAALGGR827TQBAKcOhc31koZBk5wqDYXLcJZAi2YL1tUEQEal1dME5ppHQT0PwpiCOYjKcmcTbeUlRsGN8YpslMXCpW5s4jSuqM7uZAP4R5Kx7YWO2pas3Bm51cgjcZAdI5ALphFLkp9w7V1pZBM8l9GdvGqfIEHg0QZByNAiDyIT7ekk8vlP9JSJ4fyjZBlopIrYbDT8xl2Gy7Vmfqwvm4ZA"

graph = facebook.GraphAPI(access_token)
posts = graph.get_object(id=id, fields='posts')
Posts = posts['posts']['data']
def get_count_comments():
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

def get_count_likes():
    i = 1
    for post in Posts:
        x = post['id']
        url = f"https://graph.facebook.com/v13.0/{x}?fields=likes.summary(total_count)&access_token={access_token}"
        response = requests.get(url)
        data = response.json()
        likes_count = data['likes']['summary']['total_count']
        print(f'''
                Post : Number {i} has :"{likes_count}" likes
                ''')
        i += 1

Shares = graph.get_object(id=id, fields='posts{shares}')
postsShares = Shares['posts']['data']
def get_count_shares():
    i = 1
    for post in postsShares:
        if next(iter(post)) == 'shares':
            print(f'Post number {i} has {post["shares"]["count"]} shares')
        else:
            print(f'Post number {i} has no shares !')
        i += 1
#test
get_count_comments()
get_count_likes()
get_count_shares()