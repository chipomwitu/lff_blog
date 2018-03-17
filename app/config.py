import os
class Configuration(object):
    DEBUG=True
    #PORT=6702 # ?
    APPLICATION_DIR=os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI='sqlite:///{}/blog.db'.format(APPLICATION_DIR)
    # dialect+driver://username:password@host:port/database
    # postgresql://postgres:password@localhost:5432/blog_db
    SQLALCHEMY_TRACK_MODIFICATIONS=True
