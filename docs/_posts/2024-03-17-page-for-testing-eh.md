---
title: "Internal test page — *do not use parentheses in note names*"
date: 2024-03-17 21:26:51
last_modified_at: 2024-08-22 11:01:09
show_date: true
permalink: /testpages/page-for-testing-eh/
tags:
- test
- yaml
toc: true
toc_sticky: true
category: Test
baz:
- foo
- 123
- 2024-06-21 18:36:45
- - bar
  - 456
  - - blap:
      - 3
      - 2
      - 1
math: true
foo: 1234
bar: 2024-03-25 18:15:12
qux:
- 1
- 2
- 3
- 4
---
This note's title tests the collapsing of spaces, `'-'`s, and `'_'`s. *Putting parentheses in a note's name makes it impossible to easily parse links with a regular expression.*

This note tests many aspects of Obsidian and Jekyll as parsed by [`obsidianjekyll`](https://github.com/dcpetty/obsidian/tree/main/src/obsidianjekyll).

## Various links

- I am linking to other Obsidian pages like [Page for testing... _-_-_ éh? !@$-](/obsidian/testpages/page-for-testing-eh)
- And [Colors](/obsidian/colors).
- And [AdditionalNote](/obsidian/testpages/subfolder/additionalnote).
- And [ObsidianJekyll](/obsidian/obsidian-jekyll/obsidianjekyll).
- And [https://google.com/](https://google.com/).

## YAML 'font matter'


- YAML format consists of `---`, a dictionary in the form of `key: value`, followed by `---` in line in the note. When YAML appears as the first thing in a note, it is literally front matter. It can appear multiple times in a note
- The YAML `key` is a string. The YAML `value` can be a string or a list. lists are entered as follows:

```
metasyntactic:
 - foo
 - bar
 - baz
```

- Duplicate `key`s incorporate only the final value, as with `category: Test` above, except for `key` `'tags'` where all tags are accumulated in a sorted set.

## `tags`

- Tags can be added to YAML front matter (as a list) or in-line with text following a `#`.
- Additional Jekyll  YAML 'front matter' can be included throughout a note, though it renders in Obsidian as horizontal rules followed by a list.
- Tags can be added anywhere in-line. #test
- Duplicate tags in a single document are removed. For example, there is only one `#test` tag included in this document, though it is included in the front matter, the in-line tag above and the following 'front matter.'


## Images

![20230626-i'm-taking-the-mole](/obsidian/assets/obsidian/20230626-im-taking-the-mole.png)

<center style="padding: 1em;"><em>I'm leaving you, Henry, and I'm taking the mole.</em></center>

The centered caption used embedded HTML (`<center style="padding: 1em;"><em>I'm leaving you, Henry, and I'm taking the mole.</em></center>`).

![](/obsidian/assets/obsidian/pasted-image-20240411151449.png)

There are blank lines on either side of the this pasted image, plus blank lines on either side of any HTML.

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

My favorites: ×≈≡ΛΔ𝛿×𝜈∏ʻ‡⊠□ΦΘ½👍🏻♥️

## Include Right Navigation

See [JavaScriptForIncludedNavigation](/obsidian/obsidian-jekyll/javascriptforincludednavigation).

{% include right.html %}