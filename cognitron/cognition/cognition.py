""" Cognitron main script """

# TODO: Make this module the one in charge of building the MCA up
# It gotta read the cognitron yaml file to load the MCA 
# components and trigger the attention. This module should somehow
# tell the attention what are the elements it's gonna manage so
# it'll call those when the cognitron is alive.

# Each module has sets of operations (SOO)
# e.g. atenttion SOO list: learn_new_sequence=["srlc", "grlc"]
#                    - 1) sent request to the Learning component: cod of seq: srlc
#                    - 2) get the result from the Learning component: grlc
#      then both ops are sent to the attention static class operator
#      alongside required variables
# Same pattern for memory and learning components
