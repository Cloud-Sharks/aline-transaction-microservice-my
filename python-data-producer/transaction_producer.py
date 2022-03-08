import requests
import logging
import os
from faker import Faker

def populate_transaction(auth, acc_nums):
    logging.basicConfig(level=logging.INFO, filename="aline_files/core-my/docker-data/aline_log.log", filemode='a', format='%(process)d - [%(levelname)s ] - %(message)s')
    fake = Faker()
    # transaction_url = 'http://localhost:8073/transactions'
    transaction_url = f"{os.environ.get('TRANS_URL')}/transactions"

    transaction_entries = len(acc_nums)
    for i in range(transaction_entries):
        transaction_info = {
            "amount" : fake.numerify('#####'),
            "date" : fake.numerify('201#-0%-1#'),
            "initialBalance" : fake.numerify('####'),
            "method" : fake.random_element(elements=('ACH','ATM','CREDIT_CARD','DEBIT_CARD','APP')), 
            "merchantCode" : '1111',
            "type" : fake.random_element(elements=('WITHDRAWAL','TRANSFER_OUT','TRANSFER_IN','DEPOSIT')),
            "accountNumber" : acc_nums[i]
        }
        logging.info(f'Trying to post {transaction_info}')
        try:
            reg_trans = requests.post(transaction_url, json=transaction_info, headers=auth)
            logging.info('Transaction posted')
        except Exception as e:
            logging.error(f'Error entering transaction: ', exc_info=True)

print('', end='')
