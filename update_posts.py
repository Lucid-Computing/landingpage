#!/usr/bin/env python3
"""
Script to update blog/posts.json with published blog posts.
Adds any post where 'publish' is true in the frontmatter if it doesn't already exist.
Pure Python - no external dependencies.
"""

import os
import json
import re
from pathlib import Path


def parse_yaml_value(value_str):
    """Parse a YAML value string into Python type."""
    value_str = value_str.strip()
    
    # Handle quoted strings
    if (value_str.startswith('"') and value_str.endswith('"')) or \
       (value_str.startswith("'") and value_str.endswith("'")):
        return value_str[1:-1]
    
    # Handle booleans
    if value_str.lower() in ('true', 'yes', 'on'):
        return True
    if value_str.lower() in ('false', 'no', 'off'):
        return False
    
    # Handle numbers
    try:
        if '.' in value_str:
            return float(value_str)
        return int(value_str)
    except ValueError:
        pass
    
    # Default to string
    return value_str


def parse_yaml_frontmatter(frontmatter_text):
    """Parse simple YAML frontmatter into a dictionary."""
    result = {}
    lines = frontmatter_text.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Skip empty lines
        if not line.strip():
            i += 1
            continue
        
        # Handle key-value pairs
        if ':' in line and not line.strip().startswith('#'):
            parts = line.split(':', 1)
            key = parts[0].strip()
            value_str = parts[1].strip() if len(parts) > 1 else ''
            
            # Check if next line starts a list (indented with -)
            if i + 1 < len(lines) and (lines[i + 1].strip().startswith('- ') or 
                                       (lines[i + 1].startswith('  - ') and not lines[i + 1].startswith('   '))):
                # This is a list
                current_list = []
                i += 1
                while i < len(lines):
                    list_line = lines[i].rstrip()
                    if list_line.startswith('  - ') or list_line.startswith('- '):
                        list_item = list_line.split('- ', 1)[1].strip()
                        # Remove quotes if present
                        if (list_item.startswith('"') and list_item.endswith('"')) or \
                           (list_item.startswith("'") and list_item.endswith("'")):
                            list_item = list_item[1:-1]
                        current_list.append(list_item)
                        i += 1
                    elif list_line.startswith('  ') and not list_line.startswith('   '):
                        # Continuation of list item (multiline)
                        current_list[-1] += ' ' + list_line.strip()
                        i += 1
                    else:
                        break
                result[key] = current_list
                continue
            elif value_str.startswith('|') or value_str.startswith('>') or value_str.startswith('|-'):
                # Multiline string (literal or folded)
                multiline_content = []
                i += 1
                while i < len(lines):
                    multiline_line = lines[i]
                    # Check if this is the start of a new key (has colon and proper indentation)
                    if ':' in multiline_line and not multiline_line.startswith(' ') and not multiline_line.startswith('\t'):
                        break
                    multiline_content.append(multiline_line)
                    i += 1
                result[key] = '\n'.join(multiline_content).rstrip()
                continue
            elif value_str == '':
                # Empty value - might be a list starting on next line
                if i + 1 < len(lines) and lines[i + 1].strip().startswith('- '):
                    # Handle as list (code above will catch it)
                    result[key] = []
                else:
                    result[key] = ''
            else:
                # Regular key-value
                value = parse_yaml_value(value_str)
                result[key] = value
        
        i += 1
    
    return result


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown file."""
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if not match:
        return None, content
    
    frontmatter_text = match.group(1)
    markdown_content = match.group(2)
    
    try:
        frontmatter = parse_yaml_frontmatter(frontmatter_text)
        return frontmatter, markdown_content
    except Exception as e:
        print(f"Error parsing YAML frontmatter: {e}")
        return None, content


def markdown_to_html(markdown_text):
    """Convert markdown to HTML using basic regex patterns."""
    html = markdown_text
    
    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^##### (.+)$', r'<h5>\1</h5>', html, flags=re.MULTILINE)
    html = re.sub(r'^###### (.+)$', r'<h6>\1</h6>', html, flags=re.MULTILINE)
    
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'__(.+?)__', r'<strong>\1</strong>', html)
    
    # Italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'_(.+?)_', r'<em>\1</em>', html)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Images
    html = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', html)
    
    # Code blocks (fenced)
    html = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    
    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Blockquotes
    lines = html.split('\n')
    result_lines = []
    in_blockquote = False
    
    for line in lines:
        if line.strip().startswith('>'):
            if not in_blockquote:
                result_lines.append('<blockquote>')
                in_blockquote = True
            result_lines.append('<p>' + line.strip()[1:].strip() + '</p>')
        else:
            if in_blockquote:
                result_lines.append('</blockquote>')
                in_blockquote = False
            if line.strip():
                result_lines.append('<p>' + line + '</p>')
            else:
                result_lines.append('')
    
    if in_blockquote:
        result_lines.append('</blockquote>')
    
    html = '\n'.join(result_lines)
    
    # Lists (unordered)
    html = re.sub(r'^[\*\-\+] (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Lists (ordered)
    html = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Paragraphs (wrap consecutive non-empty lines)
    # This is a simplified version - full markdown parsing would be more complex
    
    return html


def load_posts_json(posts_json_path):
    """Load existing posts.json file."""
    if os.path.exists(posts_json_path):
        with open(posts_json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"posts": []}


def post_exists(posts, slug):
    """Check if a post with the given slug already exists."""
    return any(post.get('slug') == slug for post in posts)


def create_post_entry(frontmatter, markdown_content):
    """Create a post entry for posts.json from frontmatter and content."""
    # Convert markdown content to HTML
    html_content = markdown_to_html(markdown_content)
    
    # Extract first paragraph or heading for description if not provided
    description = frontmatter.get('description', '')
    if not description and markdown_content:
        # Try to extract first paragraph
        first_para = re.search(r'^([^\n]+)', markdown_content.strip(), re.MULTILINE)
        if first_para:
            description = first_para.group(1)[:200]  # Limit to 200 chars
    
    # Handle tags - convert single value to list if needed
    tags = frontmatter.get('tags', [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []
    
    post = {
        "title": frontmatter.get('title', ''),
        "slug": frontmatter.get('slug', ''),
        "date": frontmatter.get('date', ''),
        "author": frontmatter.get('author', ''),
        "tags": tags,
        "image": frontmatter.get('image', ''),
        "description": description,
        "content": html_content
    }
    
    return post


def update_posts_json():
    """Main function to update posts.json with published posts."""
    posts_dir = Path('blog/posts')
    posts_json_path = Path('blog/posts.json')
    
    if not posts_dir.exists():
        print(f"Error: {posts_dir} directory not found")
        return
    
    # Load existing posts
    posts_data = load_posts_json(posts_json_path)
    existing_posts = posts_data.get('posts', [])
    
    # Get all markdown files
    markdown_files = list(posts_dir.glob('*.md'))
    
    added_count = 0
    skipped_count = 0
    
    for md_file in markdown_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, markdown_content = parse_frontmatter(content)
        
        if not frontmatter:
            print(f"Warning: Could not parse frontmatter in {md_file.name}")
            continue
        
        # Check if publish is true (handle both boolean and string)
        publish = frontmatter.get('publish', False)
        if isinstance(publish, str):
            publish = publish.lower() in ('true', '1', 'yes', 'on')
        if not publish:
            continue
        
        slug = frontmatter.get('slug', '')
        if not slug:
            print(f"Warning: Post {md_file.name} has publish=true but no slug")
            continue
        
        # Check if post already exists
        if post_exists(existing_posts, slug):
            skipped_count += 1
            continue
        
        # Create new post entry
        new_post = create_post_entry(frontmatter, markdown_content)
        existing_posts.append(new_post)
        added_count += 1
        print(f"Added post: {new_post['title']} ({slug})")
    
    # Sort posts by date (newest first)
    existing_posts.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    # Write updated posts.json
    posts_data['posts'] = existing_posts
    with open(posts_json_path, 'w', encoding='utf-8') as f:
        json.dump(posts_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nSummary: Added {added_count} new post(s), skipped {skipped_count} existing post(s)")


if __name__ == '__main__':
    update_posts_json()
