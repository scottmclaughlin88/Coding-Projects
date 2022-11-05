import pandas as pd

def load_twitter_data(filename):
#UTF-8 doesn't work
    df = pd.read_csv(filename, encoding = 'ISO-8859-1')
    return df

df = load_twitter_data('twitter.csv')
text = list(df['text'])


print(text[0:50])