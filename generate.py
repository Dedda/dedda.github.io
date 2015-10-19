#!/usr/bin/python
__author__ = 'dedda'

import sys
import generate_index
import generate_projects
import generate_downloads

debug = 'debug' in sys.argv

print('generating...')

generate_index.generate(debug)
generate_projects.generate(debug)
generate_downloads.generate(debug)

print('generated!')