---
show_date: true
title: "ObsidianJekyll"
categories:
 - Obsidian-Jekyll
tags:
 - Obsidian
 - Jekyll
toc: true
toc_sticky: true
---
## What I learned about Obsidian & Jekyll

- Obsidian has `.md` files in a [normal format](https://www.markdownguide.org/tools/obsidian/) that are shown as **Notes** without the `.md`.
- Obsidian allows for nested notes within subdirectories.
- Obsidian allows for Wiki-style links (credits to [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham) & https://wiki.c2.com/) of the form `[ObsidianJekyll](ObsidianJekyll)` to link to this note. As long as there are not duplicate filenames, `[SubDirectoryNote](SubDirectoryNote)` can refer to [obsidian/TestPages/SubFolder/SubDirectoryNote](obsidian/TestPages/SubFolder/SubDirectoryNote) in a subdirectory.
  - Under `Obsidian > Settings > Files and links` with `Use [Wikilinks](Wikilinks)` enabled...
   - With `Files and links > New link format > Relative path to file`, [obsidian/TestPages/AdditionalNote](obsidian/TestPages/AdditionalNote) shows as `[AdditionalNote](AdditionalNote)` when entered Wiki-style, whereas [obsidian/TestPages/SubFolder/AdditionalNote|AdditionalNote](obsidian/TestPages/SubFolder/AdditionalNote|AdditionalNote) shows as `[SubFolder/AdditionalNote|AdditionalNote](SubFolder/AdditionalNote|AdditionalNote)` when entered Wiki-style.
   - With `Files and links > New link format > Absolute path in vault`, [obsidian/TestPages/AdditionalNote|AdditionalNote](obsidian/TestPages/AdditionalNote|AdditionalNote) shows as `[obsidian/AdditionalNote|AdditionalNote](obsidian/AdditionalNote|AdditionalNote)` when entered Wiki-style, whereas [obsidian/TestPages/SubFolder/AdditionalNote|AdditionalNote](obsidian/TestPages/SubFolder/AdditionalNote|AdditionalNote) shows as `[obsidian/SubFolder/AdditionalNote|AdditionalNote](obsidian/SubFolder/AdditionalNote|AdditionalNote)` when entered Wiki-style.
 - Under `Obsidian > Settings > Files and links` with `Use [Wikilinks](Wikilinks)` disabled...
  - With `Files and links > New link format > Relative path to file`, [AdditionalNote](/obsidian/testpages/additionalnote) shows as `[AdditionalNote](AdditionalNote.md)` when entered Wiki-style, whereas [AdditionalNote](/obsidian/testpages/subfolder/additionalnote) shows as `[AdditionalNote](SubFolder/AdditionalNote.md)` when entered Wiki-style.
  - With `Files and links > New link format > Absolute path in vault`, [obsidian/TestPages/AdditionalNote|AdditionalNote](obsidian/TestPages/AdditionalNote|AdditionalNote) shows as `[AdditionalNote](/obsidian/additionalnote)` when entered Wiki-style, whereas [AdditionalNote](/obsidian/testpages/subfolder/additionalnote) shows as `[AdditionalNote](/obsidian/subfolder/additionalnote)` when entered Wiki-style.

- **Best strategy for parsing links: `Obsidian > Settings > Files and links > Use [Wikilinks](Wikilinks)` *disabled* & `Obsidian > Settings > Files and links > New link format > Absolute path in vault`.**  This will result in repository (`obsidian`) public notes links being prefixed by `(obsidian` and postfixed by `.md)` (or other valid extensions).
- **Slugified links involve replacing spaces (`' '`) with `'%20'` but (more or less?) leaving other special characters intact.** The rule of thumb is, therefore, eschew spaces in note / file names and subfolder names.
- There is a question of whether all image assets should go in `obsidian/docs/assets/` or `obsidian/docs/assets/images/` or `obsidian/assets` to be copied — with `Obsidian > Settings > Files and links > Default location for new attachments` adjusted.

![](/obsidian/assets/obsidian/pasted-image-20240324105650.png)

- `Obsidian > Settings`
 - `General > Your Account > Sign In`

#Obsidian

## Jekyll on GitHub

Links for setting up
https://docs.github.com/en/pages/quickstart *Quickstart for GitHub Pages* with Jekyll
https://github.com/jhvanderschee/brackettest *Wiki-style links in Jekyll*
https://pages.github.com/themes/ *Supported themes* for Jekyll on GitHub pages

[2024-03-21-Test with spaces, éh? !@%](/obsidian/docs/-posts/nesteddirectory/2024-03-21-test-with-spaces-eh) This link illustrates the simple Obsidian slugified links (*replace spaces (`' '`) with `'%20'` but (more or less?) leave other special characters intact*). Since we can slugify the copied pages however we want, the simple slugify function should:
- Replace `'%20'` with `' '`.
- Call `unicodedata.normalize('NFKD', ...)` (https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize) with the result.
- Replace `' '` with `'-'`.
- `lower()` the result.
## Minimal Mistakes

- https://github.com/mmistakes/mm-github-pages-starter/generate copy MM starter
- https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/ installed from scratch, to fix `gem install jekyll bundler`

> `gem install jekyll bundler`
> `bundle install`
> `bundle add webrick`

- [https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-I/](https://www.cross-validated.com/Personal-website-with-Minimal-Mistakes-Jekyll-Theme-HOWTO-Part-I/) is a really helpful configuration HOW-TO site
- [https://www.supertechcrew.com/setup-jekyll-sitemap/](https://www.supertechcrew.com/setup-jekyll-sitemap/) describes `sitemap.xml`
- [https://renatogolia.com/2020/10/22/creating-this-blog-theme/](https://renatogolia.com/2020/10/22/creating-this-blog-theme/) More configuration
- [https://mmistakes.github.io/minimal-mistakes/docs/layouts/](https://mmistakes.github.io/minimal-mistakes/docs/layouts/) MM layouts

There is more documentation in [JavaScriptForIncludedNavigation](/obsidian/obsidian-jekyll/javascriptforincludednavigation) about including right navigation.

#Jekyll



<!-- Modified 2024-03-27:22:33:59 -->
