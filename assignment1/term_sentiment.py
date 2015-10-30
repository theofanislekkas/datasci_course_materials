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
            text = x.get('text').encode("ascii", "ignore")
            for term in scores:
                new_list.append(x)
            return new_list

def repeated_terms(new_sent):
    #repeated_terms = []
    #Look for terms that are repeated
    #create a new list of tweets with repeted terms
    #return repeated_terms
    pass

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
    filtered_list(tweet_list,scores)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
