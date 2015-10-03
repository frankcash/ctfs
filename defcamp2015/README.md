# DEFCAMP Qualifiers 2015 Dump


# Crpyto 50: (Solved)

Question: 11 short texts have been encrypted with the same stream cipher. No no! Figure out the 11th plaintext!

Solution:
I originally attempted just `xor`-ing cipher 11 to the other ciphers.  
I then realized that crib dragging was necessary due to "same stream cipher" description in the problem.
I quickly coded up a crib dragging `xor` solution (`xor.py`).  
Guessed at the key quite a few times more than I'd like to admit and then guessed `cipher` which started to decrypt. And repeated this process a few time.

Flag: `When using a stream cipher, never use the key more than once!`

# Web 100: (Solved)

Problem: Web site with simple input box, adds a cookie that keep track of your "money". You only gain $10 with the provided code but need to reach enough to 'buy' the flag.

Solution:
Full path disclosure by setting the cookie value to null.

Flag: `DCTF{3a9bad36a0fb1edcaa83b6669d667061}`
