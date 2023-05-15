import facebook
id = '109105195512089'
access_token = 'EAALGGR827TQBAPjDJ4iPkWE0g3GaDAzVlFLfjlciPlF74ZCyvshyYxsu9ZCVfnlymcQGDUoVjZBPYwNL4sn5n1pvZBhphTsQ6K26ZCgJO6C9zWu0S8SG5jI2EUSbkFhWNlZCsLSgYJZBxbVEY3HS5qUsuwyIeu2E3XZAHpaSem9vYmMCc7zOemsGnJL0KtdePSZBIh1uWGGLwzMTZAlfADEsrr'
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