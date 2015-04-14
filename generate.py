__author__ = 'dedda'

import sys
import os
import generate_index
import generate_projects

debug = 'debug' in sys.argv

print('generating...')

generate_index.generate(debug)
generate_projects.generate(debug)
##if debug:
    ##os.system('python generate_index.py debug')
    ##os.system('python generate_projects.py debug')

##else:
    ##os.system('python generate_index.py')
    ##os.system('python generate_projects.py')

print('generated!')