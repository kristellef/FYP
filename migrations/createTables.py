from lib.db import DB

def createTables(db: DB):
    
    commands = []

    # Create rent table
    commands.append("""
        CREATE TABLE transactions (
        receiver VARCHAR NOT NULL,
        sender VARCHAR NOT NULL,
        amount DOUBLE precision NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT NOW()
        );
    """)

    db.execute(commands,False);