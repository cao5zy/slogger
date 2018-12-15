from logger_wrapper import Logger
import logging
import sys

def main():
    lg = Logger.getLogger("cat1")
    
    lg.debug("debug hello to cat1")
    lg.info("info hello to cat1")
<<<<<<< 6977a306e12a0c87acbe811729f075e7963a6495
=======

    def greet_me(**kwargs):
        if kwargs is not None:
            for key, value in kwargs.items():
                print("%s == %s" %(key,value))

    greet_me(name="alan", id=123)
>>>>>>> add test
    
if __name__ == "__main__":
    main()
