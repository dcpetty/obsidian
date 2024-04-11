---
title: "What I learned about Obsidian & Jekyll"
date: 2024-03-18 15:48:12
last_modified_at: 2024-04-11 19:39:52
show_date: true
permalink: /obsidian-jekyll/obsidianjekyll/
tags:
- Jekyll
- Obsidian
toc: true
toc_sticky: true
category: ObsidianJekyll
---
## How Obsidian works as a linking Markdown editor

- Obsidian has `.md` files in a [normal format](https://www.markdownguide.org/tools/obsidian/) that are shown as **Notes** without the `.md`.
- Obsidian allows for nested notes within subdirectories.
- Obsidian allows for Wiki-style links (credits to [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham) & [https://wiki.c2.com/](https://wiki.c2.com/)) of the form `[[ObsidianJekyll]]` to link to this note. As long as there are not duplicate filenames, `[[SubDirectoryNote]]` can refer to [obsidian/TestPages/SubFolder/SubDirectoryNote](obsidian/TestPages/SubFolder/SubDirectoryNote) in a subdirectory.
  - Under `Obsidian > Settings > Files and links` with `Use [[Wikilinks]]` enabled...
   - With `Files and links > New link format > Relative path to file`, [obsidian/TestPages/AdditionalNote](obsidian/TestPages/AdditionalNote) shows as `[[AdditionalNote]]` when entered Wiki-style, whereas [obsidian/TestPages/SubFolder/AdditionalNote|AdditionalNote](obsidian/TestPages/SubFolder/AdditionalNote|AdditionalNote) shows as `[[SubFolder/AdditionalNote|AdditionalNote]]` when entered Wiki-style.
   - With `Files and links > New link format > Absolute path in vault`, [obsidian/TestPages/AdditionalNote|AdditionalNote](obsidian/TestPages/AdditionalNote|AdditionalNote) shows as `[[obsidian/AdditionalNote|AdditionalNote]]` when entered Wiki-style, whereas [obsidian/TestPages/SubFolder/AdditionalNote|AdditionalNote](obsidian/TestPages/SubFolder/AdditionalNote|AdditionalNote) shows as `[[obsidian/SubFolder/AdditionalNote|AdditionalNote]]` when entered Wiki-style.
 - Under `Obsidian > Settings > Files and links` with `Use [[Wikilinks]]` disabled...
  - With `Files and links > New link format > Relative path to file`, [AdditionalNote](/obsidian/testpages/additionalnote) shows as `[AdditionalNote](AdditionalNote.md)` when entered Wiki-style, whereas [AdditionalNote](/obsidian/testpages/subfolder/additionalnote) shows as `[AdditionalNote](SubFolder/AdditionalNote.md)` when entered Wiki-style.
  - With `Files and links > New link format > Absolute path in vault`, [obsidian/TestPages/AdditionalNote|AdditionalNote](obsidian/TestPages/AdditionalNote|AdditionalNote) shows as `[AdditionalNote](/obsidian/additionalnote)` when entered Wiki-style, whereas [AdditionalNote](/obsidian/testpages/subfolder/additionalnote) shows as `[AdditionalNote](/obsidian/subfolder/additionalnote)` when entered Wiki-style.
- To expose some of the Obsidian notes to the public, it is necessary to (a) create a subfolder in the Obsidian vault (in this case `obsidian`) and (b) clone a new repo in GitHub that matches its name (in this case `https://github.com/dcpetty/obsidian`) in which the public notes and assets and the Jekyll site lives.

### Best strategy for allowing for parsing Obsidian links

- `Obsidian > Settings > Files and links > Use [[Wikilinks]]` *disabled* & `Obsidian > Settings > Files and links > New link format > Absolute path in vault`. This will result in repository (`obsidian`) public notes links being prefixed by `(obsidian` and postfixed by `.md)` (or other valid extensions).
- **Slugified links involve replacing spaces (`' '`) with `'%20'` but (more or less?) leaving other special characters intact.** The rule of thumb is, therefore, eschew spaces in note / file names and subfolder names.
- Wiki-style *external* links (`[[https://obsidian.md/]]`)  can be more easily entered verbatim, because wiki-style links are not allowed with `/`s (with the side effect that they cannot be clicked in Obsidian — only Jekyll).
- There is a question of whether all image assets should go in `obsidian/docs/assets/` or `obsidian/docs/assets/images/` or **`obsidian/assets/obsidian`** to be copied — with `Obsidian > Settings > Files and links > Default location for new attachments` adjusted (see below).

![](/obsidian/assets/obsidian/pasted-image-20240324105650.png)

- Other `Obsidian > Settings`
 - `General > Your Account > Sign In`
 - `Editor > Default editing mode > Source mode`
 - `Core plugins > property view > Enabled`

#Obsidian

## Jekyll on GitHub

Jekyll follows a certain directory structure and the public Obsidian notes must conform to that structure.

- The `docs` directory is the root for the entire Jekyll site set in the repository by `Settings > Pages > Branch > Select folder > docs`. That is one of two choices for folders in the `main` branch — the other being `/`.
- The `_posts` directory contains all the posts with filenames of the form *e.g.* `2024-03-15-colors.md`.
- The `assets` directory contains configuration assets. By adding the directory `assets/obsidian` to the Obsidian vault and setting '*Default location for new attachments*' it is possible to include *e.g.* `![Monty](/obsidian/assets/obsidian/monty-192x192.png)` images: ![Monty](/obsidian/assets/obsidian/monty-192x192.png) (The reason for the `obsidian` subfolder is so as to not interfere with `docs/assets` used by the Jekyll configuration.)
- The `_include` directory contains files to be included through [Liquid](https://shopify.dev/docs/api/liquid) code in the note *e.g.* `{% raw %}{% include right.html %}{% endraw %}`.

There is more documentation in [JavaScriptForIncludedNavigation](/obsidian/obsidian-jekyll/javascriptforincludednavigation) about including right navigation from .HTML files in the `_include` directory.

### Research for setting up an Obsidian-compatible Jekyll site:

- [https://docs.github.com/en/pages/quickstart](https://docs.github.com/en/pages/quickstart) *Quickstart for GitHub Pages* with Jekyll
- [https://github.com/jhvanderschee/brackettest](https://github.com/jhvanderschee/brackettest) *Wiki-style links in Jekyll*
- [https://pages.github.com/themes/](https://pages.github.com/themes/) *Supported themes* for Jekyll on GitHub pages

### Jekyll-compatible Obsidian links:

- Slugified ([https://arc.net/l/quote/zeinsemk](https://arc.net/l/quote/zeinsemk)) links created by Jekyll for `.md` files — if there is no `permalink:` in the YAML front matter — involve replacing spaces (`' '`) with `'%20'` but (more or less?) leaving other special characters intact. *The rule of thumb for Obsidian notes is, therefore, eschew spaces in file names and subfolder names* &mdash; which is the [https://wiki.c2.com/](https://wiki.c2.com/) norm.
- `[2024-03-21-Test with spaces, éh? !@%](/obsidian/docs/-posts/nesteddirectory/2024-03-21-test-with-spaces-eh)` This link illustrates the simple Obsidian slugified links (*replace spaces (`' '`) with `'%20'` but (more or less?) leave other special characters intact*).
- Since we can slugify the copied pages however we want, the simple slugify function should:
   - Replace `'%20'` with `' '`.
   - Call `unicodedata.normalize('NFKD', ...)` (https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize) with the result.
   - Replace `' '` with `'-'`, remove anything matching `r'[^/\w\s._-]'`, replace anything matching `r'[\s._]'` with `'-'`, and remove multiple `'-'`s.
   - Conditionally `lower()` the result (based on if it is a pathname or `categories:`  names).
- Therefore, translate `[text](/obsidian/directory/file)` links to `[text](/obsidian/directory/file)` links and translate `[[https://obsidian.md/]]` links to `[https://obsidian.md/](https://obsidian.md)` links.

## Minimal Mistakes

What I did to get Jekyll running on my local machine:

- https://github.com/mmistakes/mm-github-pages-starter/generate copy MM starter
- https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/ installed from scratch, to fix `gem install jekyll bundler`.

> `gem install jekyll bundler`<br>
> `bundle install`<br>
> `bundle add webrick`<br>

- [https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-I/](https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-I/) is a really helpful configuration HOW-TO site
- [https://www.supertechcrew.com/setup-jekyll-sitemap/](https://www.supertechcrew.com/setup-jekyll-sitemap/) describes `sitemap.xml`
- [https://renatogolia.com/2020/10/22/creating-this-blog-theme/](https://renatogolia.com/2020/10/22/creating-this-blog-theme/) More configuration
- [https://mmistakes.github.io/minimal-mistakes/docs/layouts/](https://mmistakes.github.io/minimal-mistakes/docs/layouts/) MM layouts

#Jekyll

## TODO

- Revisit the idea of simply copying the .MD files with adjusted links to `README.md` files in named directories and use [https://pages.github.com/](https://pages.github.com/) to format them.
- [https://ascii-tree-generator.com/](https://ascii-tree-generator.com/) can generate a directory tree matching come sample files.
<pre>obsidian/
├─ assets/
│  ├─ obsidian/
│  │  ├─ img.png
├─ docs/
│  ├─ assets/
│  │  ├─ obsidian/
│  │  │  ├─ img.png
│  ├─ _posts/
│  │  ├─ 2024-03-01-firstfile.md
│  │  ├─ 2024-03-02-secondfile.md
│  │  ├─ 2024-03-03-thirdfile.md
├─ FirstFolder/
│  ├─ SecondFile.md
├─ FirstFile.md
├─ ThirdFile.md
</pre>