# MKDW ➤ Special characters

## Synopsis

You can write special characters in plaintext and they will automatically be converted into their corresponding symbol glyphs.

??? info "Mkdocs configurations"

    ```bash
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    ```

    ```yaml
    # mkdocs.yml
    markdown_extensions:
        - pymdownx.smartsymbols
    ```

## Examples

=== "Basic"

    Out | In
    - | -
    (tm) | `(tm)`
    (c) | `(c)`
    (r) | `(r)`
    +/- | `+/-`
    --> | `-->`
    <-- | `<--`
    <--> | `<-->`
    =/= | `=/=`
    1/4 | `1/4`
    1st 2nd 3rd 4th 12th | `1st 2nd 3rd 4th 12th`

## References

- [Mkdocs-Material ➤ Formatting ➤ SmartSymbols](https://squidfunk.github.io/mkdocs-material-insiders/reference/formatting/)
- [Pymdown-Extensions ➤ SmartSymbols](https://facelessuser.github.io/pymdown-extensions/extensions/smartsymbols/)
