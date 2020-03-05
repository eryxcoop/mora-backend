from bson.json_util import dumps

from database import mongo
from . import users


@users.route('/users', methods=['GET'])
def users_list():
    mongo.db.testData.insert_one({'Test': 'usuarioDeTest'})
    test_data = mongo.db.testData.find_one()
    return dumps({'juan': test_data['Test']})

