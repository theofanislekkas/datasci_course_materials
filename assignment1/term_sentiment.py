import sys


"""
Search both the AFINN file & the twitter file.
Look for AFINN terms in each tweet.
For tweets with AFINN terms look for additional terms that are repeated
with the AFINN term.
Assign some type of sentiment value to the non-AFINN terms.
Return the term & it's value ('term' float(12.03))
"""


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
