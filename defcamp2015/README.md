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
Ran `document.cookie="PHPSESSID="` in the JavaScript console.

Flag: `DCTF{3a9bad36a0fb1edcaa83b6669d667061}`

# Misc 100: (Solved)

Problem:  Broken .png file (`m100.png`)

Solution:
I utilized a bunch of tools on this problem.  First I ran `pngcheck` to see what the problem was.  
```
ERRORS DETECTED in fix.png
mainframe% pngcheck -vt7f m100.png
File: m100.png (65141 bytes)
  chunk IHDR at offset 0x0000c, length 13
    666 x 519 image, 32-bit RGB+alpha, non-interlaced
  CRC error in chunk IHDR (computed 3ff4fc62, expected 35468913)
  chunk gAMA at offset 0x00025, length 4: 0.45455
  chunk pHYs at offset 0x00035, length 9: 3780x3780 pixels/meter (96 dpi)
  chunk tEXt at offset 0x0004a, length 25, keyword: Software
    Adobe ImageReady
  chunk IDAT at offset 0x0006f, length 65010
    zlib: deflated, 32K window, fast compression
  chunk IEND at offset 0x0fe6d, length 0
ERRORS DETECTED in m100.png
```

I then did some research and found out this is a checksum error.  So I then utilized [PNGCSum](http://schaik.com/png/pngcsum.html) to fix it.
After that the picture was finally "fixed." But something appeared to be cut off.
I then edited the headers to resize it from `666x519` to `666x666`.  This revealed the text, which was crooked.
I opened the image in GNU Image Processor to change the perspective of the text.

Flag: `s1z3_d03s_ma773r_baby`
