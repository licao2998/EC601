import tweepy
import webbrowser
import time
import pandas as pd
from pandas import DataFrame as df
import json
import config

def extract_timeline_as_df(timeline_list):
    columns = set()
    allowed_types = [str, int]
    tweets_data = []
    for status in timeline_list:
        #print(status.text)
        #print(type(vars(status)))
        #print(status.user.screen_name)
        status_dict = dict(vars(status))
        keys = status_dict.keys()
        single_tweet_data = {"user": status.user.screen_name, "author": status.author.screen_name}
        for k in keys:
            try:
                v_type = type(status_dict[k])
            except:
                v_type = None
            if v_type != None:
                if v_type in allowed_types: 
                    single_tweet_data[k] = status_dict[k]
                    columns.add(k)
        tweets_data.append(single_tweet_data)

    header_cols = list(columns)
    header_cols.append("user")
    header_cols.append("author")

    df = pd.DataFrame(tweets_data, columns=header_cols)
    return df

def update_own_status():
    user_input = input("what's the details of the update? ")
    new_status = api.update_status(user_input)

if __name__ == "__main__":
    callback_uri = 'oob'
    auth = tweepy.OAuthHandler(config.consumer_key,config.consumer_secret,callback_uri)
    redirect_url = auth.get_authorization_url()
    webbrowser.open(redirect_url)
    user_pint_input = input("what's the pin value? ")
    auth.get_access_token(user_pint_input)

    api=tweepy.API(auth)

    me=api.me()
    print(me.screen_name)

    update_own_status()

    status_obj = api.get_status("1581332329309425670")
    print(status_obj.text)

    my_timeline = api.home_timeline()
    user = api.get_user("code")
    user_timeline = user.timeline()
    user_timeline_status_obj = user_timeline[0]
    status_obj_id = user_timeline_status_obj.id
    status_obj_screen_name = user_timeline_status_obj.user.screen_name
    status_obj_url = f"https://twitter.com/{status_obj_screen_name}/status/{status_obj_id}"

    #api.retweet(status_obj_id)
    #api.create_favorite(status_obj_id)

    df_my_timeline = extract_timeline_as_df(my_timeline)
    df_my_timeline.to_json(path_or_buf='test1.json',orient="table")
    df_my_timeline.head()

    df_user_timeline = extract_timeline_as_df(user_timeline)
    df_user_timeline.to_json(path_or_buf='test2.json',orient="table")
    df_user_timeline.head()
