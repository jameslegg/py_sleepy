import simplejson
import tweepy
import time
def sleeper():
    while True:
        print "Sleeping for 3.."
        time.sleep(3)
        print "Wake up! for 1.."
        time.sleep(1)
        print "this is fun"

if __name__ == "__main__":
    sleeper()
