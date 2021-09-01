from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 영화 제목 매트릭스의 평점 가져오기

# 한 개 찾기 - 예시
movie = db.movies.find_one({'title':'매트릭스'})
print(movie['point'])

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_points = list(db.movies.find({'point':movie['point']},{'_id':False}))

for same_movie in same_points:
    print(same_movie['title'])
    
# 바꾸기 - 예시
db.movies.update_one({'title':'매트릭스'},{'$set':{'point':0}})