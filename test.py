from slogger import Logger
import logging
import sys

def main():
    lg = Logger.getLogger("cat1")
    
    lg.debug("debug hello to cat1")
    lg.info("info hello to cat1")
    
if __name__ == "__main__":
    main()
