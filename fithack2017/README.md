# Fit Hack 2017

## Trivia1 (MISC 10):

Problem: A bug found in bash causes arbitrary code to be executed remotely

Answer: `FIT{SHELLSHOCK}`

## Trivia2 (MISC 10):

Problem: A dog breed that exists in Version 3.0 of SSL.

Answer: `FIT{POODLE}`

## Trivia3 (MISC 10):

Problem: VyOS 1.0.0 - 1.0.5

Answer: `FIT{HYDROGEN}`

## Look Quickly (Web 50):

Problem: It's not food.

There is a link provided that loads a web page with a picture of cookies.  If you look at the cookies in the web request you get the flag.

Answer: `FIT{I7_i5_n07_4_c00ki3_t0_3a7}`

## Get (Web 50):

Problem: Get...

This problem includes a zip file with a PCAP in it.  The PCAP has a `/GET/` Request.  Within the header of the `/GET/` there is an authorization header with a base64 encrypted value.  I put the value into the JavaScript console and ran `atob(Zml0aGFjazpGSVR7MzMyZHJlZjNhNWc3aH0=)`.  This yields the flag `fithack:FIT{332dref3a5g7h}`

Solution: `FIT{332dref3a5g7h}`

## 100 Count ( Web 100):

Problem: may be....sumtion?

The included link leads to a web site asking you to complete simple addition 100 times.  This site has two cookies: `count` and `rand_add`.  Count is the current amount of success previous adds, whereas Rand_add is the answer to the addition.  By changing `count` to 100 and then submitting one more addition the flag will load.  

Solution: `FIT{fsaewiwe}`
