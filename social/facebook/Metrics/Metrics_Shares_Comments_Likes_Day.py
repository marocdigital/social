import facebook
import requests
from .. import Page

id = "109105195512089"
access_token = "EAALGGR827TQBAPFuRMZAlQF9TBT9WmIm8q4q4pHdN49Nd00ifnXpCZAeaxtW9CNOwQaDSpDNpulmqiVGhDBqHcTPoIsVoaOJ8ghx65XurlvqADRWlifyVmaLibYGU7taj5V1R13KNd1xF4zE8jBpES2Bvq7xPGbDi4WGLeezdRKsjV2En5MiKd18871ZCA7aKvr3jdOzgPw5IedJhHF"

graph = facebook.GraphAPI(access_token)
posts = graph.get_object(id=id, fields='posts')
Posts = posts['posts']['data']


def get_Count_Comments_Per_Day():
    i = 1
    for post in Posts :
        x = post['id']
        url = f"https://graph.facebook.com/v13.0/{x}?fields=comments.summary(total_count)&access_token={access_token}"
        response = requests.get(url)
        data = response.json()
        metric = Page.GetPageInfos()
        insights = graph.get_object(id=id + '/insights/' + metric)
        print(metric)

get_Count_Comments_Per_Day()


