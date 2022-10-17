import botometer
from _init_ import Botometer

rapidapi_key = "xxx"
twitter_app_auth = {
    'consumer_key': 'xxx',
    'consumer_secret': 'xxx',
    'access_token': 'xxx',
    'access_token_secret': 'xxx',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@DisneyPlus')
#print(result)
# Check a single account by id
result = bom.check_account(1548959833)
#print(result)
# Check a sequence of accounts
accounts = ['@hourlyyuzu', '@vismyg', '@emmekalin']
for screen_name, result in bom.check_accounts_in(accounts):
    print(screen_name)
    print(result)

