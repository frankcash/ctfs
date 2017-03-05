# Pragyan CTF 2017

# "Game of Fame" 50: (Solved)

Problem: "p xasc. a zdmik qtng. yiy uist. easc os iye iq trmkbumk. gwv wolnrg kaqcs vi rlr."

Hint: "Robert Sedgewick"

Solution:

The problem appears to be a substitution cipher.  I tried using various cipher methods such as rotation cipher and then kamasutra cipher (which I've never seen before this).
I then continued looking at more "classical" ciphers and tried applying the Vigenere Cipher.  The Vigenere Cipher requires a key to encrypt and decrypt though.
I tried using the CTF's name and out came: `AGAMEAMOVIESTARHISWIFENAMEOFTHECSTEXTBOOKTHEWINNERTAKESITALL`.

I then looked up Sedgewick and found out he wrote many books, the common theme of which was the flag.

Solution: `pragyanctf{algorithms}`
