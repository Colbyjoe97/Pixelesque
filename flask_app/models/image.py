from flask_app.config.mysqlconnection import connectToMySQL


class Image:
    db = 'pixelesque'
    def __init__(self, data):
        self.id = data['id']
        self.image = data['image']

    
    @classmethod
    def save(cls, data):
        print(data)
        query = 'INSERT INTO images (image) VALUES (%(image)s)'
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM images'
        results = connectToMySQL(cls.db).query_db(query)
        images = []

        for i in results:
            images.append(cls(i))
        return images