import facebook
import requests
id = 'page_id'
access_token = 'access_token'
graph = facebook.GraphAPI(access_token)
PostsGrph = graph.get_object(id=id, fields='posts{likes}')
Posts = PostsGrph['posts']['data']
def get_post_author():
    for post in Posts:
        x = post['id']
        url = f"https://graph.facebook.com/v13.0/{x}?fields=likes.summary(total_count)&access_token={access_token}"
        response = requests.get(url)
        likes = response.json()
        if likes['likes']['data']:
            for item in likes['likes']['data']:
                print(f"post liked by : {item['name']}")
        else :
            print(f"post has no likes")



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


get_post_likes()
get_post_author()