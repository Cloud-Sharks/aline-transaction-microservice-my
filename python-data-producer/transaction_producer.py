import requests
from faker import Faker

def populate_transaction(auth, acc_nums):
    fake = Faker()
    register_url = 'http://localhost:8073/transactions'

    transaction_entries = len(acc_nums)
    for i in range(transaction_entries):
        register_info = {
            "amount" : fake.numerify('#####'), # int
            "date" : fake.numerify('201#-0%-1#'), # datetime(6) nullable
            "initialBalance" : fake.numerify('####'), # int
            "method" : fake.random_element(elements=('ACH','ATM','CREDIT_CARD','DEBIT_CARD','APP')), # varchar(255)
            "merchantCode" : '1111',
            "state" : fake.random_element(elements=('CREATED','PROCESSING')), # varchar(255)
            "status" : fake.random_element(elements=('APPROVED','DENIED','PENDING')), # varchar(255)
            "type" : fake.random_element(elements=('WITHDRAWAL','TRANSFER_OUT','TRANSFER_IN','DEPOSIT')), # varchar(255)
            "accountNumber" : acc_nums[i]
            # account_id is restricted foreign key from table 'account'
            # merchant_code is restricted foreign key from table 'merchant'
        }
        reg_trans = requests.post(register_url, json=register_info, headers=auth)
        # print(reg_trans.text)

# login_info = {
#     'username' : 'adminUser',
#     'password' : 'Password*8'
# }
# login_response = requests.post('http://localhost:8070/login', json=login_info)
# bearer_token = login_response.headers['Authorization']
# auth = {'Authorization' : bearer_token}
# populate_transaction(auth)
