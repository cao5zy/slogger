from ..log import Logger
import logging
from codegenhelper import test_root, init_test_folder, remove_test_folder, put_file
from nose import with_setup
from assertpy import assert_that, contents_of
import os

logging.basicConfig(level=logging.DEBUG)

def test_getLogger():
    logger = Logger.getLogger("test_module")

    logger.debug("debug info")
    logger.title("x").debug("debug info")



def init_logger_config():
    put_file('logger_wrapper.cfg', './', '''[handlers]
all_all
''')
    
def remove_files():
    os.remove('logger_wrapper.cfg')
    os.remove('all.log')
    
@with_setup(init_logger_config, remove_files)
def test_all_from_file():
    logger = Logger.getLogger('test_module1')

    logger.debug('debug for test_module1')

    assert_that('all.log').exists()
    content = contents_of('all.log')
    assert_that(content).contains("debug for test_module1")

def init_config_for_category():
    put_file('logger_wrapper.cfg', './', '''[handlers]
all_all: test1
''')

@with_setup(init_config_for_category, remove_files)
def test_category():
    logger = Logger.getLogger("test_module2")
    logger.debug('debug for test_module2') # the content should not be output to all.log

    logger1 = Logger.getLogger("test1")
    logger1.debug('debug for test1') # the content should be output to all.log
    
    content = contents_of("all.log")
    assert_that(content).does_not_contain("debug for test_module2")
