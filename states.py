import requests
import json
import os
from bs4 import BeautifulSoup

open('states.txt', 'w')

BASE_URL = "http://en.wikipedia.org/wiki/"
STATE_URLS = [
    'Alaska',
    'Alabama',
    'Arkansas',
    'Arizona',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'Florida',
    'Georgia_(U.S._state)',
    'Guam',
    'Hawaii',
    'Iowa',
    'Idaho',
    'Illinois',
    'Indiana',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Massachusetts',
    'Maryland',
    'Maine',
    'Michigan',
    'Minnesota',
    'Missouri',
    'Mississippi',
    'Montana',
    'National',
    'North_Carolina',
    'North_Dakota',
    'Nebraska',
    'New_Hampshire',
    'New_Jersey',
    'New_Mexico',
    'Nevada',
    'New_York',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Rhode_Island',
    'South_Carolina',
    'South_Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Virginia',
    'Vermont',
    'Washington_(state)',
    'Wisconsin',
    'West_Virginia',
    'Wyoming'
]
# STATE_URLS = [
#     'South_Dakota',
# ]

label_count = {
    'pos': 0,
    'neg': 0,
    'neutral': 0
}

max_sentiment = ['', 0]
min_sentiment = ['', 1]
avg_sentiment = ['', 0]

try:
    def analyze_probability(state, probabilities):
        """
        Will look at the sentiment probs of the text and set the appropriate variables
        :param probabilities: will be of the form
            {
                "neg": 0.22499999999999998,
                "neutral": 0.099999999999999978,
                "pos": 0.77500000000000002
            }
        :return: None
        """
        pos = probabilities['pos']
        neg = probabilities['neg']
        neutral = probabilities['neutral']

        if pos > max_sentiment[1]:
            max_sentiment[0] = state
            max_sentiment[1] = pos

        if neg < min_sentiment[1]:
            min_sentiment[0] = state
            min_sentiment[1] = neg

        records = open("states.txt", "a")
        records.write("--------------------\n")
        records.write("Processing: %s" % state + "\n")
        records.write("Max Sentiment" + str(max_sentiment) + "\n")
        records.write("Min Sentiment" + str(min_sentiment) + "\n")
        records.write("--------------------\n\n")
        records.close()



    for state_url in STATE_URLS:
        print("Processing: %s" % state_url)

        soup_content = None
        if not os.path.isfile('states/cached-%s' % state_url):
            url = BASE_URL + state_url
            r = requests.get(url)
            if r.status_code != 200:
                raise RuntimeError(url)

            soup_content = BeautifulSoup(r.content, "html.parser").find('div', {'id': 'bodyContent'}).getText()

            cached_state_wiki = open('states/cached-%s' % state_url, 'w')
            cached_state_wiki.write(soup_content)

        else:
            soup_content = open('states/cached-%s' % state_url).read()

        post_data = {'text': soup_content[:50000]}
        raw_sentiment = requests.post("http://text-processing.com/api/sentiment/", data=post_data)

        sentiment = json.loads(raw_sentiment.content.decode('UTF-8'))
        sentiment_label = sentiment['label']

        label_count[sentiment_label] += 1
        analyze_probability(state_url, sentiment['probability'])

except :
    print('')
    raise
















