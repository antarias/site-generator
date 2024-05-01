from functions_blocks import *
from functions_gencontent import *

def main():
    #generate_page("content/index.md", "content/template.html", "public/index.html")
    generate_pages_recursive("content", "content/template.html", "public")
    
main()