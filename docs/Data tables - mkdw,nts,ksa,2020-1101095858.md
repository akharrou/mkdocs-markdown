# MKDW ➤ Data tables

## Synopsis

Tables are supported, with no configuration required.

## Examples

=== "Left Aligned"

    In
    : <space>

        ```
        | Method      | Description                          |
        | :---------- | :----------------------------------- |
        | `GET`       | :material-check:     Fetch resource  |
        | `PUT`       | :material-check-all: Update resource |
        | `DELETE`    | :material-close:     Delete resource |
        ```

    ---

    Out
    : <space>

        | Method      | Description                          |
        | :---------- | :----------------------------------- |
        | `GET`       | :material-check:     Fetch resource  |
        | `PUT`       | :material-check-all: Update resource |
        | `DELETE`    | :material-close:     Delete resource |

=== "Center Aligned"

    In
    : <space>

        ```
        | Method      | Description                          |
        | :----------: | :-----------------------------------: |
        | `GET`       | :material-check:     Fetch resource  |
        | `PUT`       | :material-check-all: Update resource |
        | `DELETE`    | :material-close:     Delete resource |
        ```

    ---

    Out
    : <space>

        | Method      | Description                          |
        | :----------: | :-----------------------------------: |
        | `GET`       | :material-check:     Fetch resource  |
        | `PUT`       | :material-check-all: Update resource |
        | `DELETE`    | :material-close:     Delete resource |

=== "Right Aligned"

    In
    : <space>

        ```
        | Method      | Description                          |
        | ----------: | -----------------------------------: |
        | `GET`       | :material-check:     Fetch resource  |
        | `PUT`       | :material-check-all: Update resource |
        | `DELETE`    | :material-close:     Delete resource |
        ```

    ---

    Out
    : <space>

        | Method      | Description                          |
        | ----------: | -----------------------------------: |
        | `GET`       | :material-check:     Fetch resource  |
        | `PUT`       | :material-check-all: Update resource |
        | `DELETE`    | :material-close:     Delete resource |

=== "Sorted"

    For [Mkdocs-Material](https://squidfunk.github.io/mkdocs-material-insiders/), to sort tables see [Mkdocs-Material ➤ Sortable Tables](https://squidfunk.github.io/mkdocs-material-insiders/reference/data-tables/#sortable-tables).

## References

- [Mkdocs-Material ➤ Data tables](https://squidfunk.github.io/mkdocs-material-insiders/reference/data-tables/)
