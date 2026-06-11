import sys
sys.path.append('instabot')
from instabot import Bot

bot=Bot(filter_users=False,max_following_to_followers_ratio=100)

bot.login(username='', password='')
followers = bot.get_user_followers('')

i=0
for user in followers[105:]:
    username = bot.get_username_from_user_id(user)
    print(f'attemping to follow {username}')
    if bot.follow(username):
        i += 1
        print(f"follwed-{username}")
    else:
        print(f"Not followed-{username}")
        if i > 150:
            break
    