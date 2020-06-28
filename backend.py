import os, json, face_recognition, heapq, numpy
import os.path
import math
from os import path

def knn_search (file_stream, k):
    index = {}
    if path.exists ('photo_index.json'):
        print ("index exists")
        with open ('photo_index.json', "r") as index_file:
            index = json.load (index_file)
    else:
        print ("index does not exist")
        for root, dirs, files in os.walk ("lfw", topdown=True):
            for name in dirs:
                name = "lfw/" + name
                for filename in os.listdir (name):
                    pathname = name + "/" + filename
        #pathname = 'fotos_bd/'
        #for filename in os.listdir (pathname):
        #    filename = pathname + filename
                    img = face_recognition.load_image_file (pathname)
                    img_encoding = face_recognition.face_encodings (img)
                    if len (img_encoding) == 0:
                        img_encoding = [0] * 128
                    else:
                        img_encoding = img_encoding[0]
                        img_encoding = img_encoding.tolist ()
                    index[pathname] = [img_encoding]

        with open ('photo_index.json', 'w+') as output:
            json.dump (index, output, indent=4)

    query_encoding = get_query_encoding (file_stream)
    k_nearest_neighbors = get_knn_ED (index, query_encoding, k)
    return k_nearest_neighbors

def get_query_encoding (file_stream):
    query_img = face_recognition.load_image_file (file_stream)
    query_face_encoding = face_recognition.face_encodings (query_img)
    return query_face_encoding

def get_knn_ED (index, query_face_encoding, k):
    result = []
    for filename in index.keys ():
        distance = ED (query_face_encoding, index[filename])
        heapq.heappush (result, (-distance, filename))
        if len (result) > k:
            heapq.heappop (result)
    result = [(filename, -distance) for distance, filename in result]
    result.sort (key = lambda x: x[1])
    return result

def get_knn_MD (index, query_face_encoding, k):
    result = []
    for filename in index.keys ():
        distance = MD (query_face_encoding, index[filename])
        heapq.heappush (result, (-distance, filename))
        if len (result) > k:
            heapq.heappop (result)
    result = [(filename, -distance) for distance, filename in result]
    result.sort (key = lambda x: x[1])
    return result

def ED (x, y):
    zipped = zip (x, y)
    distance = 0
    for a, b in zipped:
        for i in range (len (a) - 1):
            if len (a) - 1 < i:
                v1 = 0
            else:
                v1 = a[i]
            if len (b) - 1 < i:
                v2 = 0
            else:
                v2 = b[i]
            distance += (v1 - v2) ** 2
    distance = math.sqrt (distance)
    return distance

def MD (x, y):
    zipped = zip (x, y)
    distance = 0
    for a, b in zipped:
        for i in range (len (a) - 1):
            distance += abs (a[i] - b[i])
    return distance

#photo_path = "fotos_query/avril_lavigne_query.jpg"
#result = knn_search (photo_path, 3)
#print (result)
