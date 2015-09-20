#CSAW Qualifiers 2015 File Dump

#Forensics 100: Transfer (Solved)

Utilized [Wireshark](https://www.wireshark.org/). Applied the filter `http and !http.host==google.com and !http.host==www.google.com`.  
Revealed packet 60.  Upon further investigating of that packet it's a python script.  
If you analyze the python script you see that they're randomly choosing an encryption method.  If you reverse the steps you can easily reveal the flag.

#Trivia 100: Trivia 1 (Solved)

Was a type of Rat.  

#Forensics 200: Airport (Attempted)

Was investigating using [steghide](http://steghide.sourceforge.net/).  The `steghide.jpg` lead me to this software after a quick DuckDuckGo search.
`[1-4].png` are troublesome with steghide.  I tried and failed to open `steghide.jpg` using `steghide info steghide.jpg`.
I then resorted to looking at it in hex and used [Bless Hex Editor](http://home.gna.org/bless/). No progress was made.

#Forensics 150: Pcapin (Attempted)

lolnope.jpg
