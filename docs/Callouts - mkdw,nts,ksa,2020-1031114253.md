# MKDW ➤ Callouts

Also known as _admonitions_.

## Synopsis

```
!!! <class> "[opt-title]"
    <content>
```
Boxed content.

## Examples

=== "Default"

    In
    : <space>

        ```
        !!! danger
            You should note that the title will be automatically capitalized.
        ```

    ---

    Out
    : <space>

        !!! danger
            You should note that the title will be automatically capitalized.

=== "Custom title"

    In
    : <space>

        ```
        !!! note "Custom callout title"
            ...
        ```

    ---

    Out
    : <space>

        !!! note "Custom callout title"
            ...

=== "Titleless"

    In
    : <space>

        ```
        !!! important ""
            Callout without title.
        ```

    ---

    Out
    : <space>

        !!! important ""
            Callout without title.

## Parameters

`class`
:   Callout type, each type has its own color and icon. See supported types: [Mkdocs-Material ➤ Admonitions ➤ Supported types](https://squidfunk.github.io/mkdocs-material-insiders/reference/admonitions/?h=+admo#supported-types).

`[opt-title]`
:   Optional text title, displayed as box header

## References

1. [Mkdocs-Material ➤ References ➤ Admonitions](https://squidfunk.github.io/mkdocs-material-insiders/reference/admonitions/)
1. [Pymdown-Extensions ➤ References ➤ Details](https://squidfunk.github.io/mkdocs-material-insiders/reference/admonitions/)
1. [Pymdown-Extensions ➤ References ➤ Admonitions](https://squidfunk.github.io/mkdocs-material-insiders/reference/admonitions/)
