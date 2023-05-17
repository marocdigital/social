import facebook
id = 'page_id'
access_token = 'access_token'
graph = facebook.GraphAPI(access_token)
Shares = graph.get_object(id=id, fields='posts{shares}')

#all posts
postsShares = Shares['posts']['data']

#Get count of shares
def get_post_shares():
    i = 1
    for post in postsShares:
        if next(iter(post)) == 'shares' :
            print(f'Post number {i} has {post["shares"]["count"]} shares')
        else:
            print(f'Post number {i} has no shares !')
        i+=1

get_post_shares()