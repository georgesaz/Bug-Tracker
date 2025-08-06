import os
import re

TEMPLATE_DIR = 'app/templates'

def find_case_issues():
    # Regex to find extends/include statements with filenames
    pattern = re.compile(r'{%\s*(extends|include)\s*[\'"]([^\'"]+)[\'"]\s*%}')

    # Collect all actual template filenames in lowercase for comparison
    actual_files = {f.lower() for f in os.listdir(TEMPLATE_DIR)}

    issues = []

    for root, _, files in os.walk(TEMPLATE_DIR):
        for file in files:
            if not file.endswith('.html'):
                continue
            filepath = os.path.join(root, file)
            with open(filepath, encoding='utf-8') as f:
                content = f.read()
            matches = pattern.findall(content)
            for tag, filename in matches:
                # Check if filename lowercase exists in actual files
                filename_lower = filename.lower()
                if filename_lower not in actual_files:
                    issues.append((filepath, tag, filename, 'File not found'))
                else:
                    # Check if casing matches exactly
                    # get real filename
                    real_filename = next((f for f in os.listdir(TEMPLATE_DIR) if f.lower() == filename_lower), None)
                    if real_filename and real_filename != filename:
                        issues.append((filepath, tag, filename, f'Casing mismatch, should be "{real_filename}"'))

    if issues:
        print('Potential casing issues found:')
        for filepath, tag, filename, issue in issues:
            print(f'{filepath}: {tag} references "{filename}" - {issue}')
    else:
        print('No casing issues found.')

if __name__ == '__main__':
    find_case_issues()
