import os

def check_templates(template_names, base_folder='app/templates'):
    missing = []
    for template in template_names:
        path = os.path.join(base_folder, template)
        if not os.path.isfile(path):
            missing.append(template)
    return missing

if __name__ == '__main__':
    templates_to_check = [
        'login.html',
        'register.html',
        'index.html',
        # add other templates you use here
    ]

    missing_templates = check_templates(templates_to_check)

    if missing_templates:
        print("❌ Missing templates:")
        for t in missing_templates:
            print(f" - {t}")
    else:
        print("✅ All templates found!")
