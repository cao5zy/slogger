from ..log import Logger
import logging
from codegenhelper import test_root, init_test_folder, remove_test_folder, put_file
from nose import with_setup
from assertpy import assert_that, contents_of
import os


def init_config_for_category():
    put_file('slogger.cfg', './', '''[handlers]
all_all: test1
''')


def remove_files():
    os.remove('slogger.cfg')
    os.remove('all.log')

    
@with_setup(init_config_for_category, remove_files)
def test_category():
    logger = Logger.getLogger("test_module2")
    logger.debug('debug for test_module2') # the content should not be output to all.log

    logger1 = Logger.getLogger("test1")
    logger1.debug('debug for test1') # the content should be output to all.log
    
    content = contents_of("all.log")
    assert_that(content).does_not_contain("debug for test_module2")
