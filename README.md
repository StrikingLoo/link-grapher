# Interactive Graph maker

This program first fetches all internal links in my wiki (any links matching ()[/wiki/\*]) and then outputs the connections as a json. Using that json, I create an interactive graph that allows to see the connections between zettels, and spot the isolated ones. This generalizes to any folder full of .md files that link to each other. Though right now the regex is hardcoded to the prefix '/wiki/' this could be removed to intercept all internal links, or changed to a different prefix easily enough.

## To use
- `python3 get\_links.py WIKI_PATH`
- `python3 make\_graph.py`
