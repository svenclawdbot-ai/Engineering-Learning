# Engineering Research Journal

A Jekyll-based research blog for documenting daily engineering challenges, deep dives, and technical explorations.

## Quick Start

### 1. Create GitHub Repository

1. Go to https://github.com/new
2. Name: `engineering-research-journal` (or your preference)
3. Make it **Public** (for free GitHub Pages hosting)
4. Don't initialize with README (we have our own)

### 2. Push This Repository

```bash
cd /home/james/.openclaw/workspace/research-blog

# Initialize git
git init
git add .
git commit -m "Initial commit: Research journal setup"

# Add remote (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/engineering-research-journal.git

# Push to GitHub
git push -u origin main
```

### 3. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages**
3. Source: Deploy from a branch
4. Branch: **main** / **root**
5. Click **Save**

Your site will be live at: `https://USERNAME.github.io/engineering-research-journal`

## Daily Workflow

### Creating a New Research Post

1. Create a new file in `_posts/` with format: `YYYY-MM-DD-title.md`

2. Use this template:

```markdown
---
layout: post
title: "Your Research Title"
date: YYYY-MM-DD HH:MM:SS +0000
topic: "Topic Category"
tags: [tag1, tag2, tag3]
summary: "Brief summary of the research"
references:
  - author: "Author Name"
    year: 2024
    title: "Paper Title"
    journal: "Journal Name"
    url: "https://doi.org/..."
---

Your research content here...
```

3. Commit and push:

```bash
git add _posts/YYYY-MM-DD-title.md
git commit -m "Add research: Title"
git push
```

GitHub Pages will automatically rebuild your site (takes 1-2 minutes).

## Directory Structure

```
research-blog/
├── _config.yml              # Site configuration
├── _layouts/                # HTML templates
│   ├── default.html
│   ├── post.html
│   └── home.html
├── _posts/                  # Research posts (YYYY-MM-DD-title.md)
├── _includes/               # Reusable components
├── assets/
│   ├── css/
│   │   └── style.css       # Site styling
│   └── images/             # Images and figures
├── papers/                 # Static pages for extended papers
├── index.md                # Homepage
├── archive.md              # Post archive by date
└── about.md                # About page
```

## Features

- **Date-organized posts** — Automatic chronological sorting
- **Topic tagging** — Filter by research area
- **Reference management** — Built-in bibliography support
- **Syntax highlighting** — For code and equations
- **Mobile responsive** — Works on all devices
- **SEO optimized** — Automatic meta tags

## Customization

### Change Site Title/Description

Edit `_config.yml`:
```yaml
title: "Your Research Journal"
description: "Your description here"
author: "Your Name"
```

### Add New Topics

Topics are just tags. Add them to any post:
```yaml
tags: [thermal-systems, materials, robotics]
```

### Add Mathematical Equations

Use LaTeX-style math with MathJax (requires plugin) or just code blocks:

```
$$q_{CHF} = 0.131 \times h_{fg} \times \rho_v^{0.5}$$
```

To enable MathJax, add to `_config.yml`:
```yaml
plugins:
  - jekyll-mathjax
```

## Local Development (Optional)

If you want to preview changes locally:

```bash
# Install Jekyll
gem install bundler jekyll

# Install dependencies
cd research-blog
bundle init
bundle add jekyll

# Serve locally
bundle exec jekyll serve

# Visit http://localhost:4000
```

## Backup Strategy

Your content is automatically backed up to GitHub. For additional safety:

1. The repository is cloned locally in `/home/james/.openclaw/workspace/research-blog/`
2. Git history preserves all versions
3. You can download ZIP from GitHub anytime

## Questions?

- Jekyll docs: https://jekyllrb.com/docs/
- GitHub Pages: https://pages.github.com/
- Markdown guide: https://www.markdownguide.org/
