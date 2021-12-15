import sqlalchemy as db
from sqlalchemy import text
from faker import Faker

# specify db config
config = {
    'host' : 'localhost',
    'port' : 3307,
    'user' : 'user',
    'password' : 'pwd',
    'database' : 'alinedb'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = db.create_engine(connection_str)
connection = engine.connect()

def populate_transaction(conn):
    fake = Faker()
    # optional clear table entries
    clear = True
    if clear:
        conn.execute(text('DELETE FROM transaction'))
        conn.execute(text('ALTER TABLE transaction AUTO_INCREMENT = 1'))

    # create and insert X entries
    num_entries = 10
    for i in range(num_entries):
        # define values to be inserted into user table
        # id is bigInt auto-inc
        amount = fake.numerify('#####') # int
        date = fake.date_time() # datetime(6) nullable
        description = fake.word() # varchar(255) nullable
        initial_balance = fake.numerify('#####') # int
        last_modified = fake.date_time() # datetime(6) nullable
        method = fake.word() # varchar(255)
        posted_balance = fake.numerify('#####') # int nullable
        state = fake.state() # varchar(255)
        status = fake.word() # varchar(255)
        type = fake.word() # varchar(255)
        # account_id is restricted foreign key from table 'account'
        # merchant_code is restricted foreign key from table 'merchant'

        # create and execute insert string
        trans_ins = text("INSERT INTO transaction (amount, date, description, initial_balance, last_modified, method, posted_balance, state, status, type) VALUES (:amount, :date, :description, :initial_balance, :last_modified, :method, :posted_balance, :state, :status, :type)")
        conn.execute(trans_ins, amount=amount, date=date, description=description, initial_balance=initial_balance, last_modified=last_modified, method=method, posted_balance=posted_balance, state=state, status=status, type=type)

populate_transaction(connection)