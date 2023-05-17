#+++++++++++++
# Page Model +
#+++++++++++++
import facebook

id = 'page_id'
access_token = 'access_token'
graph = facebook.GraphAPI(access_token)

#get Infos of page
def GetPageInfos() :
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

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#test
#GetPageInfos()



