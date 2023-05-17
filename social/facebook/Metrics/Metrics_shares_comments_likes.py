import facebook
import requests

id = "page_id"
access_token = "access_token"

graph = facebook.GraphAPI(access_token)
posts = graph.get_object(id=id, fields='posts')
#all Posts
Posts = posts['posts']['data']

#return count of comments
def get_count_comments():
    i = 1
    for post in Posts :
        x = post['id']
        url = f"https://graph.facebook.com/v13.0/{x}?fields=comments.summary(total_count)&access_token={access_token}"
        response = requests.get(url)
        data = response.json()
        for k, v in data.items():
            if k == "comments" :
                return v['summary']['total_count']
            elif k == "error":
                return f'''
                    post number {i} has no comments
                '''
        i+=1
#return Count of likes
def get_count_likes():
    for post in Posts:
        x = post['id']
        url = f"https://graph.facebook.com/v13.0/{x}?fields=likes.summary(total_count)&access_token={access_token}"
        response = requests.get(url)
        data = response.json()
        likes_count = data['likes']['summary']['total_count']
        return likes_count


Shares = graph.get_object(id=id, fields='posts{shares}')
#all shares
postsShares = Shares['posts']['data']

#return Count of shares
def get_count_shares():
    i = 1
    for post in postsShares:
        if next(iter(post)) == 'shares':
            return post["shares"]["count"]
        else:
            return f'Post number {i} has no shares !'
    i += 1
#test
#get_count_comments()
#get_count_likes()
#get_count_shares()