---
title: "Internal test page — *do not use parentheses in note names*"
date: 2024-03-17 21:26:51
last_modified_at: 2024-04-11 19:49:12
show_date: true
permalink: /testpages/page-for-testing-eh/
tags:
- another-test-tag
- test
- yaml
toc: true
toc_sticky: true
category: Test
---
This note's title tests the collapsing of spaces, `'-'`s, and `'_'`s. *Putting parenteses in a note's name makes it impossible to easily parse links with a regular expression.*

## Various links

- I am linking to other Obsidian pages like [Page for testing... _-_-_ éh? !@$-](/obsidian/testpages/page-for-testing-eh)
- And [Colors](/obsidian/colors).
- And [AdditionalNote](/obsidian/testpages/subfolder/additionalnote).
- And [ObsidianJekyll](/obsidian/obsidian-jekyll/obsidianjekyll).
- And [https://google.com/](https://google.com/).

## `tags`

Tags can be added to YAML front matter (as a list) or in-line with text following a `#`.


AdditionalJekyll  YAML 'front matter' can be included throughout a note, though it renders in Obsidian as horizontal rules followed by a list. Tags can be added anywhere in-line. #another-test-tag

## Images

![20230626-i'm-taking-the-mole](/obsidian/assets/obsidian/20230626-im-taking-the-mole.png)

<center style="padding: 1em;"><em>I'm leaving your, Henry, and I'm taking the mole.</em></center>

The centered caption used embedded HTML (`<center style="padding: 1em;"><em>I'm leaving your, Henry, and I'm taking the mole.</em></center>`).

![](/obsidian/assets/obsidian/pasted-image-20240411151449.png)

There are blank lines on either side of the this pasted image, plus blank lines of either side of any HTML.

## Included files

These come from {% raw %}`{% include foo.html %}`{% endraw %} ([https://shopify.github.io/liquid/](https://shopify.github.io/liquid/) ).

```
{% include foo.html %}
```

{% include foo.html %}

## This is a test of using UTF-8

This is a way to test:

¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘«åß∂ƒ©˙∆˚¬…æΩ≈ç√∫˜µ≤≥÷

⁄€‹›ﬁﬂ‡°·‚—±Œ„´‰ˇÁ¨ˆØ∏”’ÅÍÎÏ˝ÓÔÒÚÆ¸˛Ç◊ı˜Â¯˘¿

My favorites: ×≈≡ΛΔ𝛿×∏ʻ⊠□ΦΘ👍🏻

## Include Right Navigation

See [JavaScriptForIncludedNavigation](/obsidian/obsidian-jekyll/javascriptforincludednavigation).

{% include right.html %}