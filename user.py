from mysqlconnection import connectToMySQL

class usercls:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at= data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_schema').query_db(query)
        # print(results)
        userlist = []
        for user in results:
            userlist.append(cls(user))
        return userlist
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first)s, %(last)s, %(email)s)"
        result = connectToMySQL("users_schema").query_db(query,data)
        return result

    def get_one():
        pass

    def update():
        pass

    def delete():
        pass