# igfasouza.com — blog archive

Published at **[igfasouza.github.io/old-igfasouza-blog](https://igfasouza.github.io/old-igfasouza-blog/)**.

Static rebuild of my old WordPress blog at [igfasouza.com/blog](https://www.igfasouza.com/blog/),
converted to Markdown and served by [Quarkus Roq](https://iamroq.dev/).

This project is a **backup / archive**. The WordPress site is no longer maintained
and this repository preserves the posts as they were, plus a fresh landing page.
Layout or formatting glitches may still show up here and there.

Last content update: **15/07/2026**

## Stack

- **Quarkus 3.37** with the [Roq](https://iamroq.dev/) static site framework
- **Java 25** (via [mise](https://mise.jdx.dev/))
- **Maven 3.9+** (also managed by mise)
- Tailwind + esbuild via `quarkus-roq-theme-default` (mvnpm bundling)

## Layout

```
content/
  index.html          Landing page (bio + social links + link to /posts/)
  posts.html          Blog index — grid of post cards at /posts/
  posts/              One Markdown file per post
  404.html
data/
  authors.yml
  menu.yml
public/
  images/             Static assets (mirrors the old /wp-content/uploads/ tree)
src/main/resources/
  application.properties
  templates/
    partials/roq-default/
      head.html               Overrides theme head (adds Google Fonts + bg image)
      sidebar-about.html      Empty (theme sidebar is hidden)
      sidebar-contact.html    Empty
      sidebar-copyright.html  Empty
    layouts/
      links-post.html         Custom layout for posts with a list of external links
web/
  _custom.css         Site styles (Hiero-inspired: black/white + red accent, Yanone Kaffeesatz)
```

## Running locally

Requires Java 25 and Maven 3.9+. If you use mise, both are pinned in `mise.toml`
and `.config/mise/config.toml`.

```bash
mvn quarkus:dev
```

The site is served at http://localhost:8080/.

The **first run** downloads a lot of `mvnpm` artifacts (npm packages published to Maven
Central via mvnpm.org) — including Tailwind, esbuild plugins and platform-native binaries.
Expect it to take several minutes. Subsequent runs use the local `~/.m2/repository` cache
and start in a few seconds.

### Custom Maven repository

`pom.xml` declares the [mvnpm.org](https://mvnpm.org/) repository — required for the
web-bundler / Tailwind CSS extensions used by the Roq default theme. It is set at the
project level so no global `~/.m2/settings.xml` change is needed.

## Content

### Adding a regular post

Create a Markdown file in `content/posts/` named `YYYY-MM-DD-slug.md`:

```yaml
---
layout: post
title: "Post title"
date: '2026-01-15'
slug: my-post-slug
tags:
  - Java
  - Kafka
description: "Short description that appears on cards and social previews."
image: wp/2026/01/cover.jpg   # relative to public/images/, NOT starting with /images/
---

Content in Markdown here.
```

**Important:** the frontmatter `image:` field is resolved relative to `public/images/`,
so use `wp/2026/01/cover.jpg`, **not** `/images/wp/2026/01/cover.jpg`. Inline `![]()`
image references inside the body still use the absolute `/images/...` path since they
are served at runtime.

### Adding a link-list post

Uses the custom layout at `src/main/resources/templates/layouts/links-post.html`:

```yaml
---
layout: links-post
title: "Title"
description: "Description"
image: "foo.jpg"
links:
  - title: "A link"
    url: "https://example.com"
    description: "Optional description"
    image: "https://example.com/logo.png"
---
```

## Theme customization

The Roq default theme is loaded from `io.quarkiverse.roq:quarkus-roq-theme-default:2.1.4`.
It ships a sidebar with about / menu / contact / copyright partials that expect fields
in `site.data.*` (`name`, `simple-name`, etc.). This project overrides them with empty
templates under `src/main/resources/templates/partials/roq-default/` and hides the
sidebar entirely via CSS (`.sidebar.main { display: none }`), because the site does not
use that sidebar layout.

The tiled background image (`public/images/bg01.jpg`) is applied only to the home page
via a `<style>` block in `head.html` scoped to `.wrapper.home-page`. Keeping the URL
outside `_custom.css` avoids esbuild trying to resolve it as a bundled asset.

## Deploy — GitHub Pages

The site is rebuilt and published automatically on every push to `main` via the
workflow at [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

### One-time setup for the repository

1. **Push the repo** to GitHub (default branch `main`).
2. **Enable Pages** — go to `Settings → Pages`, set **Source** to **GitHub Actions**
   (not "Deploy from a branch"). No branch selection needed with this source.
3. **Check the site URL** — the workflow assumes the site will be served at
   `https://<user>.github.io/<repo>/`. The current value is set in
   [`src/main/resources/application.properties`](src/main/resources/application.properties):
   ```
   quarkus.roq.site-url=https://igfasouza.github.io/old-igfasouza-blog
   ```
   If your repo has a different name, or you are publishing to a custom domain,
   change that URL accordingly.
4. **Push to `main`** — the workflow runs, builds the static site via
   `quarkiverse/quarkus-roq@v1.1`, and deploys to Pages.

The first run takes a while because Maven downloads every mvnpm artifact from
scratch. Subsequent runs hit the cached `~/.m2/repository` (via `actions/cache`)
and complete in a couple of minutes.

### Build only (no deploy)

```bash
mvn install
```

Produces the fully-rendered static site under `target/roq/` (or `target/generated-site/`
depending on the Roq version) — ready to publish anywhere (S3, Netlify, Cloudflare Pages,
plain `nginx`, etc.).

## License

MIT
