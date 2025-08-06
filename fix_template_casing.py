import os

TEMPLATE_DIR = 'app/templates'  # Adjust path if needed
FILES_EXTENSIONS = ['.html', '.htm', '.jinja2']  # common template extensions

def fix_casing_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('Base.html', 'base.html').replace('Navbar.html', 'navbar.html')

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed casing in: {file_path}")

def main():
    for root, dirs, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if any(file.endswith(ext) for ext in FILES_EXTENSIONS):
                fix_casing_in_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
