import time
def sleeper():
    while True:
        print "Sleeping for 3.."
        time.sleep(3)
        print "Wake up! for 1.."
        time.sleep(1)

if __name__ == "__main__":
    sleeper()
