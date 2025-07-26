#!/usr/bin/env python3
"""
Script to add copyright header to all files in the Aura Insurance Engine codebase.
"""

import os
import glob
import re
from pathlib import Path

# Copyright header text
COPYRIGHT_TEXT = """Aura Insurance Engine – Proprietary Software

Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.

This software was developed solely by Jose Reyes – full-stack engineer and designer.
Jacob Powers contributed as the licensed insurance agent for the project.
It is a modern insurance submission platform built to streamline the intake
and processing of insurance applications.

This code is proprietary and confidential. Unauthorized use, reproduction,
distribution, or modification is strictly prohibited.

Project repository: https://github.com/reyesjl/aura-insurance-engine
DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine"""

# Different comment styles for different file types
COMMENT_STYLES = {
    # C-style comments for JS/TS/Vue/CSS files
    'js_style': {
        'start': '/*\n',
        'prefix': ' * ',
        'end': ' */\n\n',
        'extensions': ['.js', '.ts', '.vue', '.css', '.scss', '.html']
    },
    # Python style comments
    'python_style': {
        'start': '#\n',
        'prefix': '# ',
        'end': '#\n\n',
        'extensions': ['.py']
    },
    # YAML/Markdown style comments
    'hash_style': {
        'start': '#\n',
        'prefix': '# ',
        'end': '#\n\n',
        'extensions': ['.yaml', '.yml']
    }
}

def get_comment_style(file_path):
    """Determine the appropriate comment style for a file."""
    ext = Path(file_path).suffix.lower()
    
    for style_name, style_info in COMMENT_STYLES.items():
        if ext in style_info['extensions']:
            return style_info
    
    # Default to JS style for unknown extensions
    return COMMENT_STYLES['js_style']

def format_header(comment_style):
    """Format the copyright header with the appropriate comment style."""
    lines = COPYRIGHT_TEXT.strip().split('\n')
    
    header = comment_style['start']
    for line in lines:
        if line.strip():
            header += comment_style['prefix'] + line + '\n'
        else:
            header += comment_style['prefix'].rstrip() + '\n'
    header += comment_style['end']
    
    return header

def file_has_copyright(file_path):
    """Check if file already has a copyright header."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(1000)  # Read first 1000 chars
            return 'Aura Insurance Engine' in content and 'Jose Reyes' in content
    except:
        return False

def should_skip_file(file_path):
    """Determine if a file should be skipped."""
    # Skip files that shouldn't have headers
    skip_patterns = [
        '__pycache__',
        '.git',
        'node_modules',
        '.vscode',
        'dist',
        'build',
        '.pyc',
        'package-lock.json',
        '.prettierrc.json',
        'db.sqlite3',
        'venv',
        'migrations',  # Django migrations
        'static',
        '.env'
    ]
    
    path_str = str(file_path)
    for pattern in skip_patterns:
        if pattern in path_str:
            return True
    
    # Skip JSON config files (but not package.json)
    if file_path.suffix == '.json' and file_path.name != 'package.json':
        return True
    
    # Skip certain auto-generated or config files
    skip_files = [
        'add_copyright_header.py',  # Skip this script itself
        'requirements.txt',
        'Dockerfile',
        'docker-compose.yml',
        'docker-compose.yaml',
        'docker-compose.dev.yaml',
        'docker-compose.prod.yaml',
        '.dockerignore',
        '.gitignore',
        'nginx.conf'
    ]
    
    if file_path.name in skip_files:
        return True
        
    return False

def add_header_to_file(file_path):
    """Add copyright header to a single file."""
    if should_skip_file(file_path):
        return False, "Skipped (excluded file type)"
    
    if file_has_copyright(file_path):
        return False, "Already has copyright header"
    
    try:
        # Read existing content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get appropriate comment style
        comment_style = get_comment_style(file_path)
        header = format_header(comment_style)
        
        # Handle special cases
        new_content = content
        
        # For Python files, preserve shebang lines
        if file_path.suffix == '.py' and content.startswith('#!'):
            lines = content.split('\n', 1)
            if len(lines) > 1:
                new_content = lines[0] + '\n\n' + header + lines[1]
            else:
                new_content = lines[0] + '\n\n' + header
        # For HTML files, add after DOCTYPE if present
        elif file_path.suffix == '.html':
            if content.strip().startswith('<!DOCTYPE'):
                lines = content.split('\n', 1)
                if len(lines) > 1:
                    new_content = lines[0] + '\n' + header + lines[1]
                else:
                    new_content = header + content
            else:
                new_content = header + content
        # For Vue files, add before template
        elif file_path.suffix == '.vue':
            new_content = header + content
        else:
            new_content = header + content
        
        # Write the updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Header added successfully"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    """Main function to process all files."""
    # Get project root
    project_root = Path(__file__).parent
    
    # File patterns to process
    patterns = [
        '**/*.py',
        '**/*.js',
        '**/*.ts',
        '**/*.vue',
        '**/*.css',
        '**/*.scss',
        '**/*.html',
        '**/*.yaml',
        '**/*.yml',
        '**/package.json'
    ]
    
    processed_files = []
    skipped_files = []
    error_files = []
    
    # Process each pattern
    for pattern in patterns:
        for file_path in project_root.glob(pattern):
            if file_path.is_file():
                success, message = add_header_to_file(file_path)
                
                if success:
                    processed_files.append(str(file_path.relative_to(project_root)))
                    print(f"✓ {file_path.relative_to(project_root)}")
                elif "Error:" in message:
                    error_files.append((str(file_path.relative_to(project_root)), message))
                    print(f"✗ {file_path.relative_to(project_root)}: {message}")
                else:
                    skipped_files.append((str(file_path.relative_to(project_root)), message))
                    print(f"- {file_path.relative_to(project_root)}: {message}")
    
    # Print summary
    print(f"\n=== Summary ===")
    print(f"Files processed: {len(processed_files)}")
    print(f"Files skipped: {len(skipped_files)}")
    print(f"Files with errors: {len(error_files)}")
    
    if error_files:
        print(f"\nErrors:")
        for file_path, error in error_files:
            print(f"  {file_path}: {error}")

if __name__ == "__main__":
    main()
