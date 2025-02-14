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

def filtered_list(tweet_list, scores):
    new_list = []
    for x in tweet_list:
        if x.get('text'):
            for term in scores:
                new_list.append(x)
            return new_list


"""
Should I be doing a word count?  It seems as though that I should use the
AFINN terms to lookup repeated terms.  Something like:

    asd = scores[term]
    if asd in x.get('text'):
        I'm actually stumped here.
        What I want to find is what terms are most frequently used with
        scores[term].  Then assign some values to those new terms (based
        on count probably.)
"""

def new_sentiment(repeated_terms):
    #if sentiment > 0:
    #    total = new_term.count()
    #    new_sent_score = total*some_value
    #else:
    #    if sentiment < 0:
    #        total = new_term.count()
        #    new_sent_score = total*some_value
    #return new_term, new_score
    pass

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = senti_file(sent_file)
    tweet_list = tweets(tweet_file)
    new_list = filtered_list(tweet_list,scores)
    repeated_terms(new_list)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
