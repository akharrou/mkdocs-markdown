# MKDW ➤ Overview

## Basic Markdown

See [Markdown Guide :: Basic Syntax](https://www.markdownguide.org/basic-syntax).

## Extended Markdown

See [Markdown Guide :: Extended Syntax](https://www.markdownguide.org/extended-syntax).

## Python Markdown

See [PyMdown Extensions Documentation](https://facelessuser.github.io/pymdown-extensions/).

### Snippets

Includes the entire contents of other files.

```` markdown
--8<--​ "filename.ext"
````

Comment out certain files with `;`.

````
--8<--​ ; "skip.md"
````

Spacing and other elements are preserved in output.

```` narkdown
--8<--​ "filename.md"

--8<--​ "filename.log"
````

### Admonitions (callouts)

[[Callouts - mkdw,nts,ksa,2020-1031114253|MDKW ➤ Callouts]]

### Details

???+ info "Synopsis"

    ```
    ???[+] <class> "opt-title"

        <content>
    ```

    Adds collapsable boxed content.

??? tldr "Details"

    ??? info "Parameters"

        ??? info "`[+]`"

            If specified, sets default state of the box to be open (not collapsed); default is closed.

        ??? info "`class`"

            See [[Callouts - mkdw,nts,ksa,2020-1030204944]].

??? example "Examples"

    === "Nested open/closed style"

        ???+ note "Open styled details"

            ??? danger "Nested details!"
                And more content again.

        ---

        ```
        ???+ note "Open styled details"

            ??? danger "Nested details!"
                And more content again.
        ```

??? faq "References"

    - [mkdocs::reference::admonitions::details](https://squidfunk.github.io/mkdocs-material-insiders/reference/admonitions/#details)
    - [pymdown-extensions::details](https://facelessuser.github.io/pymdown-extensions/extensions/details/)

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

Enabled via `mkdocs.yml`:

```yml
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

### Buttons

=== "Out"

    [Home](index.md){: .md-button}

=== "In"

    ```markdown
    [Home](index.md){: .md-button}
    ```

Enabled via `mkdocs.yml`:

```yml
markdown_extensions:
  - attr_list
```

### Keyboard Keys

=== "Out"

    ++ctrl+alt+enter++

=== "In"

    ```
    ++ctrl+alt+enter++
    ```

See all possbile keys at [Pymdown-Extensions ➤ Keys](https://facelessuser.github.io/pymdown-extensions/extensions/keys/). Enabled via `mkdocs.yml`:

```yml
markdown_extensions:
  - pymdownx.keys
```

### >end
