ECE 459 A1 Backend
==================

This is a tiny python script to return parts of an image (requires PIL, Flask, gevent).
It simulates some service that does computation and returns after some time.
Instead of computing, the script just waits abs(random.gauss(0.2, 0.2))
seconds and then returns the image.

Just kidding. It doesn't do a random sleep. Network delays are killer as it is if you're running this somewhere that's not on your local network.


