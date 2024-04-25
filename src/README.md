# `obsidianjekyll`

[Obsidian](https://obsidian.md/) '&hellip;is the private and flexible writing app that adapts to the way you think.' [Jekyll](https://jekyllrb.com) '&hellip;is a static site generator. It takes text written in your favorite markup language and uses layouts to create a static website.' The theme I have chosen is [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes/) (MM).

## `obsidianjekyll`

`obsidianjekyll` processes an [Obsidian](https://obsidian.md/) vault into a [Jekyll](https://jekyllrb.com) markdown-based website.

Executing `python obsidianjekyll -?` from the command line shows:

```python3
usage: obsidianjekyll [-?] [--version] [-r] [-v] REPODIR POSTDIR

Format files in REPODIR into Jekyll and copy results to POSTDIR.

positional arguments:
  REPODIR        repository source directory
  POSTDIR        posts destination directory

optional arguments:
  -?, --help     show this help message and exit
  --version      show program's version number and exit
  -r, --rebuild  rebuild entire Jekyll site (default: False)
  -v, --verbose  log DEBUG status information (default: False)
```

## Including a right-navigation `.HTML` file

This is a sample of right navigation above any table of contents &mdash; including JavaScript to position the `<nav>`. It was inspired by [Renato Golia](https://renatogolia.com/2020/10/22/creating-this-blog-theme/). There are *a lot* of assumptions.

```js
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
- https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style
- https://zellwk.com/blog/css-values-in-js/
- https://github.com/mmistakes/minimal-mistakes/tree/master/_layouts

### TODO

- Add configuration for *include globs* `['*.md', '*.png', '*.jpg', '*.html', ]` and *exclude globs* `['**/.git/**', '**/docs/**', '**/scripts/**', '**/README.md', ]`.
- Add a way to clean out old `asset` files.
- Complete `tests` suite.
- Update test suite to include support for [`pytest`](https://docs.pytest.org/).
