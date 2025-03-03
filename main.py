import os

def list_markdown_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(".md") and f not in {"template.md", "README.md"}]

def generate_readme(template_path, output_path, md_files):
    with open(template_path, "r", encoding="utf-8") as file:
        content = file.read()

    md_list = "\n".join(f"- [{file}](./{file})" for file in md_files)
    content = content.replace("{{MD_FILES_LIST}}", md_list)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    directory = "."  # Change this if your .md files are in another directory
    template_path = "template.md"
    output_path = "README.md"

    md_files = list_markdown_files(directory)
    generate_readme(template_path, output_path, md_files)

    print("README.md has been generated from template.md")
