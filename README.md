# Ding Ding Magic

This repository contains the booklet for **Ding Ding Magic**, a children's musical.

## View Online

The booklet is published on GitHub Pages and can be accessed at:

**https://wongallan.github.io/dingding/**

## Contents

The booklet includes:
- Overview and show details
- Character guide
- Scene synopsis
- Full script (9 scenes) with Chinese dialogue, Sidney Lau romanization, and English translation

## Local Development

The site uses Jekyll for GitHub Pages. To view locally:

```bash
# Install Jekyll (if not already installed)
gem install bundler jekyll

# Serve the site locally
jekyll serve

# Visit http://localhost:4000/dingding/ in your browser
```

## Repository Structure

- `booklet/` - Main content directory
  - `index.md` - Landing page
  - `overview.md` - Plot synopsis and show details
  - `characters.md` - Character guide
  - `scene-synopsis.md` - Scene summaries
  - `script/` - Full script files by scene
- `_config.yml` - Jekyll configuration
- `.github/workflows/pages.yml` - GitHub Actions workflow for deployment

## Publishing

The site is automatically deployed to GitHub Pages when changes are pushed to the main/master branch.
