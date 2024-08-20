# WP Export CSV Cleaner

When using WP Export All plugin if a list of IDs are exported, for example a list of associated people to a post, the list of IDs is formatted in the following: `"";i:1;s:1:""` between each ID, this makes re-importing that data problematic. 

This python script will loop through each line of a CSV and replace those with a `|` delimator.

i: Is a reference to the index in the list
s: Is how long the ID length is