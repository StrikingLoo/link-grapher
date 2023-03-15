import re
import glob
import json
import sys

# Regular expression pattern
if len(sys.argv) > 2:
  WIKI_PATH = sys.argv[2]
else:
  WIKI_PATH = '../../dev/strikingloo.github.io/wiki'

print(WIKI_PATH)

pattern = r'\[[^\]]*\]\((/wiki/[^\s)]+)\)'

def get_wiki_name(file_path):
  last_part = file_path.split('/')[-1]
  if last_part[-3:] == ".md":
    return last_part[:-3]
  else:
    if '#' in last_part:
        return last_part[:last_part.index('#')]
    return last_part

# Find all links in the Markdown text
def get_links(file_contents):
  links = re.findall(pattern, file_contents)
  return links

link_graph = {}
for file_path in glob.glob(WIKI_PATH+'/*md'):
  print(file_path)
  with open(file_path, 'r') as f:
    contents = f.read()
    links = get_links(contents)
    link_graph[get_wiki_name(file_path)] = list(set([get_wiki_name(link) for link in links]))

json_str = json.dumps(link_graph, indent=4)
with open('output.json', 'w') as f:
  f.write(json_str)
print(json_str)
