# MKDW ➤ Abbreviations and glossaries

## Synopsis

You can create glossaries whose terms, defined with `*[term]: def`,  will, in the output page, be underlined and, on hover, display their definition in a small text box.

![[abbreviations.jpg]]

## Examples

=== "Local glossary"

    In
    : <space>

        ```markdown
        <!-- docs/*.md -->
        The HTML specification is maintained by the W3C.

        *[HTML]: Hyper Text Markup Language
        *[W3C]: World Wide Web Consortium
        *[CSS]: Cascading style sheets
        ```

    ---

    Out
    : <space>

        The HTML specification is maintained by the W3C.

=== "Imported glossary"

    In
    : <space>

        ```markdown
        <!-- includes/glossary.md -->

        *[HTML]: Hyper Text Markup Language
        *[W3C]: World Wide Web Consortium
        *[CSS]: Cascading style sheets
        ```

        ```markdown
        <!-- docs/*.md -->

        The HTML specification is maintained by the W3C.

        {​% include "glossary.md" %}
        ```

    ---

    Out
    : <space>

        The HTML specification is maintained by the W3C.

## References

- [Mkdocs-Material ➤ Abbreviations](https://squidfunk.github.io/mkdocs-material-insiders/reference/abbreviations)
- [Python Markdown ➤ Extensions ➤ Abbreviations](https://python-markdown.github.io/extensions/abbreviations/)

<!-- Includes -->
{% include "includes/glossary.md" %}
<!-- >Includes -->
