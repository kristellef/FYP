from lib.db import DB
from lib.DisjointSet import DisjointSet
from pprint import pprint

import json
from migrations.createTables import createTables

# Load configuration file and connect to database
with open('config.json') as json_file:
    config = json.load(json_file)

db = DB(config['DB'])

# createTables(db)

# Load transaction json file
with open('data.json') as json_file:
    transactions = json.load(json_file)['data']

query = """
        INSERT INTO TRANSACTIONS (receiver, sender, amount) VALUES ('{0}', '{1}', {2});
    """

for transaction in transactions:
    receiver1=transaction['to'][18:][:-24]
    sender1=transaction['from'][18:][:-24]
    amount1=transaction['value'][:-4]

    # db.execute([query.format(str(receiver1),str(sender1),str(amount1))],False);

results = db.execute(["SELECT receiver, sender from transactions"]);

ds = DisjointSet()

for result in results:
    ds.add(result[0], result[1])

pprint(ds.group)