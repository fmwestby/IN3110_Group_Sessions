# RegEx Cheat Sheet

## Common Metach­ara­cters

|RegEx|Explanation|
|-|-|
|```^```|This will match from the beginning of the string|
|```[]```|A set of characters|
|```.```|Matches any alphanumeric character or symbol|
|```$```|This represents the end of the string or line|
|```{}```|Exactly the specified number of occurrences|
|```*```|Matches 0 or more times|
|```()```|Capture and group|
|```\```|Signals a special sequence (can also be used to escape special characters)|
|```+```|Matches 1 or more times|
|```\|```|Alternation / OR|
|```?```|Character match optional|

## Quanti­fiers

|RegEx|Explanation|
|-|-|
|```*```|or more|
|```+```|or more|
|```?```|0 or 1|

## Groups and Ranges

|RegEx|Explanation|
|-|-|
|```.```|Any character except new line (\n)|
|```(a\|b)```|a or b|
|```(...)```|Group|
|```(?:...)```|Passive (non-c­apt­uring) group|
|```[abc]```|Range (a or b or c)|
|```[^abc]```|Not (a or b or c)|
|```[a-q]```|Lower case letter from a to q|
|```[A-Q]```|Upper case letter from A to Q|
|```[0-7]```|Digit from 0 to 7|
|```\x```|Group/­sub­pattern number "­x"|

## Anchors

|RegEx|Explanation|
|-|-|
|```^```|Start of string, or start of line in multi-line pattern|
|```\A```|Start of string|
|```$```|End of string, or end of line in multi-line pattern|
|```\Z```|End of string|
|```\b```|Word boundary|
|```\B```|Not word boundary|
|```\<```|Start of word|
|```\>```|End of word|

## Special Characters

|RegEx|Explanation|
|-|-|
|```\n```|New line|
|```\r```|Carriage return|
|```\t```|Tab|
|```\v```|Vertical tab|
|```\f```|Form feed|
|```\xxx```||
|```\xhh```|Hex character hh|

## Character Classes

|RegEx|Explanation|
|-|-|
|```\c```|Control character|
|```\s```|White space|
|```\S```|Not white space|
|```\d```|Digit|
|```\D```|Not digit|
|```\w```|Word|
|```\W```|Not word|
|```\x```|Hexade­cimal digit|
|```\O```|Octal digit|

## Escape Sequences

|RegEx|Explanation|
|-|-|
|```\```|Escape following character|
|```\Q```|Begin literal sequence|
|```\E```|End literal sequence|

## Assertions

|RegEx|Explanation|
|-|-|
|```?=```|Lookahead assertion|
|```?!```|Negative lookahead|
|```?<=```|Lookbehind assertion|
|```?!= or ?<!```|Negative lookbehind|
|```?>```|Once-only Subexp­ression|
|```?()```|Condition [if then]|
|```?()\|```|Condition [if then else]|
|```?#```|Comment|

## References:
Python RegEx Meta Characters. (n.d.). Retrieved October 10, 2022, from https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp

Regular Expressions Cheat Sheet. (2011, October 19). Cheatography. Retrieved October 10, 2022, from https://cheatography.com/davechild/cheat-sheets/regular-expressions/