# Default environments for testing, staging and production are included.
from girru.environments import *

env.project = 'erskine_design'

def testing():
    env.hosts = [default_testing_server]
    env.name = 'testing'
    env.path = '/var/www/redactor_test.erskinedev.com'

def staging():
    env.hosts = [default_staging_server]
    env.name = 'staging'
    env.path = '/var/www/redactor_test.erskinestage.com'

# Do not modify below this line
from girru.operations import *
