from pymongo import MongoClient


def uploadToDB(location, content, lat, lon):
    client = MongoClient('localhost', 27017)
    db = client.locations
    posts = db.posts

    db = client.locations
    posts = db.posts

    post_data = {
        'location': str(location),
        'content': str(content),
        'lat': str(lat),
        'lon': str(lon)
    }

    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))

#find_content = posts.find_one({'lat': '40'})
#print(find_content)
#for document in posts.find():
#    print(document)

