# social
Python Project to becnhmark social presence

# social
Python Project to becnhmark social presence

# Facebook Scraper 🤖

<p align="center">
<img src="images/header.png">
</p>****

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 

This tool allows you to scrape Facebook Posts based on search queries .

## Prerequisites 🚀

You will need python 3+.

First clone this repo, then navigate to the folder and install the requirements

```
git clone https://github.com/IbtissamBerroho/social.git
cd social
pip install -r requirements.txt
```
## To Get Count of likes

```python
id = "page_id"
access_token = "access_token"

graph = facebook.GraphAPI(access_token)
posts = graph.get_object(id=id, fields='posts')
Posts = posts['posts']['data']
```

```python
def get_count_likes():
    i = 1
    for post in Posts:
        post_id = post['id']
        url = f"https://graph.facebook.com/v13.0/{post_id}?fields=likes.summary(total_count)&access_token={access_token}"
        response = requests.get(url)
        data = response.json()
        likes_count = data['likes']['summary']['total_count']
        print(f'''
                Post : Number {i} has :"{likes_count}" likes
                ''')
        i += 1```

```
### Output Exemple : 
```
  Post : Number 1 has :"2" likes
  Post : Number 2 has :"2" likes
  Post : Number 3 has :"3" likes
  Post : Number 4 has :"3" likes
```
## To Get Count of comments

```python
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
```
## Output exemple : 
```
post number 1 has 2 comments
post number 2 has 1 comments
post number 3 has 1 comments
post number 4 has 1 comments
                
```
## To get Count of shares 

```python
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
```
## Output exemple :

```
Post number 1 has no shares !
Post number 2 has 1 shares
Post number 3 has no shares !
Post number 4 has no shares !
```

## To get infos about Page 

```python
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
```

## Output exemple :
```
Page Name               : FirstPage
The number of Followers : 2
About  Page             : testing
Phone Page              :  +212614414091
birthday                : 05/04/1988
Posts count of page     : 4

Picture cover           : https://z-p3-scontent.fcmn1-1.fna.fbcdn.net/v/t39.30808-6/345022313_1716339945481945_131495556255635423_n.png?_nc_cat=106&ccb=1-7&_nc_sid=1091cb&_nc_eui2=AeG4D2CphdWkZq1dlp48aHmH67VayckNStfrtVrJyQ1K1-TuxDAiE24y6f7ydSBytTzGj_1n6zoJbgCXqOmq7k2G&_nc_ohc=bPdFwLDRRjEAX_yZeFd&_nc_zt=23&_nc_ht=z-p3-scontent.fcmn1-1.fna&edm=AJdBtusEAAAA&oh=00_AfCchS8G2xm-DWO_e6nalZctdJCHzAXKseiUeBEZDCYjKA&oe=6467682E

Picture profile         : https://z-p3-scontent.fcmn1-1.fna.fbcdn.net/v/t39.30808-1/345022313_1716339945481945_131495556255635423_n.png?stp=cp0_dst-png_p50x50&_nc_cat=106&ccb=1-7&_nc_sid=dbb9e7&_nc_eui2=AeG4D2CphdWkZq1dlp48aHmH67VayckNStfrtVrJyQ1K1-TuxDAiE24y6f7ydSBytTzGj_1n6zoJbgCXqOmq7k2G&_nc_ohc=bPdFwLDRRjEAX_yZeFd&_nc_ht=z-p3-scontent.fcmn1-1.fna&edm=AJdBtusEAAAA&oh=00_AfCT_glUz1aj5TTXI73FRFKa-BcqYQjOQ_8Q5gPLWJAEPg&oe=646695EC
```
