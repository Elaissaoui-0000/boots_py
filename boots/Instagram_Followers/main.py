from instagrapi import Client
import os
from time import sleep

USERNAME = ''
PASSWORD = ''
PATH = './Instagram_Followers/cred.json'
class BOT:
    brian = None
    def __init__(self) -> None:
        self.brian = Client()
        if os.path.exists(PATH):
            self.brian.load_settings(PATH)
            self.brian.login(USERNAME,PASSWORD)
        else:
            self.brian.login(USERNAME,PASSWORD)
            self.brian.dump_settings(PATH)
    
    def follow_username(self, username):
        user_id = self.brian.user_id_from_username(username)
        self.brian.user_follow(user_id)
    
    def get_username_followers(self, username, amoute):
        print(f"getting {amoute} of {username} followers")
        user_id = self.brian.user_id_from_username(username)
        data = self.brian.user_followers(user_id)
        return [user.username for user in data.values()]
        
    def follow_username_list(self, data):
        for username in data:
            user_id = self.brian.user_id_from_username(username)
            self.brian.user_follow(user_id)
            print(f'following ( {username} ) done !!')
        print('follow users done')
            
    
    def update(self):
        pass
    
bot=BOT()
usernames = bot.get_username_followers("natgeo", 5)
print(usernames)
bot.follow_username_list(usernames)

bot.update()
sleep(120)