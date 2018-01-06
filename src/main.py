import os, sys
sys.path.append(os.path.abspath('./lib'))

from chest import waveform

# This file contains multiple entry points for different lambdas.
# It makes sharing code between lambdas really easy :)

def waveform_main(event, context):
    return waveform.main(event, context)
