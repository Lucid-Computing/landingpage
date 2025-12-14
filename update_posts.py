#!/usr/bin/env python3
"""
Script to update blog/posts.json with published blog posts.
Adds any post where 'publish' is true in the frontmatter if it doesn't already exist.
"""

import os
import json
import re
import yaml
from pathlib import Path

try:
    import markdown
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False
    print("Warning: markdown library not found. Content will be stored as raw markdown.")


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown file."""
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if not match:
        return None, content
    
    frontmatter_text = match.group(1)
    markdown_content = match.group(2)
    
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        return frontmatter, markdown_content
    except yaml.YAMLError as e:
        print(f"Error parsing YAML frontmatter: {e}")
        return None, content


def markdown_to_html(markdown_text):
    """Convert markdown to HTML."""
    if HAS_MARKDOWN:
        md = markdown.Markdown(extensions=['extra', 'codehilite'])
        return md.convert(markdown_text)
    else:
        # Fallback: return markdown as-is (or could do basic conversion)
        return markdown_text


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
    
    post = {
        "title": frontmatter.get('title', ''),
        "slug": frontmatter.get('slug', ''),
        "date": frontmatter.get('date', ''),
        "author": frontmatter.get('author', ''),
        "tags": frontmatter.get('tags', []),
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
