#k-means
import numpy as np
import random 

def get_user_reputation_data():
	f = open('u.data', 'r')
# array
	ratings = [[ 0 for i in range(1690)] for j in range(944)]

	for line in f:
		inp = line.split()
   		for i in range(4):
   			ratings[int(inp[0])][int(inp[1])]=inp[2]
	return ratings

def get_user_data():
  f = open('u.user', 'r')
	#  array
  users = []
  for line in f:
  	inp =line.split("|")
  	user_inp = [0 for j in range(3)]
  	user_inp[0] = int(inp[1])
  	if inp[2] == "M":
  		user_inp[1] = 0
  	if inp[2] == "F":
  		user_inp[1] = 1
  	if inp[3] == 'administrator':
  		user_inp[2] = 0
  	if inp[3] == "artist":
  		user_inp[2] = 1
  	if inp[3] == "doctor":
  		user_inp[2] = 2
  	if inp[3] == "educator":
  		user_inp[2] = 3
  	if inp[3] == "engineer":
  		user_inp[2] = 4
  	if inp[3] == "entertainment":
  		user_inp[2] = 5
  	if inp[3] == "executive":
  		user_inp[2] = 6
  	if inp[3] == "healthcare":
  		user_inp[2] = 7
  	if inp[3] == "homemaker":
  		user_inp[2] = 8
  	if inp[3] == "lawer":
  		user_inp[2] = 9
  	if inp[3] == "librarian":
  		user_inp[2] = 10
  	if inp[3] == "marketing":
  		user_inp[2] = 11
  	if inp[3] == "none":
  		user_inp[2] = 12
  	if inp[3] == "other":
  		user_inp[2] = 13
  	if inp[3] == "programmer":
  		user_inp[2] = 14
  	if inp[3] == "retired":
  		user_inp[2] = 15
  	if inp[3] == "scientist":
  		user_inp[2] = 16
  	if inp[3] == "student":
  		user_inp[2] = 17
  	if inp[3] == "salesman":
  		user_inp[2] = 18
  	if inp[3] == "technician":
  		user_inp[2] = 19
  	if inp[3] == "writer":
  		user_inp[2] = 20 			
	users.append(user_inp)
  return users
  

def get_movie_data():
	f = open('u.item', 'r')
# array
	movies = []
	
	for line in f:
		inp = line.split("|")
		#print inp
		movie_inp = []
   		for i in range(len(inp)):
   			if i > 4:
   				movie_inp.append(inp[i])
   			else:
   				pass
   		movies.append(movie_inp)
   		if movie_inp[-1] == '0\n':
   			movie_inp[-1] = 0
   		elif  movie_inp[-1] == '1\n':
   			movie_inp[-1] = 1
   		else:
   			pass
	return movies

def cluster(data,k):
	#print data
	for i in range(len(data)):
		data[i].append(random.randint(0,k-1))
	return data

def cluster_update(data,k):
	cluster = [[] for j in range(k)]
	for i in range(len(data)):
		cluster[data[i][-1]].append(data[i]) 
	jushin = [[0 for b in range(len(data[0]))] for e in range(k)]
	tmat = [0 for b in range(k)]

	for i in range(k):	
		tmat[i] = np.array(cluster[i]).transpose()
		for j in range(len(cluster[i])):
			for w in range(len(data[0])):
				jushin[i][w] = np.mean(tmat[i][w])
	
	for d in range(len(data)):
		minimize = [[0 for b in range(len(data[0]))] for e in range(k)]
		for i in range(k):			
			for j in range(len(data[i])-1):
				minimize[i][j] = (data[d][j]-jushin[i][j])**2
		judge_cluster = [0 for c in range(k)]
		for  c in range(k):
			for d2 in range(len(data[0])):
				judge_cluster[c] += minimize[c][d2]
		minimam = np.min(judge_cluster)
		data[d][j+1] = judge_cluster.index(minimam)
		new_cluster = data[d][j+1]
		
	return data,jushin

def get_cluster_score(key_data,jushin):
	key_jushin = jushin[key_data[-1]-1]
	judge_jushin = [[0 for b in range(2)] for e in range(k)]
	for i in range(k):
		for j in range(len(key_data)-1):
			judge_jushin[i][0] += (key_data[j]-jushin[i][j])**2
		judge_jushin[i][1] = i
	judge_jushin_sort = sorted(judge_jushin)
	for i in range(k):
		judge_jushin_sort[i].append(k-i)
	return judge_jushin_sort


