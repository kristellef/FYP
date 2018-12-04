from lib.db import DB
from lib.DisjointSet import DisjointSet
from pprint import pprint
from lib.BitcoinBlockCrawler import BitcoinBlockCrawler
import json, csv
from migrations.createTables import createTables

# Load configuration file and connect to database
with open('config.json') as json_file:
    config = json.load(json_file)

db = DB(config['DB'])
createTables(db)

# queries1 = []
# addresses = []
# queries1 = """SELECT * FROM addresses;"""
# addresses = db.execute(queries1, False)
# queries2 = []
# query2 = """UPDATE addresses SET id = (SELECT id FROM address_matching where address={0});"""
# for row in addresses:
#     queries2.append(query2.format(row))
# db.execute(queries2, False)

# queries=[]
# query="""INSERT INTO address_mapping (address, id) VALUES ('{0}',{1});"""
#
# csv_file = csv.reader(open('/Users/macbook/Desktop/map_addresses-1_500000.csv', 'rt'), delimiter=',')
# for row in csv_file:
#     try:
#         id = int(row[1])
#     except ValueError:
#         print('Please enter an integer')
#         continue
#     queries.append(query.format(row[0], id))
#
#     if len(queries) == 1000:
#         db.execute(queries,False)
#         queries = []
#         print('Saved 1000.')


