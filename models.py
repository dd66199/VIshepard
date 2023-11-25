from peewee import *

db = SqliteDatabase('spectres.db')


class User(Model):
    class Meta:
        database = db
        datatable = 'Spectres'
    vk_id = IntegerField()
    name = TextField()
    good = IntegerField()
    evil = IntegerField()
    clown = IntegerField()


if __name__ == '__main__':
    db.create_tables([User])