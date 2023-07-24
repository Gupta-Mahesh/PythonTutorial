"""
This module provides access to the garbage collector for reference cycles.

enable() -- Enable automatic garbage collection. 
disable() -- Disable automatic garbage collection. 
isenabled() -- Returns true if automatic collection is enabled. 
collect() -- Do a full collection right now. 
get_count() -- Return the current collection counts. 
get_stats() -- Return list of dictionaries containing per-generation stats. 
set_debug() -- Set debugging flags. 
get_debug() -- Get debugging flags. 
set_threshold() -- Set the collection thresholds. 
get_threshold() -- Return the current the collection thresholds. 
get_objects() -- Return a list of all objects tracked by the collector. 
is_tracked() -- Returns true if a given object is tracked. 
is_finalized() -- Returns true if a given object has been already finalized. 
get_referrers() -- Return the list of objects that refer to an object. 
get_referents() -- Return the list of objects that an object refers to. 
freeze() -- Freeze all tracked objects and ignore them for future collections. 
unfreeze() -- Unfreeze all objects in the permanent generation. 
get_freeze_count() -- Return the number of objects in the permanent generation.
"""
import gc

class hi:
    #to test some value
    pass


print(gc.isenabled())

gc_count=gc.get_count()
print(gc_count)
print(gc.get_objects())


