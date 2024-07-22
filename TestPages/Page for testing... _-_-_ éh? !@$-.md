---
category: OriginalTest
tags:
 - test
---

# Internal test page — *do not use parentheses in note names*

This note's title tests the collapsing of spaces, `'-'`s, and `'_'`s. *Putting parentheses in a note's name makes it impossible to easily parse links with a regular expression.*

This note tests many aspects of Obsidian and Jekyll as parsed by [`obsidianjekyll.py`](https://github.com/dcpetty/obsidian/blob/main/scripts/obsidianjekyll.py).

## Various links

- I am linking to other Obsidian pages like [Page for testing... _-_-_ éh? !@$-](obsidian/TestPages/Page%20for%20testing...%20_-_-_%20éh?%20!@$-.md)
- And [Colors](obsidian/Colors.md).
- And [AdditionalNote](obsidian/TestPages/SubFolder/AdditionalNote.md).
- And [ObsidianJekyll](obsidian/Obsidian%20&%20Jekyll/ObsidianJekyll.md).
- And [[https://google.com/]].

## YAML 'font matter'

---
category: Test
tags:
 - yaml
---

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

---
tags: test
---

## Images

![20230626-i'm-taking-the-mole](obsidian/assets/obsidian/20230626-i'm-taking-the-mole.png)

<center style="padding: 1em;"><em>I'm leaving you, Henry, and I'm taking the mole.</em></center>

The centered caption used embedded HTML (`<center style="padding: 1em;"><em>I'm leaving you, Henry, and I'm taking the mole.</em></center>`).

![](obsidian/assets/obsidian/Pasted%20image%2020240411151449.png)

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

My favorites: ×≈≡ΛΔ𝛿×∏ʻ⊠□ΦΘ👍🏻

## Include Right Navigation

See [JavaScriptForIncludedNavigation](obsidian/Obsidian%20&%20Jekyll/JavaScriptForIncludedNavigation.md).

{% include right.html %}