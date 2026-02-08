import os

files = [
    'core/trinity_core.py',
    'core/evolution_protocol.py'
]

for file_path in files:
    if not os.path.exists(file_path):
        print(f"Skipping {file_path} (not found)")
        continue
        
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace problematic unclosed string pattern
    new_content = content.replace('\\\"\"\"', '\"\"\"')
    
    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Fixed syntax errors in {file_path}")
    else:
        print(f"ℹ️ No syntax errors found in {file_path}")
