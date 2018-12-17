from ..log import Logger
import logging
from codegenhelper import test_root, init_test_folder, remove_test_folder, put_file
from nose import with_setup
from assertpy import assert_that, contents_of
import os


def init_config_for_level_all():
    put_file('logger_wrapper.cfg', './', '''[handlers]
all_all
''')

def init_config_for_level_info():
    put_file('logger_wrapper.cfg', './', '''[handlers]
all_info
''')


def remove_files():
    os.remove('logger_wrapper.cfg')
    os.remove('all.log')

    
@with_setup(init_config_for_level_all, remove_files)
def test_level_all():
    logger = Logger.getLogger("test_level_all")
    logger.debug('debug for test_level_all') # the content should be output to all.log

    content = contents_of("all.log")
    assert_that(content).contains("debug for test_level_all")

@with_setup(init_config_for_level_info, remove_files)
def test_level_info():
    logger = Logger.getLogger("test_level_info")
    logger.debug("debug for test_level_info") # the content should not be output to all.log

    content = contents_of("all.log")
    assert_that(content).does_not_contain("debug for test_level_info")
