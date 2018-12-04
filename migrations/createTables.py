from lib.db import DB

def createTables(db: DB):
    
    commands = []

    # Create rent table
    commands.append("""
        CREATE TABLE IF NOT EXISTS address_mapping (
        address VARCHAR NOT NULL,
        id bigint NOT NULL,
         PRIMARY KEY (id)
        );
    """)

    db.execute(commands, False)
