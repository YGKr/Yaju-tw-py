# coding: utf-8

from requests_oauthlib import OAuth1Session
import data     

url = "https://api.twitter.com/1.1/account/update_profile.json"

params = {"name":"野獣先輩","description":"二十四歳、学生です","url":"114514.com","location":"下北沢"}

twitter = OAuth1Session(data.CK, data.CS, data.AT, data.AS)
req = twitter.post(url, params = params)