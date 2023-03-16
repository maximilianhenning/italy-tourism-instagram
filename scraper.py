from instaloader import Instaloader, Profile
import time
import os

path = os.path.dirname(__file__)
with open(path + "/accounts.txt", "r") as infile:
    lines = infile.read()
accounts = lines.split("\n")

l = Instaloader(download_videos = False, 
                save_metadata = False, 
                post_metadata_txt_pattern="", 
                dirname_pattern=path + "{profile}/")

def account_scraper(account):
    print(account)
    profile = Profile.from_username(l.context, account)
    posts = profile.get_posts()
    post_counter = 0
    while True:
        for post in posts: 
            l.download_post(post, profile)
            post_counter += 1
            time.sleep(6)
            print(post_counter)
            if post_counter == 10:
                print("break")
                posts = []
                break
        
for account in accounts:
    account_scraper(account)