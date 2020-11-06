---
title: Lorem ipsum
---

# MKDW ➤ Meta tags

## Synopsis

In HTML, meta tags allow to provide additional metadata for a document, e.g. page titles and descriptions, additional assets to be loaded, and [Open Graph](https://ogp.me/) data. Also known as front matter, it's written as a series of key-value pairs at the beginning of the Markdown document, delimited by a blank line which ends the YAML context.

??? info "Mkdocs configurations"

    ```bash
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    ```

    ```yaml
    # mkdocs.yml
    markdown_extensions:
      - meta
    ```

## Examples

=== "Basic"

    ```markdown
    <!-- docs/*.md -->
    ---
    title: Lorem ipsum dolor sit amet
    description: Nullam urna elit, malesuada eget finibus ut, ac tortor.
    ---

    Content...
    ```

## References

- [Mkdocs-Material ➤ Meta Tags](https://squidfunk.github.io/mkdocs-material-insiders/reference/meta-tags/)
- [Jekyll ➤ Docs ➤ Front Matter](https://jekyllrb.com/docs/front-matter/)