def get_item_score(cluster_data,jushin_score):
	for i in range(len(cluster_data)):
		for j in range(k):
			if cluster_data[i][-1] == jushin_score[j][1]:
				cluster_data[i].append(jushin_score[j][2])
				break
			else:
				pass
	return cluster_data

def get_user_score(recom_data,user_data):
	for i in range(len(user_data)):
		u = user_data[i][-1]
		r = recom_data[i][-1]
		u_score = (u+r)/2
		user_data[i][-1] = u_score
	return user_data

def  get_recommend(key_data,recomend_movie_id_uniq,movie_cluster_data):
	f = open('u.item', 'r')
	movie = []
	for line in f:
		movie.append(line)
	for  i in range(len(key_data)):
		if key_data[i] == 5:
			cluster = movie_cluster_data[i][-1]
			pass
	for j in range(len(recomend_movie_id_uniq)):
		if key_data[int(recomend_movie_id_uniq[j])] == 0 and movie_cluster_data[j][-1] == cluster:
			print movie[j] 
	

if __name__ == "__main__":	
	####make and arrange data
	rep_data = get_user_reputation_data()
	movie_data = get_movie_data()
	user_data = get_user_data()

	for i in range(len(rep_data)):
		for j in range(len(rep_data[0])):
			rep_data[i][j]=int(rep_data[i][j])
	for i in range(len(user_data)):
		for j in range(len(user_data[0])):
			user_data[i][j]=int(user_data[i][j])

	for i in range(len(movie_data)):
		for j in range(len(movie_data[0])):
			movie_data[i][j]=int(movie_data[i][j])

	####get clustering data (recom_data)
	######
	k = 20
	d = cluster(rep_data,k)
	cd = []
	d = cluster_update(d,k)
	cd.append(d[0])
	#print "update"
	d = cluster_update(d[0],k)
	cd.append(d[0])
	while cd[-1] != cd [-2]:
		d = cluster_update(d[0],k)
		cd.append(d[0])
	jushin = d[1]
	cluster_data = d[0]
	#####key_data is target's rep_data
	key_data = rep_data[1]
	####give cluster score to each data
	jushin_score = get_cluster_score(key_data,jushin)
	rep_score = get_item_score(cluster_data,jushin_score)

	####get clustering data (recom_data)
	d = cluster(user_data,k)
	cd = []
	d = cluster_update(d,k)
	cd.append(d[0])
	#print "update_user"
	d = cluster_update(d[0],k)
	cd.append(d[0])
	####cluster update
	while cd[-1] != cd [-2]:
		d = cluster_update(d[0],k)
		cd.append(d[0])
	jushin = d[1]
	cluster_data = d[0]
	#####key_data is target's rep_data
	key_data = user_data[1]
	####give cluster score to each data
	jushin_score = get_cluster_score(key_data,jushin)
	demo_score = get_item_score(cluster_data,jushin_score)

	####get user_score -> mean(rep and user)
	user_score = get_user_score(rep_score,demo_score)

	##clustering in movie data
	
	d = cluster(movie_data,k)
	cd = []
	d = cluster_update(d,k)
	cd.append(d[0])
	#print "updatee"
	d = cluster_update(d[0],k)
	cd.append(d[0])
	####cluster update
	while cd[-1] != cd [-2]:
		d = cluster_update(d[0],k)
		cd.append(d[0])

	jushin = d[1]
	movie_cluster_data = d[0]

	#keyman = ##### now key man = data[0]
	##get key_man's high score movie

	#key_data = ####key_man's reputation data 
	###get high score users -> score is k
	####and get high score users id
	high_user = [i for i in user_score if i[-1] == k]
	high_user_index = []
	for i in range(len(high_user)):
		for j in range(len(user_score)):
			if high_user[i] == user_score[j]:
				high_user_index.append(j)
			else:
				pass
	
	###get movie id which high_user rate is 5
	recomend_movie_id = []
	for i in range(len(high_user_index)):
		high_user_movie_rep = rep_data[int(high_user_index[i])]
		movie_id = [k for k,j in enumerate(high_user_movie_rep) if j == 5]
		for j in range(len(movie_id)):
			recomend_movie_id.append(movie_id[j])
	
	recomend_movie_id_uniq = list(set(recomend_movie_id))

	get_recommend(rep_data[1],recomend_movie_id_uniq,movie_cluster_data)



