# "Notesy 2.0" 1: (Solved)

Problem: "Remember last year?"

Flag: `abcdefghijklmnopqrstuvwxyz`

# "Kill" Forensics 50: (Solved)

Problem: "Is kill can fix? Sign the autopsy file?"

Solution: File is a corrupted `.pcapng`.  It will not open in Wireshark or tcpdump.  File is readable in text editor.  Used `file_search.py` to find the flag.

Flag: `flag{roses_r_blue_violets_r_r3d_mayb3_harambae_is_not_kill}`


# "MFW" Web 125: (Attempted)

Problem: "Hey, I made my first website today. It's pretty cool and web7.9."

Solution: Inspect HTML, and notice possible "?/page=flag".

Flag:
