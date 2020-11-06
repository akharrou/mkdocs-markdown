# MKDW ➤ Highlight marks

## Synopsis

Highlighted text marks are supported with the `==text==` syntax.

??? info "Mkdocs configurations"

    ```bash
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    ```

    ```yaml
    # mkdocs.yml
    markdown_extensions:
      - pymdownx.mark
    ```

## Examples

=== "Basic"

    In
    : <space>

      ```
      ==mark me==

      ==smart==mark==
      ```

    ---

    Out
    : <space>

        ==mark me==

        ==smart==mark==

## References

- [Mkdocs-Material ➤ Formating ➤ Caret, Mark, Tilde](https://squidfunk.github.io/mkdocs-material-insiders/reference/formatting/#caret-mark-tilde)
- [Pymdown-Extension ➤ Mark](https://facelessuser.github.io/pymdown-extensions/extensions/mark/)
