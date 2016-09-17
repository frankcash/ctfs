# "Notesy 2.0" 1: (Solved)

Problem: "Remember last year?"

Flag: `abcdefghijklmnopqrstuvwxyz`

# "Kill" Forensics 50: (Solved)

Problem: "Is kill can fix? Sign the autopsy file?"

Solution: File is a corrupted `.pcapng`.  It will not open in Wireshark or tcpdump.  File is readable in text editor.  Used `file_search.py` to find the flag.

Flag: `flag{roses_r_blue_violets_r_r3d_mayb3_harambae_is_not_kill}`


# "Warmup" PWN 50: (Attempted):

Solution: Ran `file warmup`: `warmup: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=ab209f3b8a3c2902e1a2ecd5bb06e258b45605a4, not stripped`.  Exposing a pointer that is the address of `easy`. `_gets` is taking in 0 and a pointer.

# "MFW" Web 125: (Attempted)

Problem: "Hey, I made my first website today. It's pretty cool and web7.9."

Solution: Inspect HTML, and notice possible `?/page=flag`. The site also points out how it is built with git `http://web.chal.csaw.io:8000/.git/config` is accessible.  Attempted file inclusion, but like the code shows it is not feasible.  

(Need to do an RCE `assert("file_exists('$file')") or die("That file doesn't exist!");` seems vulnerable)

Flag:
