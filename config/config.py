class ConfigData:
    
    USER_NAME = '{twitter username}'
    BASE_URL = 'https://api.twitter.com/2/users/'
    BEARER_TOKEN = '{Twitter Bearer Token}'
    HEADERS = {'Authorization': BEARER_TOKEN}
    USER_BY_USERNAME_URL = f'{BASE_URL}by/username/{USER_NAME}'
    USER_ID = ''
    
    
    @classmethod
    def set_config(cls, userid):
        if userid == '':
            raise ValueError('User ID should not be empty!')
        
        cls.USER_ID = userid
        cls.FOLLOWING_URL = f'{cls.BASE_URL}{userid}/following'
        cls.FOLLOWERS_URL = f'{cls.BASE_URL}{userid}/followers'
        
        