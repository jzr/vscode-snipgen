import json
from pathlib import Path

template_dir = Path("templates/")
templates = template_dir.glob("*.md")

snippets = {}

for template in templates:
    with open(template) as template_file:
        template_name = template.stem
        template_body = template_file.read().splitlines()

        snippets[template_name] = {"prefix": template_name, "body": template_body}


snippets_dir = Path(".vscode/")
snippets_dir.mkdir(exist_ok=True)

snippets_path = snippets_dir / "markdown.code-snippets"

with open(snippets_path, "w") as f:
    json.dump(snippets, f, indent=2)
