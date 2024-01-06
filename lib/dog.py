import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    all = []

    def __init__(self, name, breed) :
        self.name = name
        self.breed = breed
        self.id = None 

    @classmethod
    def create_table(cls):
     sql = """
              CREATE TABLE IF NOT EXISTS dogs(
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  breed TEXT
              )
        """
     CURSOR.execute(sql)
     CONN.commit()

    @classmethod
    def drop_table(cls):
     sql = """
              DROP TABLE IF EXISTS DOGS
       """
     CURSOR.execute(sql)
     CONN.commit()

    def save(self):
        sql = """
                INSERT INTO dogs (name, breed)
                VALUES(?, ?)

          """
        CURSOR.execute(sql,(self.name, self.breed))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls, name, breed):
       dog = cls(name, breed)
       dog.save()
       return dog
    @classmethod
    def new_from_db(cls, row):
       if row is not None:
        dog = cls(name = row[1], breed = row[2])
        dog.id = row[0]
        return dog
       else:
          return cls(None, None)
    
    @classmethod
    def get_all(cls):
       sql = """
        SELECT * FROM  dogs
        """
       all = CURSOR.execute(sql).fetchall()
       cls.all = [cls.new_from_db(row) for row in all]
       return cls.all
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM dogs
            WHERE name = ?
            LIMIT 1
        """

        dog = CURSOR.execute(sql,(name,)).fetchone()
        return cls.new_from_db(dog)

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM dogs
            WHERE id = ?
            LIMIT 1
        """

        dog = CURSOR.execute(sql, (id,)).fetchone()
        return cls.new_from_db(dog)

    @classmethod   
    def find_or_create (cls,):
       Dog.find_by_name ()
       

    
