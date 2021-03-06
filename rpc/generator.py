import db;

# db init
db.FoxDB().init();
db.FoxDB().start();

def insert():
    db.Block.create(
        number = 1,        
        difficulty = 1,
        gas_limit = 1,
        gas_used = 1,
        hash = 'h',
        size = 1,
        timestamp = 1,
        total_difficulty = 1,
        txs_n = 1,
    );

    db.Tx.create(
        hash = 'hash',
        input = 'input',
    )
    print("Insert Succeed!")

def read():
    print("\nTotal `Block` query: [", db.Block.select().count(), "]")
    for b in db.Block.select():
        print("hash: ", b.hash, "  time:", b.timestamp)

    print("\nTotal `Tx` query: [", db.Tx.select().count(), "]")
    for tx in db.Tx.select():
        print("hash: ", tx.hash, "  input:", tx.input)

arg = input("choose function: (1) insert data  (2) read data :  ");
if arg == str(1):
    insert();
else:
    read();
