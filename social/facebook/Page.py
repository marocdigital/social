#+++++++++++++
# Page Model +
#+++++++++++++
import facebook

def GetPageInfos() :
    id = '109105195512089'
    access_token = 'EAALGGR827TQBAG8BT6nNY3g06FPrjDrOUnuWyHrMb4ik0U26MKQAqaPyZCAEHj2geRTRea6yjuUz3iQFXp2oBntTmxZAQt6L0wJBkWJihMIZBuv99uDpiX2C0kSgq8H13jpixUtpILwYHhLGOHHh7BEHRid0ogVAmqjCVy07YeNk2aBtrk6zG0zrHAJZAxIFRzlmgMvM3F1ZCluzXzXvX'
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
    for item in profile :
        if item == 'description' :
            print(f"Description of page: : {profile['description']}")






GetPageInfos()