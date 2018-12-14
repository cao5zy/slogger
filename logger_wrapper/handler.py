from fn import F
from configparser import ConfigParser
from os import path
import os

def loadHandlerNames():
    def work(config_name, section_name):
        if not path.exists(config_name):
            print('config is not found at {}/{}, default std output will be used.'.format(os.getcwd(), config_name))
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
        def dummy(handler_dict, handler_name_key, type_of_interval, handler_key, get_file_name):
            from logging.handlers import TimedRotatingFileHandler

            handler_dict[handler_key] = TimedRotatingFileHandler(get_file_name(handler_dict[handler_name_key]), type_of_interval)

            return handler_dict

        return [dummy(handler_dict, "name", "D", "handler", lambda name: "{}.log".format(name)) for handler_dict in handler_names]

    def setHandlers(handler_names):
        for handler_dict in handler_names:
            logger.addHandler(handler_dict["handler"])

    (F(loadHandlerNames) >> \
        F(getValidNames) >> \
        F(buildHandlers) >> \
        F(setHandlers))()
    
    return logger
