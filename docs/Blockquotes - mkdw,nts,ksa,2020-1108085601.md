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

=== "Nested blockquotes"

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

=== "Nested elements"

    In
    :   <space>
        ```
        > ### The quarterly results look great!
        >
        > - Revenue was off the chart.
        > - Profits were higher than ever.
        >
        >  *Everything* is going according to **plan**.
        ```

    ---

    Out
    :   > ### The quarterly results look great!
        >
        > - Revenue was off the chart.
        > - Profits were higher than ever.
        >
        >  *Everything* is going according to **plan**.

## References

- [Markdown Guide ➤ Basic Sytnax # Blockquotes](https://www.markdownguide.org/basic-syntax/#blockquotes-1)
