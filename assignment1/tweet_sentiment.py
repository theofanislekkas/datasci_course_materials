import json
import sys


reload(sys)
sys.setdefaultencoding("utf-8")

sent_file = open(sys.argv[1])
tweet_file = open(sys.argv[2])

scores = {}
tweet_dict = []

for tweet in tweet_file:
    tweet_dict.append(json.loads(tweet))
# return tweet_dict

for x in tweet_dict:
    """
    As is, instead of scoring each line & printing out, this loop 
    (w/in a loop) is printing out each value from 0 to 6 in order...
    No idea why that is happening.  I think it's sorting the returned
    values.
    """
    if x.get('text'):
        tscore = 0
        for line in sent_file:
            term, score = line.split("\t")
            scores['term'] = int(score)
            if term in x.get('text'):
                tscore = tscore + scores['term']
            print tscore

# I want to call a function that adds up the sentiment w/in a loop
# that grabs each tweet['text'], not the way I'm doing it above.

def lines(fp):
    print str(len(fp.readlines()))

def main():
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
