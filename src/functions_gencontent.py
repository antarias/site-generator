import re
import os
from pathlib import Path
from functions_blocks import *

# extract_title(markdown)
#   Grab the text of the h1 header from the markdown file (The line that starts with a single #) and return it. 
#   If there is no h1 header, raise an exception. All pages need a single h1 header.                
def extract_title(markdown):
    pattern = r"^# (.*)$"
    match = re.search(pattern, markdown, flags=re.MULTILINE)
    if match == None:
        raise Exception("No title found")
    return match.group(1)

# generate_page(from_path, template_path, dest_path)
def generate_page(from_path, template_path, dest_path):
    print (f"  Generating page from {from_path} to {dest_path} using {template_path}")    
    # Get input files
    from_md_text = None
    with open(from_path, "r") as f:
        from_md_text = f.read()
    template_text = None
    with open(template_path, "r") as f:
        template_text = f.read()
    if (from_md_text == None or template_text == None):
        raise (Exception("Ficheros no encontrados"))
    # Prepare html
    content = markdown_to_html_node(from_md_text).to_html()
    title = extract_title(from_md_text)
    html = template_text
    html = html.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)
    #print (html)
    # Write html
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html)

# generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
def generate_pages_recursive(content_dir_path, template_path, dest_dir_path):
    print (f"Generating recursively all pages from {content_dir_path} to {dest_dir_path} using {template_path}")
    # Convert to Path objects
    content_dir = Path(content_dir_path)
    dest_dir    = Path(dest_dir_path)
    # Crawl content dir
    contents = os.listdir (content_dir)
    for content in contents:
        content_path = content_dir / content
        if content_path.is_file():
            if content_path.suffix == ".md":
                #print (f"MD File: {content_path}")
                dest_path = dest_dir / (content.split('.')[0] + ".html")
                generate_page(content_path, template_path, dest_path)
        if content_path.is_dir():
            #print (f"Dir : {content_path}")
            # If directory, recurse it
            generate_pages_recursive (content_path, template_path, dest_dir / content)
        
    