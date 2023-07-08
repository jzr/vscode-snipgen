# Generate VS code snippets

Generate snippets for VS Code from templates.  
It deals with escaping special characters and line breaks.

## Usage

Create your templates in _templates/_ as _prefix.md_.  
You can use [VS Code placeholders](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_placeholders) in the templates.  

Run `python3 generate-snippets.py`.  

The snippets are generated in the current workspace. You can copy the file to your user profile if you prefer.
