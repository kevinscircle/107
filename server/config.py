import pymongo
import certifi


con_str='mongodb+srv://test:test@cluster0.qmq9x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'



client = pymongo.MongoClient(con_str, tlsCAfile=certifi.where())
db=client.get_database('organika') # name of db 