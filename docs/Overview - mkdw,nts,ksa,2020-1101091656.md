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

### Code syntax highlighting, line numbering & line highlighting

```bash
pip install mkdocs-material
pip install mkdocs-material-extensions
```

```yaml
# mkdocs.yml
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.inlinehilite
```

Code syntax highlighting, line numbering and line highlighting:

=== "Out"

    ``` python linenums='1' hl_lines='1-2 4 7-8'
    import foo
    import boo.baz
    import foo.bar.baz

    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```

=== "In"

    ````
    ``` python linenums='1' hl_lines='1-2 4 7-8'
    import foo
    import boo.baz
    import foo.bar.baz

    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```
    ````

Class injections with the braces `{}`, `.cls`, `#id`:

=== "Out"

    ``` {.python .extra-class #id linenums="1 1 2"}
    """Some file."""
    import foo.bar
    import boo.baz
    import foo.bar.baz
    ```

=== "In"

    ````
    ``` {.python .extra-class #id linenums="1 1 2"}
    """Some file."""
    import foo.bar
    import boo.baz
    import foo.bar.baz
    ```
    ````

Inline code highlighting, e.g.: `:::python import foo`. Requires `pymdownx.inlinehilite`.

### Mermaid Diagrams

Mermaid diagrams are also possible but require some more configuration and extra `.js` files, etc. See [Pymdown-Extensions ➤ Advanced Mermaid Notes](https://facelessuser.github.io/pymdown-extensions/extras/mermaid/).

## References

- [Markdown Guide :: Basic Syntax](https://www.markdownguide.org/basic-syntax)
- [Markdown Guide :: Extended Syntax](https://www.markdownguide.org/extended-syntax)
- [PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/)
