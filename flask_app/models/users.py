from flask_app.config.mysqlconnection import connectToMySQL


class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
       


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('users_schema').query_db(query)
        users = []

        for i in results:
            users.append( cls(i) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users_schema').query_db(query,data)
        return result
    
    @staticmethod
    def is_valid(form_data):
        is_valid = True
        if len(form_data['first_name']) < 2:
            flash("Invalid. Must be at least 2 characters.", 'err_first_name')
            is_valid = False
        
        if len(form_data['last_name']) < 2:
            flash("Invalid. Must be at least 2 characters.", 'err_last_name')
            is_valid = False
        
        if len(form_data['email']) < 2:
            flash("required", 'err_email')
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address.", 'err_email')
            is_valid = False
        else: 
            lead = User.get_one_by_email({'email': form_data['email']})
            if lead:
                flash('Invalid email. This email is already in use.', 'err_email')        
        return is_valid

   