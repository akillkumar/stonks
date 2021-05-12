# stonks
Stock market prediction using Twitter sentiment Analysis. 

## Data Collection
Our analysis was conducted on the Nike, Inc. stock ($NKE) for a period of 3 years from Jan 2017 to Jan 2021. We investigate the relationship between Twitter data and stock prices. 

#### Market Data
Downloaded market data for Nike for the last 5 years from Nasdaq, available here: https://www.nasdaq.com/market-activity/stocks/nke/historica

The date formatting is inconsistent, which was fixed using some simple excel functions. Find the final CSV above: Nike_2017_20.csv


#### Twitter Data
Mined relevant Twitter data using [Twint](https://github.com/twintproject/twint), a Twitter scraping tool that does not use the Twitter Search API.

We scraped all tweets between Jan 2017 - Jan 2021 that contain Nike's ticker symbol "$NKE". We could scrape over 105,000 tweets for this time period. 

#### Sentiment Analysis
For Sentiment Analysis, we used [VADER](https://github.com/cjhutto/vaderSentimentb) which gives us sentiments of tweets on an ordinal scale of three values: _positive_, _neutral_, and _negative_

We also calculate the subjectivity and polarity of the tweet using [TextBlob's](https://textblob.readthedocs.io/en/dev/) sentiment subjectivity and polarity scores.

## Model
List of features: Subjectivity, Polarity, Positive sentiment score, Negative sentiment score, Neutral sentiment score, and the Compound sentiment score.

We have data for 1,007 days (average of 100 tweets per day). We split this data into 90% for training and 10% for testing.

For classification, we use the Linear Discriminant Analysis. Althought LDA is defined as a dimensionality-reduction technique, it can be used for classification. The mathematical idea behind LDA is simple; it reduces dimensions but focuses on maximizing the seperability between the known categories. 

LDA uses all the dimensions to create a new axis and projects all dimensions onto the new axis. The new axis is created according to two criteria:
1. Maximize the distance between the means.
2. Minimize the variation (or "scatter") within each category.

## Results
We are able to predict the stock price changes with 84% accurace

![accuracy](https://user-images.githubusercontent.com/46084762/118031696-74b4e800-b384-11eb-862b-c19fa0778017.PNG)

<hr>

