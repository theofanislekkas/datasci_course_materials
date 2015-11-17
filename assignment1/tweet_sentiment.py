import json
import re
import sys


def senti_file(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    
    return scores

def tweets(tweet_file):
    tweet_list = []
    for tweet in tweet_file:
        tweet_list.append(json.loads(tweet))

    return tweet_list

def sentiment(tweet_list, scores):
    for x in tweet_list:
        if x.get('text'):
            tscore = 0
            text = x.get('text').encode("ascii", "ignore")
            bag = text.split()
            for term in scores:
                if term in bag:
                    sent = bag.count(term)
                    tscore += sent*scores[term]
            print tscore

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = senti_file(sent_file)
    tweet_list = tweets(tweet_file)
    sentiment(tweet_list, scores)


if __name__ == '__main__':
    main()
