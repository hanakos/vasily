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
	#print ratings
	return ratings

def get_user_data():
  f = open('u.user', 'r')
	#  array
  users = []
  for line in f:
  	inp =line.split("|")
  	#print inp
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
	#print users
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
   		#print movie_inp
   		#print movie_inp[-1]
   		if movie_inp[-1] == '0\n':
   			movie_inp[-1] = 0
   		elif  movie_inp[-1] == '1\n':
   			movie_inp[-1] = 1
   		else:
   			pass
   			
   	#print k
	#print ratings
	return movies

def cluster(data,k):
	#print data
	for i in range(len(data)):
		data[i].append(random.randint(0,k-1))
	return data

def cluster_update(data,k):
	#print len(data)
	cluster = [[] for j in range(k)]
	for i in range(len(data)):
		cluster[data[i][-1]].append(data[i]) 
	jushin = [[0 for b in range(len(data[0]))] for e in range(k)]
	tmat = [0 for b in range(k)]

	for i in range(k):
		
		tmat[i] = np.array(cluster[i]).transpose()
		#print tmat
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
	#print "jushin"
	#print jushin
	#print key_data[-1]
	key_jushin = jushin[key_data[-1]-1]
	judge_jushin = [[0 for b in range(2)] for e in range(k)]
	for i in range(k):
		for j in range(len(key_data)-1):
			judge_jushin[i][0] += (key_data[j]-jushin[i][j])**2
		judge_jushin[i][1] = i
	#print judge_jushin	
	judge_jushin_sort = sorted(judge_jushin)
	#print judge_jushin
	for i in range(k):
		judge_jushin_sort[i].append(k-i)
	return judge_jushin_sort


def get_item_score(cluster_data,jushin_score):
	#print cluster_data
	#print jushin_score
	for i in range(len(cluster_data)):
		for j in range(k):
			if cluster_data[i][-1] == jushin_score[j][1]:
				#print cluster_data[i]
				cluster_data[i].append(jushin_score[j][2])
				break
			else:
				pass
	#print cluster_data
	return cluster_data

def get_user_score(recom_data,user_data):
	for i in range(len(user_data)):
		#print i
		#print user_data[i]
		#print recom_data
		u = user_data[i][-1]
		r = recom_data[i][-1]
		u_score = (u+r)/2
		#print u_score
		user_data[i][-1] = u_score
		#print user_data[i]
	return user_data

def user_to_movie(user_data,movie_data):
	pass


if __name__ == "__main__":
	#rep_data = [[random.randint(1,5) for b in range(15)] for e in range(943)]
	#user_data = [[random.randint(1,100) for b in range(4)] for e in range(943)]
	
	####make and arrange data
	rep_data = get_user_reputation_data()
	print len(rep_data)
	print len(rep_data[1])
	movie_data = get_movie_data()
	print len(movie_data)
	print len(movie_data[1])
	user_data = get_user_data()
	print len(user_data)
	print len(user_data[1])

	for i in range(len(rep_data)):
		for j in range(len(rep_data[0])):
			rep_data[i][j]=int(rep_data[i][j])
	#print type(rep_data[1][1])
	for i in range(len(user_data)):
		for j in range(len(user_data[0])):
			user_data[i][j]=int(user_data[i][j])

	for i in range(len(movie_data)):
		for j in range(len(movie_data[0])):
			movie_data[i][j]=int(movie_data[i][j])

	####clustering get score (recom_data and user_data)
	######
	k = 10
	d = cluster(rep_data,k)
	d = cluster_update(d,k)
	print "update"
	#print d
	d = cluster_update(d[0],k)
	print "ok1"
	d = cluster_update(d[0],k)
	print "ok2"
	jushin = d[1]
	cluster_data = d[0]
	#get_score
	key_data = rep_data[0]
	jushin_score = get_cluster_score(key_data,jushin)
	rep_score = get_item_score(cluster_data,jushin_score)


	d = cluster(user_data,k)
	d = cluster_update(d,k)
	print "update_user"
	#print d
	#print type(d[0][1][1])
	d = cluster_update(d[0],k)
	print "ok1"
	d = cluster_update(d[0],k)
	print "ok2"
	jushin = d[1]
	cluster_data = d[0]
	#get_score
	key_data = user_data[0]
	jushin_score = get_cluster_score(key_data,jushin)
	demo_score = get_item_score(cluster_data,jushin_score)

	####get user_score -> mean(rep and user)
	user_score = get_user_score(rep_score,demo_score)

	##clustering in movie data
	
	d = cluster(movie_data,k)
	d = cluster_update(d,k)
	print "updatee"
	d = cluster_update(d[0],k)
	d = cluster_update(d[0],k)
	jushin = d[1]
	cluster_data = d[0]

	#keyman = ##### now key man = data[0]
	##get key_man's high score movie

	#key_data = ####key_man's reputation data 
	print "user_score"
	print user_score
	high_user = [i for i in user_score if i[-1] == k]
	print "high_user"
	print high_user
	high_user_index = []
	for i in range(len(high_user)):
		for j in range(len(user_score)):
			if high_user[i] == user_score[j]:
				high_user_index.append(j)
			else:
				pass
	print "high_user_index"
	print high_user_index

	recomend_movie_id = []
	for i in range(len(high_user_index)):
		#print i
		high_user_movie_rep = rep_data[int(high_user_index[i])]
		#print int(high_user_index[i])
		#print high_user_movie_rep
		movie_id = [k for k,j in enumerate(high_user_movie_rep) if j == 5]
		for j in range(len(movie_id)):
			recomend_movie_id.append(movie_id[j])
	
	recomend_movie_id_uniq = list(set(recomend_movie_id))
	print recomend_movie_id_uniq


