import json
import string
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
            return tscore

def new_sentiment(tweet_list, tscore, scores):
    term_dict = {}
    for x in tweet_list:
        term = ''
        value = 0
        if x.get('text'):
            text = x.get('text').encode("ascii", "ignore").lower()
            exclude = set(string.punctuation + string.digits)
            temp = ''.join(c for c in text if c not in exclude)
            bag = temp.split()
            bag = [x for x in bag if 'http' not in x]
            for term in bag:
                if term not in scores:
                    if tscore > 0:
                        value += 1
                    elif tscore < 0:
                        value -= 1
        if value != 0:
            term_dict.update({term: float(value)})

    for key, value in term_dict.iteritems():
        # import ipdb;ipdb.set_trace()
        print key, value

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = senti_file(sent_file)
    tweet_list = tweets(tweet_file)
    tscore = sentiment(tweet_list, scores)
    new_sentiment(tweet_list, tscore, scores)

if __name__ == '__main__':
    main()
