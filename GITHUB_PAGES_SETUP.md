# GitHub Pages Setup Instructions

This document explains how to complete the GitHub Pages setup after merging this PR.

## Automatic Setup

Once this PR is merged to the main/master branch, the GitHub Actions workflow will automatically:
1. Build the Jekyll site from the markdown files
2. Deploy it to GitHub Pages

## Manual Steps Required

After merging, you need to enable GitHub Pages in the repository settings:

### Step 1: Go to Repository Settings
1. Navigate to https://github.com/wongallan/dingding
2. Click on "Settings" tab
3. Scroll down to "Pages" in the left sidebar

### Step 2: Configure GitHub Pages Source
1. Under "Build and deployment"
2. Set **Source** to "GitHub Actions" (not "Deploy from a branch")
3. This will allow the workflow to deploy automatically

### Step 3: Wait for Deployment
1. After merging the PR, the workflow will run automatically
2. Go to the "Actions" tab to monitor the deployment
3. Once complete, your site will be available at:
   **https://wongallan.github.io/dingding/**

## What's Been Set Up

This PR includes:

1. **Jekyll Configuration** (`_config.yml`)
   - Configured with the minimal theme
   - Set baseurl to `/dingding`
   - Set URL to `https://wongallan.github.io`

2. **GitHub Actions Workflow** (`.github/workflows/pages.yml`)
   - Automatically builds and deploys on push to main/master
   - Uses official GitHub Pages actions

3. **Landing Pages**
   - Root `index.md` - Main entry point
   - `booklet/index.md` - Booklet home page with navigation
   - `booklet/script/index.md` - Script index with links to all scenes

4. **Navigation Structure**
   - All pages now have navigation links
   - Easy to browse between sections
   - Back links for easy navigation

5. **README.md**
   - Documents the live URL
   - Explains the structure
   - Includes local development instructions

## Troubleshooting

If the site doesn't appear after deployment:

1. **Check Workflow Status**
   - Go to Actions tab
   - Look for "Deploy Jekyll site to Pages" workflow
   - Check if it completed successfully

2. **Verify Pages Settings**
   - Settings → Pages
   - Ensure Source is set to "GitHub Actions"
   - Check that the deployment shows as "Active"

3. **Clear Browser Cache**
   - GitHub Pages may take a few minutes to update
   - Try a hard refresh (Ctrl+F5 or Cmd+Shift+R)

## Sharing the Link

Once deployed, you can share:
- **Main page:** https://wongallan.github.io/dingding/
- **Booklet:** https://wongallan.github.io/dingding/booklet/
- **Specific scene:** https://wongallan.github.io/dingding/booklet/script/scene-01.md

The links will work in any modern web browser, and the content will be formatted nicely with the Jekyll theme.
