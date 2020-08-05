# Babylon_alternates
A simple module that adds alternates to Babylon dictionary source file.

Imagine you have a Babylon source file (.gls or .txt) in the following fromat:
header
word1 secondpart1
definition1

word2 secondpart2
definition2

word3 secondpart3 thirdpart3
definition3

word4 secondpart4
001444
....
And you want to add alternates to your dictionary so to extend search depth. Thus, it should look like this:

word1 secondpart1|word1|secondpart1
definition1

word2 secondpart2|word2|secondpart2
definition2

word3 secondpart3 thirdpart3|word3|secondpart3|thirdpart3
definition3

word4 secondpart4|word4|secondpart4
001444
...
This module will do that in a matter of seconds.
Before running the code, you should put a header in the first line of your source file! The default header is "header"!
The only dependency is pandas. You can install it on your machine by going to CMD and typing in: 
pip install pandas
