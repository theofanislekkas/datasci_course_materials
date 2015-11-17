import json
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
                    # import ipdb;ipdb.set_trace()
                    sent = bag.count(term)
                    tscore += sent*scores[term]
            return tscore

def new_sentiment(tweet_list, tscore, scores):
    for x in tweet_list:
        if x.get('text'):
            if term not in scores:
                if tscore > 0:
                    term value += 1
                elif tscore < 0:
                    term value -= 1
                else:
                    return x, value

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = senti_file(sent_file)
    tweet_list = tweets(tweet_file)
    new_sentiment(tweet_list, tscore, scores)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
