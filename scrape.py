'''
    Scraping Twitter for all tweets that include 
    $NKE, the ticker symbol for Nike

    We scrape data for the year 2020, from 1st Jan 2020 till 1st Jan 2021

    Scraping is done using Twint, a Twitter Scraping tool that does not use the Twitter API
    Twitter Search API requires a developer account which you need to request Twitter for

    @Author: Akhil Kumar, 11-05-2021
'''

# import twint
# make sure you have the package installed: pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
# pip3 install twint does not work anymore. Twitter had blocked the endpoint 
import twint 

# configure scraping parameters
c = twint.Config ()
c.Search = "$NKE"
c.Lang   = 'en'

c.Since = '2017-01-01'
c.Until = '2021-01-01'

c.Hide_output = True
c.Store_csv   = True
c.Output      = "Nike_tweets_2017_20.csv"

c.Min_likes = 2

c.Custom["tweet"] = ["date", "time", "username", "tweet"]

# scrape with this configuration
print ("Starting scraping ... ")
twint.run.Search (c)

