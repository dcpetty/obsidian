---
title: "ObsidianJekyll"
categories:
 - obsidian
tags:
 - Obsidian
 - Jekyll
---
## What I learned about Obsidian & Jekyll
- Obsidian has `.md` files in a [normal format](https://www.markdownguide.org/tools/obsidian/) that are shown as **Notes** without the `.md`.
- Obsidian allows for nested notes within subdirectories.
- Obsidian allows for Wiki-style links (credits toÂ [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham) & https://wiki.c2.com/) of the form `[[ObsidianJekyll]]` to link to this note. As long as there are not duplicate filenames, `[[SubDirectoryNote]]` can refer to [[SubDirectoryNote]] in a subdirectory. 
- Under `Obsidian > Settings > Files and links` with `Use [[Wikilinks]]` enabled...
- With `Files and links > New link format > Relative path to file`, [[AdditionalNote]] shows as `[[AdditionalNote]]` when entered Wiki-style, whereas [[SubFolder/AdditionalNote|AdditionalNote]] shows as `[[SubFolder/AdditionalNote|AdditionalNote]]` when entered Wiki-style.
- With `Files and links > New link format > Absolute path in vault`, [[obsidian/AdditionalNote|AdditionalNote]] shows as `[[obsidian/AdditionalNote|AdditionalNote]]` when entered Wiki-style, whereas [[obsidian/SubFolder/AdditionalNote|AdditionalNote]] shows as `[[obsidian/SubFolder/AdditionalNote|AdditionalNote]]` when entered Wiki-style.
- Under `Obsidian > Settings > Files and links` with `Use [[Wikilinks]]` disabled...
- With `Files and links > New link format > Relative path to file`, [AdditionalNote](AdditionalNote.md) shows as `[AdditionalNote](AdditionalNote.md)` when entered Wiki-style, whereas [AdditionalNote](SubFolder/AdditionalNote.md) shows as `[AdditionalNote](SubFolder/AdditionalNote.md)` when entered Wiki-style.
- With `Files and links > New link format > Absolute path in vault`, [[obsidian/AdditionalNote|AdditionalNote]] shows as `[AdditionalNote](obsidian/AdditionalNote.md)` when entered Wiki-style, whereas [AdditionalNote](obsidian/SubFolder/AdditionalNote.md) shows as `[AdditionalNote](obsidian/SubFolder/AdditionalNote.md)` when entered Wiki-style.
- **Best strategy for parsing links: `Obsidian > Settings > Files and links > Use [[Wikilinks]]` *disabled* & `Obsidian > Settings > Files and links > New link format > Absolute path in vault`.**  This will result in repository (`obsidian`) public notes links being prefixed by `(obsidian` and postfixed by `.md)` (or other valid extensions).
- **Slugified links involve replacing spaces (`' '`) with `'%20'` but (more or less?) leaving other special characters intact.** The rule of thumb is, therefore, eschew spaces in note / file names and subfolder names.
- There is a question of whether all image assets should go in `obsidian/docs/assets/` or `obsidian/docs/assets/images/` or `obsidian/assets` to be copied â with `Obsidian > Settings > Files and links > Default location for new attachments` adjusted.
![](obsidian/assets/Pasted%20image%2020240323125126.png)
- `Obsidian > Settings`
- `General > Your Account > Sign In`
#Obsidian
## Jekyll on GitHub
Links for setting up 
https://docs.github.com/en/pages/quickstart *Quickstart for GitHub Pages* with Jekyll
https://github.com/jhvanderschee/brackettest *Wiki-style links in Jekyll*
https://pages.github.com/themes/ *Supported themes* for Jekyll on GitHub pages
[2024-03-21-Test with spaces, Ã©h? !@%](obsidian/docs/_posts/NestedDirectory/2024-03-21-Test%20with%20spaces,%20Ã©h?%20!@%.md) This link illustrates the simple Obsidian slugified links (*replace spaces (`' '`) with `'%20'` but (more or less?) leave other special characters intact*). Since we can slugify the copied pages however we want, the simple slugify function should:
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
#Jekyll

<!-- Modified 2024-03-23:12:56:07 -->
