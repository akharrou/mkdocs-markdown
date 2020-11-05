# MKDW ➤ Superscript and Subscript

## Synopsis

Superscript is supported with the `^txt^` syntax and subscript with the `~txt~` syntax.

!!! info "Mkdocs Configuration"

    Enabled via `mkdocs.yml`:

    ```yaml
    markdown_extensions:
      - pymdownx.caret # superscript
      - pymdownx.tilde # subscript
    ```

## Examples

=== "Basic"

    In
    : <space>

        ```
        - December 12^th^.
        - H~2~0
        - A^T^A
        ```

    ---

    Out
    : <space>

      - December 12^th^.
      - H~2~0
      - A^T^A

## References

- [Mkdocs-Material ➤ Superscript](https://squidfunk.github.io/mkdocs-material-insiders/reference/formatting/#caret-mark-tilde)
- [Pymdown-Extensions ➤ Superscript](https://facelessuser.github.io/pymdown-extensions/extensions/caret/#superscript)
