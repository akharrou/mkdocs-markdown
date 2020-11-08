# MKDW ➤ Blockquotes

## Synopsis

Quotes are supported with the `> quote` syntax.

??? info "Mkdocs configurations"

    ```bash
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    ```

    ```yaml
    # mkdocs.yml
    markdown_extensions:
        - pymdownx.superfences   # better parsing for nested content blocks
    ```

## Examples

=== "Basic"

    In
    : <space>
        ```
        > some quote
        ```

    ---

    Out
    : <space>

        > some quote

=== "Multiple paragraphs"

    In
    : <space>
        ```
        > Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna
        aliqua.
        >
        > Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna
        aliqua.
        ```

    ---

    Out
    :   > Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna
        aliqua.
        >
        > Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna
        aliqua.

=== "Nesting"

    In
    : <space>
        ````
        > Some quote.
        >> subquote
        >>> subsubquote
        ````

    ---

    Out
    :   > Some quote.
        >> subquote
        >>> subsubquote

## References

- [Markdown Guide ➤ Basic Sytnax # Blockquotes](https://www.markdownguide.org/basic-syntax/#blockquotes-1)
