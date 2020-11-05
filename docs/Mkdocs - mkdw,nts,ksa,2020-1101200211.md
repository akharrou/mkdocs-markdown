# MKDW ➤ Mkdocs

Markdown documentation static website generator.

![[mkdocs material website - mkdw,imgs,ksa,2020-1101202711.png|asset-1]]

## Synopsis

Mkdocs is a python script, downloadable through [`pip`](https://pip.pypa.io/en/stable/), that generates a static documentation website. Documentation source files are written in [[Overview - mkdw,nts,ksa,2020-1101091656|Markdown]], and the website generation is configured with a single YAML file.

Beyond configurable, the generated website is extensible and overrideable in its functionality and in its look, through [third-party plugins](https://www.mkdocs.org/user-guide/plugins/) and [themes](https://www.mkdocs.org/user-guide/styling-your-docs/) but also by integrating your own python functions/modules, css stylesheets, javascripts, assets (SVG icons), etc. Additionally the Markdown language is also extendable with extensions like [Pymdown-Extensions](https://facelessuser.github.io/pymdown-extensions/). The best theme is hands down [Mkdocs-Material](https://squidfunk.github.io/mkdocs-material-insiders/), elegant and [[Extending mkdocs-material - mkdw,nts,ksa,2020-1101214900|fully extendable]].

## Examples

=== "Install"

    ```python
    pip install mkdocs
    ```

=== "Create project"

    ```bash
    mkdocs new my-project
    cd my-project
    ```
    ```bash
    .
    ├── docs
    │   └── index.md
    └── mkdocs.yml

    1 directory, 2 files
    ```

=== "Generate website"

    ```python
    mkdocs build
    ```

=== "Preview website"

    ```python
    mkdocs serve
    ```

=== "YAML config"

    <!--
    ```yaml
    # mkdocs.yml
    --8<-- "mkdocs.yml"
    ```
    -->

    ```yaml
    # mkdocs.yml

    site_name: '__fill__'
    site_url: '__fill__'
    site_author: '__fill__'
    site_description: '__fill__'
    repo_name: '__fill__'
    repo_url: '__fill__'
    edit_uri: '__fill__'
    copyright: '__fill__'

    docs_dir: 'docs/'
    theme:
        include_search_page: false
        search_index_only: true
        name: material
        language: en
        features:
            - navigation.tabs
            - navigation.instant
        palette:
            - scheme: default
                primary: black
                accent: deep purple
        font:
            text: Roboto
            code: Roboto Mono
        favicon: _assets/alfred.png
        icon:
            logo: material/apps
            repo: fontawesome/brands/github

        extra:
        social:
            - icon: fontawesome/brands/github
            link: <https://github.com/akharrou>
            - icon: fontawesome/brands/twitter
            link: <https://twitter.com/_akharrou>
            - icon: fontawesome/brands/linkedin
            link: <https://linkedin.com/in/akharrou/>

    plugins:
        - search:
            lang: en
            separator: '[\s\-\.]+'
            prebuild_index: true
        - git-revision-date-localized:
            type: timeago
            time_zone: UTC
            locale: en
            fallback_to_build_date: false
        - add-number:
            increment_topnav: false
            increment_pages: false
            order: 2
            strict_mode: false
            excludes:
            includes:
        - exclude-search:
            exclude:
                - index.md
        - minify:
            minify_html: true
            minify_js: true
            htmlmin_opts:
                remove_comments: true
        - roamlinks
        - exclude:
            glob:
                - exclude/this/path/*
                - "*.tmp"
                - "*.pdf"
                - "*.gz"
            regex:
                - '.*\.(tmp|bin|tar)$'

    markdown_extensions:
        - toc:
            toc_depth: 6
            permalink: ⚓︎
            slugify: !!python/name:pymdownx.slugs.uslugify
        - abbr
        - admonition
        - def_list
        - footnotes
        - attr_list
        - pymdownx.tabbed
        - pymdownx.inlinehilite
        - pymdownx.details
        - pymdownx.superfences:
            disable_indented_code_blocks: true
            preserve_tabs: true
            custom_fences:
                - name: math
                class: arithmatex
                format: !!python/name:pymdownx.arithmatex.fence_mathjax_format
                # - name: mermaid
                #   class: mermaid
                #   format: !!python/name:pymdownx.superfences.fence_code_format
        - pymdownx.highlight:
            # linenums: false
            linenums_style: pymdownx.inline
            guess_lang: true
            extend_pygments_lang:
              - name: php-inline
                  lang: php
                  options:
                  startinline: true
              - name: pycon3
                  lang: pycon
                  options:
                  python3: true
        - pymdownx.critic:
            mode: view
        - pymdownx.betterem:
            smart_enable: all
        - pymdownx.caret:
            insert: true
            superscript: true
        - pymdownx.mark:
            smart_mark: true
        - pymdownx.tilde:
            smart_delete: true
            delete: true
            subscript: true
        - pymdownx.smartsymbols:
            trademark: true
            copyright: true
            registered: true
            care_of: true
            plusminus: true
            arrows: true
            notequal: true
            fractions: true
            ordinal_numbers: true
        - pymdownx.keys:
            separator: '+'
        - pymdownx.arithmatex:
            generic: true
        - pymdownx.snippets:
            base_path: '.'
            encoding: utf-8
            check_paths: true
        - pymdownx.emoji:
            emoji_index: !!python/name:materialx.emoji.twemoji
            emoji_generator: !!python/name:materialx.emoji.to_svg

    extra_css:
        - stylesheets/extra.css

    extra_javascript:
        - javascripts/config.js
        - <https://polyfill.io/v3/polyfill.min.js?features=es6>
        - <https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js>
    ```

=== "Plugins & themes"

    ```bash
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    ```

    ```yaml
    # mkdocs.yml
    theme:
        name: material
    markdown_extensions:
        pymdownx.attr_list
    plugins:
        - macros:
    ...
    ```

## References

- [Mkdocs](https://www.mkdocs.org/)
- [Mkdocs ➤ Plugins](https://www.mkdocs.org/user-guide/plugins/)
- [Mkdocs ➤ Styling](https://www.mkdocs.org/user-guide/styling-your-docs/)
- [Mkdocs-Material](https://squidfunk.github.io/mkdocs-material-insiders/)
- [Pymdown-Extensions](https://facelessuser.github.io/pymdown-extensions/)
