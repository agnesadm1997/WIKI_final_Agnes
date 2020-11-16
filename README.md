# Wiki

Wiki is a Python created search engine, similair to Wikipedia, containing multiple 
template entries with educative information. An user is able to find entries, read them and save new entries or edit existing ones.

## Installation
You can download the application files here:
https://github.com/uva-webapps/wiki-agnesadm1997

To run the application you need the following required software:
- Linux
- WSL Ubuntu
- Python
- Pip, Sass abd Django
- VSCode or another similair text editor

Other required packages are:
pip3 install markdown2

## Usage

Search
Users can search for a new page by entering a search command in the search box.They can also type in wiki/"title"
directly in the https bar.

Create
Users can create a new page by pressing the create button and then filling in a title and content for the new entry in the form

Edit
Users can edit an existing page by pressing the edit button in the entries page. Then they can change the content in the text area and click create page.

Random
Users can open a random selected entry page by pressing the random button

Markdown Syntax
Each entries page markdown syntax is converted to HTML before being displayed to the user with python-markdown2. 

When you create a page you should use the following syntax described in this markdown guide: https://docs.github.com/en/free-pro-team@latest/github/writing-on-github/basic-writing-and-formatting-syntax
```
# WIKI_final_Agnes
