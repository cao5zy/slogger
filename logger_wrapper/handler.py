from fn import F
from configparser import ConfigParser
from os import path
import os

def loadHandlerNames():
    def work(config_name, section_name):
        if not path.exists(config_name):
            print('no {} found at {}'.format(config_name, os.getcwd()))
            return []

        config = ConfigParser(allow_no_value=True)
        config.read(config_name)

        if len(config.sections()) == 0:
            print('no settings in section {}'.format(section_name))
            return []

        return dict(config[section_name])

    return work("logger_wrapper.cfg", "handlers")

def getValidNames(all_handler_names):
    def buildObj(name, val, reg_rexp):
        import re
        return {
            'name': re.match(reg_rexp, name).group(1),
            'level': re.match(reg_rexp, name).group(2),
            'filters': [] if val == '' or val == None else val.split(',')
        }
    return [buildObj(name, all_handler_names[name], '''([\w\d]+)_([\w\d]+)''') for name in all_handler_names]        

def loadHandlers(logger):


    def buildHandlers(handler_names):
        pass

    def setHandlers(handlers):
        pass
    
    (F(loadHandlerNames) >> \
        F(getValidNames) >> \
        F(buildHandlers) >> \
        F(setHandlers))()
    
    return logger
