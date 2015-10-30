import sys


"""
Search both the AFINN file & the twitter file.X
Look for AFINN terms in each tweet.X
tweet_sentiment does both the above

For tweets with AFINN terms, create a filtered list containing these
tweets

In the filtered list look for additional terms that are repeated
with the AFINN term.

Assign some type of sentiment value to the non-AFINN terms.

Return the term & it's value ('term' float(12.03))
"""
tweet_sentiment funcs

def filtered_list(filtered_list):
    #for term in filtered_list:
        #new_sent = []
        #if sentiment != 0:
        #    new_sent.append(item)
    #return new_sent
    pass

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
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
