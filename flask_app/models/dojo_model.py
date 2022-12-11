from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
from flask_app import DATABASE

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM dojos;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row in results:
            dojo_instance = cls(row)
            all_dojos.append(dojo_instance)
        return all_dojos

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM dojos LEFT JOIN ninjas ON dojo_id = dojos.id WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            dojo_instance = cls(results[0])
            ninjas_list = []
            for row in results:
                ninjas_data = {
                    'id' : row['ninjas.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'age' : row['age'],
                    'created_at' : row['created_at'],
                    'updated_at' : row['updated_at'],
                    'dojo_id' : row['dojo_id']
                }
                ninja_instance = ninja_model.Ninja(ninjas_data)
                ninjas_list.append(ninja_instance)
            dojo_instance.ninjas = ninjas_list
            return dojo_instance
        else:
            return False

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO dojos(name) VALUES (%(name)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
