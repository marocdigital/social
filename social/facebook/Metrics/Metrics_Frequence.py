
import facebook
from datetime import datetime
import operator
import functools
id = 'page_id'
access_token = 'access_token'

graph = facebook.GraphAPI(access_token)
PostsGrph = graph.get_object(id=id, fields='posts')

#all posts
Posts = PostsGrph['posts']['data']

alltimes = []
newtimes = []
times = []
for post in Posts:
    newpost = post['created_time'].split('T')
    alltimes.append(newpost)
#converti string to date
for time in alltimes:
    datetime_object = datetime.strptime(time[0], '%Y-%m-%d')
    newtimes.append(datetime_object)
#Calculate the difference between the dates :
for i in range(len(newtimes) - 1) :
    times.append(newtimes[i]- newtimes[i+1])
times.append(newtimes[len(newtimes) - 2] - newtimes[len(newtimes) - 1])

#Calculate the sum of the dates
result = functools.reduce(operator.add, times)
print(result)