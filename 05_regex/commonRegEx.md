# Common Regular Expressions

Match an IP Address:

```
\b\d{1,3}\.\d{1,3}\.\d{1,3}\b
```

Match a Duplicated Word:

```
\b(\w+)\s+\1\b
```

Match a Word Near Itself:

```
\b(word1|word2|word3)(?:\W+\w+){1,6}?\W+(word1|word2|word3)\b
```

Match a Valid Date on format MM/DD/YYYY:

```
^(0[1–9]|1[012])[- /.](0[1–9]|[12][0–9]|3[01])[- /.](19|20)\d\d$
```

Match a Valid Date on format MM-DD-YYYY:

```
^(19|20)\d\d[- /.](0[1–9]|1[012])[- /.](0[1–9]|[12][0–9]|3[01])$
```

Match a URL:
```
^((http[s]?|ftp):\/)?\/?([^:\/\s]+)((\/\w+)*\/)([\w\-\.]+[^#?\s]+)(.*)?(#[\w\-]+)?$
```

Match a URL Slug:

*(A slug is the part that comes at the very end of a URL and refers to a specific page or post)*

```
^[a-z0–9-]+$
```

Match a Strong Password which:
* A minimum of 6 characters
* At least one uppercase
* At least one lowercase
* At least one digit
* Should contain other characters

```
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,}$
```

Match an HTML Tag:

*(keywords which defines that how web browser will format and display the content)*

```
^<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)$
```

Match a Username:

```
^[a-z0–9_-]{3,16}$
```

Match a Positive Integer Number:

```
\b\d+\b
```

Match a Single-Line String:

```
“[^”\r\n]*”
```

Match a Single-Line Comment:

```
#.*$
```

Match an Email Address:

```
\b[A-Za-z0–9._%+-]+@[A-Za-z0–9.-]+\.[A-Za-z]{2,}\b
```

## References:
Johnson, S. (2021, December 7). REGULAR EXPRESSION FOR DUMMIES - Syd Johnson. Medium. Retrieved October 10, 2022, from https://medium.com/@sydcjohnson/regular-expression-for-dummies-1062e5d74b7a