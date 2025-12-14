# Lucid Computing Landing Page

A static website for Lucid Computing, featuring a landing page, insights blog, and content managed through CloudCannon CMS.

## Overview

This repository contains the source code for the Lucid Computing website. The site showcases:
- **Landing Page** (`index.html`) - Main marketing page with hero, features, and CTA sections
- **Insights Blog** (`insights.html`) - Blog listing page displaying published articles
- **Article Pages** (`article.html`) - Individual blog post template

The site uses **Jekyll** for static site generation and is configured for deployment on **GitHub Pages**. It also supports **CloudCannon CMS** for content editing.

## Write a Blog Post

### OPTION 1: Pages CMS Editor

1. Go to https://app.pagescms.org/lucid-computing/landingpage/main/collection/blog 

2. Press "Add New Entry"

3. Create a new blog post. Content editors can use the CloudCannon interface to:
- Edit page content without touching code
- Upload and manage images
- Create and edit blog posts
- Manage blog post metadata (title, slug, date, author, tags, etc.)

4. Set `publish: true` in the frontmatter when ready to publish

### OPTION 2: Create a Markdown in your IDE


1. Create a new markdown file in `blog/posts/` with the naming convention:
   ```
   YYYY-MM-DD-post-slug.md
   ```

2. Add YAML frontmatter at the top of the file:
   ```yaml
   title: Your Post Title
   slug: your-post-slug
   date: YYYY-MM-DD
   author: Author Name
   tags:
     - Tag 1
     - Tag 2
   image: /media/image-path.png
   description: Short description for preview
   publish: true  # Set to true to publish the post
   content: |-
   # Your Post Content
   ```

3. Set `publish: true` in the frontmatter when ready to publish

## Local Development

To test the site locally with Jekyll:

```bash
# First time setup
bundle install

# Process posts and serve
make serve
# or: bundle exec jekyll serve
```

**Note:** The `make serve` command automatically processes blog posts before starting the server. The site will be available at `http://localhost:4000`

## Blog Post Fields

Each blog post supports the following frontmatter fields:

- **`title`** (string) - Post title
- **`slug`** (string) - URL-friendly identifier
- **`date`** (date) - Publication date (YYYY-MM-DD)
- **`author`** (string) - Author name
- **`tags`** (list) - Array of tag strings
- **`image`** (image) - Cover image path
- **`description`** (string) - Short description for previews
- **`publish`** (boolean) - Whether the post should be published (default: true)
- **`content`** (rich-text) - Post content (markdown) - stored in frontmatter for CMS compatibility

## How It Works

- **Jekyll** processes markdown files in `blog/posts/` automatically
- Posts with `publish: true` appear on the live site
- Content is converted from markdown to HTML during build
- GitHub Pages builds the site automatically on every push
- No manual conversion scripts needed!

