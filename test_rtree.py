import os 
import face_recognition
import numpy as np
from rtree import index
import time

path = '/home/francesco/Desktop/bd/pc4/fotos_test/lfw'
path1 = '/home/francesco/Desktop/bd/pc4/fotos_bd'


def get_embedding(filepath):

    # Load the uploaded image file
    img = face_recognition.load_image_file(filepath)
    # Get face encodings for any faces in the uploaded image
    unknown_face_encodings = face_recognition.face_encodings(img)
    return unknown_face_encodings

# R tree ------------------------------------------------------------

p = index.Property()
p.dimension = 128
p.interleaved=True
idx3d = index.Index('128d_index',properties=p)

N=800
#-----------------------------------------------------------------

i=0
allencodings=[]
for root, dirs, files in os.walk ("fotos_test/lfw", topdown=True):
	for name in dirs:
		name = "fotos_test/lfw/" + name
		for filename in os.listdir (name):
			print("hola",i)
			pathname = name + "/" + filename
			allencodings.append(get_embedding(pathname))
			i+=1
			if i == N:
				break
		if i == N:
			break
	if i==N:
		break

	





    	
print(len(allencodings))
for encoding in allencodings:
	for encodingg in encoding:
		newencoding=[]
		for i in range(0,128):
			newencoding.append(encodingg[i])
		for i in range(0,128):
			newencoding.append(encodingg[i])
		print(newencoding[0],newencoding[128])
		idx3d.insert(1, tuple(newencoding))

#consulta ----------------------------------------------------------

allencodings1=[]
with os.scandir(path1) as it:
    for entry in it:
    	allencodings1.append(get_embedding(entry.path))

for encoding in allencodings1:
	for encodingg in encoding:
		newencoding=[]
		for i in range(0,128):
			newencoding.append(encodingg[i])
		for i in range(0,128):
			newencoding.append(encodingg[i])
		q=newencoding
		

start_time = time.time()

lres = list(idx3d.nearest(coordinates=q, num_results=9))
print("Los 9 vecinos mas cercanos son: ", lres)
print("--- %s seconds ---" % (time.time() - start_time))

	
#-----------------------------------------------------------------
		




