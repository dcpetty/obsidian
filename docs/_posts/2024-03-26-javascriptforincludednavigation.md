---
title: "JavaScript for `_include`d .HTML file with right navigation"
date: 2024-03-26 08:16:31
last_modified_at: 2024-03-28 12:26:53
show_date: true
permalink: /obsidian-jekyll/javascriptforincludednavigation/
toc: true
toc_sticky: true
---
Inspired by [Renato Golia](https://renatogolia.com/2020/10/22/creating-this-blog-theme/) and his [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) (MM) [Jekyll](https://jekyllrb.com/) site, hosted on [GitHub Pages](https://pages.github.com/) , this `right.html` file in the `_include` directory can be included on any [Obsidian](https://obsidian.md) note with `{% raw %}{% include right.html %}{% endraw %}` to add an additional navigation box like this (as on this page):

![](/obsidian/assets/obsidian/pasted-image-20240326090137.png)
<br><br>
This matches the list items:
```HTML
    <!-- Example list of external links -->
    <li><a href="https://obsidian.md/">Obsidian</a></li>
    <li><a href="https://jekyllrb.com/">Jekyll</a></li>
    <li><a href="https://github.com/dcpetty/obsidian">GitHub</a></li>
    <li><a href="https://google.com/">Google</a></li>
```

# Code

This JavaScript / HTML uses the structure of the rendered Jekyll pages to place the right navigation box at the top of the right column above any table of contents.

The basic algorithm is:
- Given that there is HTML that matches the `<aside... <nav... <header... <ul... <li... <a...` MM pattern *exactly*
- use [`querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) to find all `aside` tags with included `nav` tags
- With more than one `aside` tag, move the `nav` tag with attribute `data-toc="top"` to the beginning of the *first* `aside`
- With only one `aside` tag (the included `aside` id is the *first* one), move it to the beginning of a `section` tag matching `<section class="page__content ..." ...>`.

```js
<script>
<!-- Example right navigation above any ToC -->
<!--
The example right navigation HTML and JavaScript to position it above any ToC is based on the Minimal Mistakes (MM) format and assumes:
- The HTML follows the <aside... <nav... <header... <ul... <li... <a... MM pattern exactly.
- The example right navigation <nav> tag has a data-toc="top" attribute.
- The ToC aside (if there is one) is the first-child of a <section> with class="page__content".
-->
<aside class="sidebar__right sticky">
<nav class="toc" data-toc="top">
  <header><h4 class="nav__title" title="External Links"><i class="fa fa-link"></i> External Links</h4>
  </header>
  <ul class="toc__menu">
    <!-- Example list of external links -->
    <li><a href="https://obsidian.md/">Obsidian</a></li>
    <li><a href="https://jekyllrb.com/">Jekyll</a></li>
    <li><a href="https://github.com/dcpetty/obsidian">GitHub</a></li>
    <li><a href="https://google.com/">Google</a></li>
  </ul>
</nav>
</aside>
<!-- JavaScript for positioning right navigation above any ToC -->
<script>
document.addEventListener("DOMContentLoaded", function() {
  // https://stackoverflow.com/a/24070373
  // function runs when the DOM is ready, i.e. when document parsed
  let firstAside = document.querySelector("aside");
  if (firstAside) {
    /* document has at least one aside. */
    let firstNav = null, firstNavBorder = null;
    for (const aside of document.querySelectorAll("aside")) {
      /* query first nav of aside */
      let nav = aside.querySelector("nav");
      console.log(nav);
      if (nav !== null) {
        /* aside has at least one nav */
//        /* TODO: firstNav & firstNavBorder are currently unused */
//        if (firstNav === null) {
//          let firstNav = nav;
//          let firstNavBorder = getComputedStyle(nav).border
//          console.log(`firstNav.border = '${firstNavBorder}'`);
//        }
        if (nav.hasAttribute("data-toc")) {
          /* Jekyll doesn't always like && */
          // && nav.getAttribute("data-toc") == 'top') {
          if (nav.getAttribute("data-toc") == 'top') {
            /* nav is <nav data-toc="top" ...> */
            console.log(nav.style);
            if (firstAside === aside) {
              /* data-toc="top" is in only aside */
              let section = document.querySelector("section.page__content");
              if (section !== null) {
                /* insert aside at begining of section.page__content */
                console.log(`aside inserted afterbegin section`)
                section.insertAdjacentElement('afterbegin', aside);
              }
            }
            else {
              /* insert nav at begining of firstAside */
              console.log(`nav inserted afterbegin firstAside`)
              firstAside.insertAdjacentElement('afterbegin', nav);
              /* insert spacer after nav */
              const spacer = document.createElement("div");
              spacer.style.height = "1em";
              nav.insertAdjacentElement("afterend", spacer);
            }
          }
        }
        console.log(firstAside);
      }
    }
  }
});
</script>
```

# TODO

- Allow for more than one such navigation with the `data-toc` attribute setting the position.
- Have some way to minimize reliance on the structure of the rendered Jekyll page.
{% include right.html %}