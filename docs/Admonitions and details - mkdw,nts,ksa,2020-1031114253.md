# MKDW ➤ Admonitions and details

## Synopsis

Fixed (admonitions/callouts) or collapsible (details/summary) content.

```
[!!!|???[+]] <type> "[opt-title]"
    <content>
```

??? info "Mkdocs configurations"

    ```bash
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    ```

    ```yaml
    # mkdocs.yml
    markdown_extensions:
        - admonition
        - pymdownx.details
        - pymdownx.superfences # allows nesting code and content blocks inside admonitions/details
    ```

## Examples

=== "Basic admonition"

    In
    : <space>

        ```markdown
        !!! danger
            You should note that the title will be automatically capitalized.
            These content boxes are by default expanded and non-collapsible.
        ```

    ---

    Out
    : <space>

        !!! danger
            You should note that the title will be automatically capitalized. These content boxes are by default expanded and non-collapsible.

=== "Basic detail"

    In
    : <space>

        ```markdown
        ??? tldr
            This content box has a default collapsed/closed state.
        ```

        ```markdown
        ???+ info
            This content box has a default expanded/opened state, set by the `+`.
        ```

    ---

    Out
    : <space>

        ??? tldr
            This content box has a default collapsed/closed state.

        ???+ info
            This content box has a default expanded/opened state, set by the `+`.

=== "Titled / titleless"

    In
    : <space>

        ```markdown
        !!! note "Custom admonition title"
            This box has a custom title.
        ```

        ```markdown
        !!! important ""
            This box has no title.
        ```

    ---

    Out
    : <space>

        !!! note "Custom admonition title"
            This box has a custom title.

        !!! important ""
            This box has no title.

=== "Nesting"

    In
    : <space>

        ```markdown
        ???+ note "Open styled details"

            ??? danger "Nested details!"
                And more content again.
        ```

    ---

    Out
    : <space>

        ???+ note "Open styled details"

            ??? danger "Nested details!"
                And more content again.

## Parameters

`type`
:   Style type. Each type has its own color and icon.
    See supported types: [Mkdocs-Material ➤ Admonitions ➤ Supported types](https://squidfunk.github.io/mkdocs-material-insiders/reference/admonitions/?h=+admo#supported-types).

`[opt-title]`
:   Optional text title, displayed as content header.

## References

1. [Mkdocs-Material ➤ Admonitions](https://squidfunk.github.io/mkdocs-material-insiders/reference/admonitions/)
2. [Pymdown-Extensions ➤ Admonitions](https://squidfunk.github.io/mkdocs-material-insiders/reference/admonitions/)
3. [Pymdown-Extensions ➤ Details](https://squidfunk.github.io/mkdocs-material-insiders/reference/admonitions/)
