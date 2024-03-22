---
title: "ObsidianJekyll"
tags:
  - obsidian
  - jekyl
---

## What I learned about Obsidian & Jekyll

- Obsidian has `.md` files in a [normal format](https://www.markdownguide.org/tools/obsidian/) that are shown as **Notes** without the `.md`.
- Obsidian allows for nested notes within subdirectories.
- Obsidian allows for Wiki-style links (credits to [Ward Cunningham](https://en.wikipedia.org/wiki/Ward_Cunningham) & https://wiki.c2.com/) of the form `[[ObsidianJekyll]]` to link to this note. As long as there are not duplicate filenames, `[[SubDirectoryNote]]` can refer to [[SubDirectoryNote]] in a subdirectory. 
	- Under `Obsidian > Settings > Files and links with Use [[Wikilinks]]` enabled...
		- With `Files and links > New link format > Relative path to file`, [[AdditionalNote]] shows as `[[AdditionalNote]]` when entered Wiki-style, whereas [[SubFolder/AdditionalNote|AdditionalNote]] shows as `[[SubFolder/AdditionalNote|AdditionalNote]]` when entered Wiki-style.
		- With `Files and links > New link format > Absolute path in vault`, [[obsidian/AdditionalNote|AdditionalNote]] shows as `[[obsidian/AdditionalNote|AdditionalNote]]` when entered Wiki-style, whereas [[obsidian/SubFolder/AdditionalNote|AdditionalNote]] shows as `[[obsidian/SubFolder/AdditionalNote|AdditionalNote]]` when entered Wiki-style.
	- Under `Obsidian > Settings > Files and links with Use [[Wikilinks]]` disabled...
		- With `Files and links > New link format > Relative path to file`, [AdditionalNote](AdditionalNote.md) shows as `[AdditionalNote](AdditionalNote.md)` when entered Wiki-style, whereas [AdditionalNote](SubFolder/AdditionalNote.md) shows as `[AdditionalNote](SubFolder/AdditionalNote.md)` when entered Wiki-style.
		- With `Files and links > New link format > Absolute path in vault`, [[obsidian/AdditionalNote|AdditionalNote]] shows as `[AdditionalNote](obsidian/AdditionalNote.md)` when entered Wiki-style, whereas [AdditionalNote](obsidian/SubFolder/AdditionalNote.md) shows as `[AdditionalNote](obsidian/SubFolder/AdditionalNote.md)` when entered Wiki-style.

- `Obsidian > Settings`
  - `General > Your Account > Sign In`

#Obsidian

## Jekyll on GitHub

Links for setting up 
https://docs.github.com/en/pages/quickstart *Quickstart for GitHub Pages* with Jekyll
https://github.com/jhvanderschee/brackettest *Wiki-style links in Jekyll*
https://pages.github.com/themes/ *Supported themes* for Jekyll on GitHub pages

## Minimal Mistakes
- https://github.com/mmistakes/mm-github-pages-starter/generate copy MM starter
- https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/ installed from scratch, to fix `gem install jekyll bundler`

> `gem install jekyll bundler`
> `bundle install`
> `bundle add webrick`

#Jekyll


