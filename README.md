# Cesium website

A small, dependency-free static website for the Cesium project.

## Preview locally

From this directory, run:

```bash
python3 -m http.server 8000
```

Then visit http://localhost:8000.

## Publish to GitHub Pages

1. Extract the archive.
2. Copy the contents of this directory (not the enclosing directory) into the root of `jwalk117/cesium.github.io`.
3. Commit and push the changes.
4. GitHub Pages should publish the site from the repository's configured Pages source.

## Customize

- Edit page content in the HTML files.
- Edit colors, spacing, and responsive styles in `assets/site.css`.
- Edit navigation behavior in `assets/site.js`.
- Replace `assets/cesium-mark.svg` and `assets/favicon.svg` to change the mark.

The Applications dropdown currently links to Cesium OS and a general "Other projects" section. These are intentionally broad placeholders until additional Cesium suite products have names and pages.
