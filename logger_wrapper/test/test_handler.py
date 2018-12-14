from codegenhelper import test_root, init_test_folder, remove_test_folder, put_file
from nose import with_setup
from assertpy import assert_that
from ..handler import loadHandlerNames, getValidNames
import os
import time

def init_config_file():
    init_test_folder()
    put_file('logger_wrapper.cfg', "./", '''[handlers]
all_all
''')

def remove_config_file():
    os.remove('logger_wrapper.cfg')

@with_setup(init_config_file, remove_config_file)
def test_loadHandlerNames():
    assert_that(loadHandlerNames()).contains('all_all')

@with_setup(init_config_file, remove_config_file)
def test_getValidNames():
    dict_data = {"all_all":None}
    assert_that(getValidNames(dict_data)[0]).contains_entry({'name':'all'}) \
    .contains_entry({'level':'all'}) \
    .contains_entry({'filters': []}) \
    
