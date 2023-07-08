import requests, json
from django.http import HttpResponse

def create_charge(apikey, amount):
    url = "https://api.zebedee.io/v0/charges"
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    payload = {
    "expiresIn": 300,
    "amount": str(amount),
    "description": "My Charge Description",
    "internalId": "11af01d092444a317cb33faa6b8304b8",
    "callbackUrl": "https://9f45-139-138-146-67.ngrok.io/callback"
    }
    res = requests.post(url, headers=heads, data=json.dumps(payload)).json()

    # {'id': 'b6c35a86-9808-4875-80fe-503d591ee1ff', 'unit': 'msats', 'slots': 0, 'minAmount': '1000000', 'maxAmount': '2000000', 'createdAt': '2022-05-20T07:48:48.183Z', 'expiresAt': None, 'internalId': '11af01d092444a317cb33faa6b8304b8', 'description': 'My Static Charge Description', 'callbackUrl': 'https://9f45-139-138-146-67.ngrok.io/callback', 'allowedSlots': 1, 'successMessage': 'Congratulations your donation was successful!', 'status': 'active', 'invoice': {'request': 'lnurl1dp68gurn8ghj7ctsdyh85etzv4jx2efwd9hj7a3s9aex2ut4v4ehgttnw3shg6tr943ksctjvajhxtmzxe3nxdtp8qmz6wfcxquz6dpcxu6j6wpsvejj6dfsxdjr2wf3v4jnzenx25wtcl', 'uri': 'lightning:lnurl1dp68gurn8ghj7ctsdyh85etzv4jx2efwd9hj7a3s9aex2ut4v4ehgttnw3shg6tr943ksctjvajhxtmzxe3nxdtp8qmz6wfcxquz6dpcxu6j6wpsvejj6dfsxdjr2wf3v4jnzenx25wtcl'}}
    return res

def create_static_charge(apikey):
    url = "https://api.zebedee.io/v0/static-charges"
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    payload = {
	"allowedSlots": 1,
    "minAmount": 1000000,
    "maxAmount": 2000000,
    "description": "My Static Charge Description",
    "internalId": "11af01d092444a317cb33faa6b8304b8",
    "callbackUrl": "https://9f45-139-138-146-67.ngrok.io/callback",
    "successMessage": "Congratulations your donation was successful!"
    }
    res = requests.post(url, headers=heads, data=json.dumps(payload)).json()

    # {'id': 'b6c35a86-9808-4875-80fe-503d591ee1ff', 'unit': 'msats', 'slots': 0, 'minAmount': '1000000', 'maxAmount': '2000000', 'createdAt': '2022-05-20T07:48:48.183Z', 'expiresAt': None, 'internalId': '11af01d092444a317cb33faa6b8304b8', 'description': 'My Static Charge Description', 'callbackUrl': 'https://9f45-139-138-146-67.ngrok.io/callback', 'allowedSlots': 1, 'successMessage': 'Congratulations your donation was successful!', 'status': 'active', 'invoice': {'request': 'lnurl1dp68gurn8ghj7ctsdyh85etzv4jx2efwd9hj7a3s9aex2ut4v4ehgttnw3shg6tr943ksctjvajhxtmzxe3nxdtp8qmz6wfcxquz6dpcxu6j6wpsvejj6dfsxdjr2wf3v4jnzenx25wtcl', 'uri': 'lightning:lnurl1dp68gurn8ghj7ctsdyh85etzv4jx2efwd9hj7a3s9aex2ut4v4ehgttnw3shg6tr943ksctjvajhxtmzxe3nxdtp8qmz6wfcxquz6dpcxu6j6wpsvejj6dfsxdjr2wf3v4jnzenx25wtcl'}}
    return res


def pay_to_ln_address(apikey, lnaddress, amount):
    url = "https://api.zebedee.io/v0/ln-address/send-payment"
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    payload = {
        "lnAddress": lnaddress, #santos@zbd.gg
        "amount": str(amount) + "000", #10000 + 000
        "description": "Payout!" # this what the description is in the zebedee app
    }
    res = requests.post(url, headers=heads, data=json.dumps(payload)).json()
    #{'success': True, 'data': {'id': '44677222-03b1-469b-84fe-717d77664461', 'fee': '0', 'unit': 'msats', 'amount': '100000', 'preimage': None, 'status': 'completed', 'invoice': 'lnbc1u1p3k2360pp5l0tmz9uf2hg85q5nxe52ldpvjy0fvxh7kkey3v5fqz9yx67vn3jshp5gnxw5xy44lje7r5m682425wysngmpvcyx4jp4akacfq5kvkdzf8qcqzpgxqzfvsp5e4hrueuuhhuk6zauz5lfug02frf0cdtljkex3vcz59gpadv90g7s9qyyssqxgvaxmscm9a6ua0h79j2l6dwfgvchwsqclp6u0e7pcqgr788v2erq63nuwfc3u7e3nkj0rryyt7yuuxvxys9xm2kusw3az3vwyv837sqd8zmat', 'walletId': 'ccb56028-fe41-4d67-b3ed-46a840b1fb24', 'transactionId': 'cc8ec7e0-3e80-4e7c-adc5-1cddf1ba8473', 'createdAt': '2022-11-04T17:09:35.791Z', 'processedAt': '2022-11-04T17:09:35.883Z'}, 'message': 'Payment done.'}
    return res

def get_withdrawal(apikey):
    url = "https://api.zebedee.io/v0/withdrawal-requests"
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    payload = {
	"expiresIn": 300,
	"amount": "10000",
	"description": "My Withdrawal Description",
	"internalId": "test transaction",
	"callbackUrl": "https://9f45-139-138-146-67.ngrok.io/callback"
    }
    res = requests.post(url, headers=heads, data=json.dumps(payload)).json()
    print(res)


    return res["data"]["invoice"]["uri"]