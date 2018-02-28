# Random-Data-Generation-Python-Code

##  Implementation of pseudo-random number generators for various distribution. 

The functions supplied here are actually bound methods of a hidden instance of the random.Random class. You can instantiate your own instances of Random to get generators that don’t share state. This is especially useful for multi-threaded programs, creating a different instance of Random for each thread, and using the jumpahead() method to make it likely that the generated sequences seen by each thread don’t overlap.

Class Random can also be subclassed if you want to use a different basic generator of your own devising: in that case, override the random(), seed(), getstate(), setstate() and jumpahead() methods. Optionally, a new generator can supply a getrandbits() method — this allows randrange() to produce selections over an arbitrarily large range.
