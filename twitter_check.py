import requests
from config.config import ConfigData
from model.dataclass import Response
from model.dataclass import Username
from dacite import from_dict

def get_userid(username):
  res = from_dict(
    data_class = Username, 
    data = requests.get(ConfigData.USER_BY_USERNAME_URL, headers = ConfigData.HEADERS).json()
    )
  return res.data.id
  
  
def get_users(url):
  users = []
  res = from_dict(
    data_class = Response, 
    data = requests.get(url, headers = ConfigData.HEADERS).json()
    )

  users += [i.username for i in res.data]

  while True:
    if res.meta.next_token:
      res = from_dict(
        data_class = Response, 
        data = requests.get(f'{url}?pagination_token={res.meta.next_token}', 
        headers = ConfigData.HEADERS).json()
        )
      users += [i.username for i in res.data]
    else:
      return users


def get_followers():
  return get_users(ConfigData.FOLLOWERS_URL)

  
def get_following():
  return get_users(ConfigData.FOLLOWING_URL)

  
def main():
  try:
    userid = get_userid(ConfigData.USER_NAME)
  except Exception:
    print('Ooopps! Can not get the user id!')
  
  ConfigData.set_config(userid) 
  
  try:
    followers = get_followers()
  except Exception:
    print('Ooopps! Can not get the followers!')

  try:
    following = get_following()
  except Exception:
    print('Ooopps! Can not get the following!')

  target_users = [i for i in following if i not in followers]
  
  print(f'\nThere are {len(target_users)} accounts you follow but they do not\nfollow you on Twitter. Here is it list of them:\n')
  for i in target_users:
      print(i)


if __name__ == "__main__":
    main()





