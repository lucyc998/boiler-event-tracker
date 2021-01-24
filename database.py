from pymongo import MongoClient


def uploadToDB(title, location, content, lat, lon):
    client = MongoClient('localhost', 27017)
    db = client.locations
    posts = db.posts

    post_data = {
        'Event': str(title),
        'Location': str(location),
        'Description': str(content),
        'lat': str(lat),
        'lon': str(lon)
    }

    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))

def fetchFromDB():
    client = MongoClient('localhost', 27017)
    db = client.locations
    posts = db.posts
    return posts.find()

print(fetchFromDB()[0])

#find_content = posts.find_one({'lat': '40'})
#print(find_content)
#for document in posts.find():
#    print(document)

