from instaloader import Instaloader, Profile
from glob import glob
import time
from os import path

path = path.dirname(__file__)
accounts_done = []
for file in glob(path + "/*"):
    filename = file.split("\\")[-1]
    if not "." in filename:
        accounts_done.append(filename)
with open(path + "/accounts.txt", "r") as infile:
    lines = infile.read()
accounts = lines.split("\n")

l = Instaloader(download_videos = False, 
                save_metadata = False, 
                post_metadata_txt_pattern="", 
                dirname_pattern=path + "/{profile}/")

def account_scraper(account):
    print(account)
    profile = Profile.from_username(l.context, account)
    posts = profile.get_posts()
    post_counter = 1
    while True:
        for post in posts: 
            print(post_counter)
            l.download_post(post, profile)
            post_counter += 1
            time.sleep(6)
            if post_counter > 10:
                posts = []
                break
        break
        
for account in accounts:
    if account not in accounts_done:
        account_scraper(account)