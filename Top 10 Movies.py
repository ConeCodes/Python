# Get top 10 movies using IMDb
# Code to install IMdbPY = python3 -m pip install imdbpy 

import imdb

ia = imdb.IMDb()

search1 = ia.get_top250_movies()
search2 = ia.get_top250_movies()

for i in range(10):
    print (search1[i])

print ('\n')

for a in range(240, 250):
    print (search2[a])