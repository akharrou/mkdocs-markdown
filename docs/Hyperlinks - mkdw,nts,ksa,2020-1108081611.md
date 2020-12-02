# MKDW ➤ Hyperlinks

## Synopsis

Links are supported with the `[link-text](path)` syntax by the Markdown standard, and wiki-link syntax `[[path|link-text]]` with third party plugins (e.g. for Mkdocs, [Roamlinks](https://github.com/Jackiexiao/mkdocs-roamlinks-plugin)).

??? info "Mkdocs configurations"

    ```bash
    pip install mkdocs-roamlinks-plugin
    ```

    ```yaml
    # mkdocs.yml
    plugins:
      - roamlink
    ```

## Examples

=== "Local links"

    In
    : <space>

        ```markdown
        Make sure to check out the [MkDocs page](Mkdocs.md)
        if you haven't already.
        ```

        ```markdown
        Make sure to check out the [​[Mkdocs|MkDocs page]]
        page if you haven't already.
        ```

    ---

    Out
    :   Make sure to check out the [[Mkdocs - mkdw,nts,ksa,2020-1101200211|MkDocs page]] if you haven't already.

=== "Remote links"

    In
    : <space>
      ```
      Search on [google](https://www.google.com).
      ```

    ---

    Out
    :   Search on [google](https://www.google.com).

=== "Reference style links"

    In
    : <space>

        ```
        [google][1]

        [1]: <https://www.google.com> "google homepage"
        ```

    ---

    Out
    :   <space>

        Search on [google][1].

        [1]: <https://www.google.com> "google homepage"

=== "Quick URLS and emails"

    In
    : <space>
      ```
      Email me at <fake@email.com>; also don't forget to search
      on <https://www.google.com>.
      ```

    ---

    Out
    :   Email me at <fake@email.com>; also don't forget to search on <https://www.google.com>.

## References

- [Markdown Guide ➤ Basic Syntax # Links](https://www.markdownguide.org/basic-syntax/#links)
