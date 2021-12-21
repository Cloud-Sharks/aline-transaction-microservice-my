import requests
from faker import Faker

def populate_transaction(auth, acc_nums):
    fake = Faker()
    register_url = 'http://localhost:8073/transactions'

    transaction_entries = len(acc_nums)
    for i in range(transaction_entries):
        register_info = {
            "amount" : fake.numerify('#####'),
            "date" : fake.numerify('201#-0%-1#'),
            "initialBalance" : fake.numerify('####'),
            "method" : fake.random_element(elements=('ACH','ATM','CREDIT_CARD','DEBIT_CARD','APP')), 
            "merchantCode" : '1111',
            "type" : fake.random_element(elements=('WITHDRAWAL','TRANSFER_OUT','TRANSFER_IN','DEPOSIT')),
            "accountNumber" : acc_nums[i]
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
