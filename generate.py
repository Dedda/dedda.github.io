__author__ = 'dedda'

import sys
import generate_index
import generate_projects

debug = 'debug' in sys.argv

print('generating...')

generate_index.generate(debug)
generate_projects.generate(debug)

print('generated!')