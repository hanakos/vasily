import numpy as np
import sys
#from sklearn.cluster import KMeans

#moviefile import
f = open('u.data', 'r')
#movie array
movies = []
#movie = [[ for i in range(3)] for j in range(5)]
for line in f:
    inp = line.split("|")
    print inp
    movie_inp = [inp[0]]
    #for i in range(18):
    #	movie_inp.append(inp[i])
    movies.append(movie_inp)
print movies

#kmeans_model = KMeans(n_clusters=15, random_state=10).fit(movies)
