Should contain files:

* names.txt
* aliases.txt
* HTML file downloaded from Facebook data containing chatlog

names.txt

* How they are identified by facebook, e.g. if user1="John Doe", alt1 might be "100000XXXXXXXXX@facebook.com" which is their messenger id. Optionally, including just the name without alts is fine also.

```
user1: alt1, alt2, etc  
user2: alt1  
user3  
user4: alt1, alt2, alt3, etc  
```

aliases.txt

* How they are identified/referred to in chat, e.g. if user1="John Doe", nickname1 might be "John". One of the nicknames must be the user identifier from names.txt. An alias must be specified for each user; to disable aliasing completely, use the user's real name as their alias. 
```
alias1: user1, nickname1, nickname2, etc  
alias2: user2, nickname1  
alias3: user3, nickname1, nickname2, nickname3, etc  
```

Generated files/graphs will also be output to this directory.