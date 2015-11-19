import json
import string
import sys


def tweets(tweet_file):
    tweet_list = []
    for tweet in tweet_file:
        tweet_list.append(json.loads(tweet))

    return tweet_list

def tweet_count(tweet_list):
    count_list = []
    for x in tweet_list:
        term = ''
        count = 0
        if x.get('text'):
            text = x.get('text').encode("ascii", "ignore")
            exclude = set(string.punctuation + string.digits)
            temp = ''.join(c for c in text if c not in exclude)
            bag = temp.split()
            for term in bag:
                count += 1
        if count != 0:
            if term in count_list:
                print term
            # import  ipdb;ipdb.set_trace()
            count_list.append({term: float(count)})
        
    return count_list

def term_freq(tweet_counts):
    total_term = len(tweet_counts)
    for i in tweet_counts:
        for k in i:
            value = i[k]
            term_count = value/total_term
            print k, term_count
    

def main():
    tweet_file   = open(sys.argv[1])
    tweet_list   = tweets(tweet_file)
    tweet_counts = tweet_count(tweet_list)
    term_freq(tweet_counts)

if __name__ == '__main__':
    main()
