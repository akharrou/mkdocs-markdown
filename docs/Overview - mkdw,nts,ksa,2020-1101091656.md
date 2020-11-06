# MKDW ➤ Overview

## Basic Markdown

!TODO Basic Markdown

## Extended Markdown

!TODO Extended Markdown

## Python Markdown

!TODO Python Markdown

### Superfence

???+ info "Synopsis"

    Adds parsing of nested fence blocks under blockquotes, lists, or other block elements. It also adds syntax highlighting to code blocks.

??? example "Examples"

    === "Blocknotes"

        - <space>
            ```
            a fenced block
            ```

        ---

        ```
        - <space>
            ```
            a fenced block
            ```
        ```

    === "Definitions"

        Definition
        :<space>
            ```
            a fenced block
            ```

        ---

        ```
        Definition
        :<space>
            ```
            a fenced block
            ```
        ```

    === "Callouts"

        ???+ tip
            ```
            code...
            ```

        ---

        ```markdown
        ???+ tip
            ```
            code...
            ```
        ```

??? faq "References"

    - [pymdown-extension::superfences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/)

### Mermaid Diagrams

Mermaid diagrams are also possible but require some more configuration and extra `.js` files, etc. See [Pymdown-Extensions ➤ Advanced Mermaid Notes](https://facelessuser.github.io/pymdown-extensions/extras/mermaid/).

## References

- [Markdown Guide :: Basic Syntax](https://www.markdownguide.org/basic-syntax)
- [Markdown Guide :: Extended Syntax](https://www.markdownguide.org/extended-syntax)
- [PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/)
