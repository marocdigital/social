#+++++++++++++
# Page Model +
#+++++++++++++
import facebook

def GetPageInfos() :
    id = '109105195512089'
    access_token = 'EAALGGR827TQBAPjDJ4iPkWE0g3GaDAzVlFLfjlciPlF74ZCyvshyYxsu9ZCVfnlymcQGDUoVjZBPYwNL4sn5n1pvZBhphTsQ6K26ZCgJO6C9zWu0S8SG5jI2EUSbkFhWNlZCsLSgYJZBxbVEY3HS5qUsuwyIeu2E3XZAHpaSem9vYmMCc7zOemsGnJL0KtdePSZBIh1uWGGLwzMTZAlfADEsrr'
    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object(id=id, fields='name,photos,access_token,followers_count,about,description,posts,phone,birthday,albums,picture,cover')
    print(f'''
            Page Name : : {profile['name']}
            The number of Followers : : {profile['followers_count']}
            About  Page: {profile['about']}
            Phone Page :  {profile['phone']}
            birthday : {profile['birthday']}
            Posts count of page  : {len(profile['posts']['data'])}
            Picture cover  : {profile['cover']['source']}
            Picture profile  : {profile['picture']['data']['url']}
        ''')
    for item in profile:
        if item == 'description':
            print(f"Description of page: : {profile['description']}")




GetPageInfos()



