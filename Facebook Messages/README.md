# Facebook Messages

Generates plots of user word count and generates simulated user messages based off of user's previous messages.

![](data/example_wordcount_chart.jpg)

Example usage:

```
# Simulate entire chat and generate alaised charts
# May be slow if large chats are simulated
# Do not include spaces between 1.html and 2.html
python process_all.py 1.html,2.html --simulate True --alias True

# Simulate single user and generate non-aliased charts
# Use underscores for spaces in names
python process_all.py 1.html --simulate True --user insert_name
```