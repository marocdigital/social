import facebook
id = '109105195512089'
access_token = 'EAALGGR827TQBAMGCv7KaTgwJFJ7ApQfbaFYhrfGJblcjv5iUug5QxwVG1A7MCr6OsN1F2uRORf61jMKeqcMYMbaIkollZCYMoxv9nNjxFhkxWfrSsW4zeDX6JCFvQasd2HbdZAd53b9oDwzxKPjGutFdmOs8BM1EdXGjIcuFiH0M83RWKXJy2FkHO4UokZBxgFKuZAWPvEzSLK06Jwh9'
graph = facebook.GraphAPI(access_token)
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

get_post_shares()