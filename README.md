# face-recognition
## cleanup.py
There was a bug in the script that downloaded images for the identities. The program somehow mixed up images of two identities within the same file. This program removes the wrong images for each identity to ensure we can build the gallery correctly.

## gallery.py
This program builds the gallery. It first removes low-quality face captures (usually background faces) whose FD_SCORE and UF_SCORE are both below 0.1. Then it sorts the sum of the absolute values of YAW, ROLL, and PITCH coordinates for each identity and select the smallest two images as "perfect images" to build the gallery.

