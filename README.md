# face-recognition
## cleanup.py
There was a bug in the script that downloaded images for the identities. The program somehow mixed up images of two identities within the same file. This program removes the wrong images for each identity to ensure we can build the gallery correctly.

## gallery.py
This program builds the gallery. It first removes low-quality face captures (usually background faces) whose FD_SCORE and UF_SCORE are both below 0.1. Then it sorts the sum of the absolute values of YAW, ROLL, and PITCH coordinates for each identity and select the smallest two images as "perfect images" to build the gallery.

## matching.py
This program finds a best match for each of the valid faces (either identity face or teammate face) in the gallery. It also records the position of the query identity for each vector (-1 if the query is not in the gallery).

## cdf.py
This program plots the CDF curve of positions of correct identities.
