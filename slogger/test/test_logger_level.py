from ..log import Logger
import logging
from codegenhelper import test_root, init_test_folder, remove_test_folder, put_file
from nose import with_setup
from assertpy import assert_that, contents_of
import os


def init_config_for_level_all():
    put_file('slogger.cfg', './', '''[handlers]
all_all
''')

def init_config_for_level_info():
    put_file('slogger.cfg', './', '''[handlers]
all_info
''')

def init_config_for_level_with_complex_name():
    put_file('slogger.cfg', './', '''[handlers]
app_x1_all
''')

def remove_files_for_complex_name():
    os.remove('slogger.cfg')
    os.remove('app_x1.log')
    
def remove_files():
    os.remove('slogger.cfg')
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
    
@with_setup(init_config_for_level_with_complex_name, remove_files_for_complex_name)
def test_level_with_complex_file_name():
    logger = Logger.getLogger("test_level_with_complex_name")
    logger.debug("debug for test_level_with_complex_name") # the content should be output to all.log

    content = contents_of("app_x1.log")
    assert_that(content).contains("debug for test_level_with_complex_name")
    
