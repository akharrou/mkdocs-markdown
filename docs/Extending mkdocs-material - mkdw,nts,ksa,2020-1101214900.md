# MKDW ➤ Extending `mkdocs-material` Theme

## Synopsis

To extend the [[Mkdocs - mkdw,nts,ksa,2020-1101200211|Mkdocs]] [Material theme](https://squidfunk.github.io/mkdocs-material-insiders/), you must:

1. create/add your extension file(s) (e.g. `*.css`,`*.js`, `*.svg`)
2. in the right folder structure
3. and configure your `mkdocs.yml` appropriately

=== "Add CSS stylesheets"

    ```bash
    .
    ├─ docs/
    │  └─ stylesheets/
    │     └─ *.css
    └─ mkdocs.yml
    ```

    ```yaml
    # mkdocs.yml
    extra_css:
      - stylesheets/*.css
    ```

=== "Add javascripts"

    ```bash
    .
    ├─ docs/
    │  └─ javascripts/
    │     └─ *.js
    └─ mkdocs.yml
    ```

    ```yaml
    # mkdocs.yml
    extra_javascript:
      - javascripts/*.js
    ```

=== "Add icons"

    ```bash
    .
    ├─ overrides/
    │  └─ .icons/
    │     └─ <folder-name>/
    │        └─ *.svg
    └─ mkdocs.yml
    ```

    ```yaml
    # mkdocs.yml
    markdown_extensions:
      - pymdownx.emoji:
          emoji_index: !!python/name:materialx.emoji.twemoji
          emoji_generator: !!python/name:materialx.emoji.to_svg
          options:
            custom_icons:
              - overrides/.icons
    ```

    ??? info "Usage"

        Use it in this manner in markdown files:

        ```markdown
        :<folder>-<svg>:
        :bootstrap-emoji-sunglasses:
        ```

        When you're extending the theme with partials or blocks, you can simply reference any icon that's bundled with the theme with Jinja's include function and wrap it with the twemoji class:

        ```html
        <span class="twemoji">
          {​% include ".icons/fontawesome/brands/twitter.svg" %}
        </span>
        ```

=== "Override partials and blocks"

    ??? info "Directory layout of the theme"

        ```
        .
        ├─ .icons/                             # Bundled icon sets
        ├─ assets/
        │  ├─ images/                          # Images and icons
        │  ├─ javascripts/                     # JavaScript
        │  └─ stylesheets/                     # Stylesheets
        ├─ partials/
        │  ├─ integrations/                    # Third-party integrations
        │  │  ├─ analytics.html                # - Google Analytics
        │  │  └─ disqus.html                   # - Disqus
        │  ├─ language/                        # Localized languages
        │  ├─ footer.html                      # Footer bar
        │  ├─ header.html                      # Header bar
        │  ├─ language.html                    # Localized labels
        │  ├─ logo.html                        # Logo in header and sidebar
        │  ├─ nav.html                         # Main navigation
        │  ├─ nav-item.html                    # Main navigation item
        │  ├─ palette.html                     # Color palette
        │  ├─ search.html                      # Search box
        │  ├─ social.html                      # Social links
        │  ├─ source.html                      # Repository information
        │  ├─ source-date.html                 # Last updated date
        │  ├─ source-link.html                 # Link to source file
        │  ├─ tabs.html                        # Tabs navigation
        │  ├─ tabs-item.html                   # Tabs navigation item
        │  ├─ toc.html                         # Table of contents
        │  └─ toc-item.html                    # Table of contents item
        ├─ 404.html                            # 404 error page
        ├─ base.html                           # Base template
        └─ main.html                           # Default page
        ```

    Pick the page you want to edit from the directory layout of the theme and add it under the `overrides/` directory.

    ```bash
    .
    ├─ overrides/
    │  └─ main.html
    │  └─ partials/
    │     └─ footer.html
    └─ mkdocs.yml
    ```

    ```yaml
    # mkdocs.yml
    theme:
      name: material
      custom_dir: overrides
    ```

=== "More fundamental changes"

    If you want to make more fundamental changes, it may be necessary to make the adjustments directly in the source of the theme and recompile it. See [Mkdocs-Material ➤ Customization ➤ Theme Development](https://squidfunk.github.io/mkdocs-material-insiders/customization/#theme-development)

## Examples

=== "Add Bootstrap icons"

    Download [Bootstrap Icons from their website](https://icons.getbootstrap.com/#install) and move them into the below structure.

    ```bash
    .
    ├─ overrides/
    │  └─ .icons/
    │     └─ bootstrap/
    │        └─ *.svg
    └─ mkdocs.yml
    ```

    Add this to your `mkdocs.yml` file.

    ```yaml
    # mkdocs.yml
    markdown_extensions:
      - pymdownx.emoji:
          emoji_index: !!python/name:materialx.emoji.twemoji
          emoji_generator: !!python/name:materialx.emoji.to_svg
          options:
            custom_icons:
              - overrides/.icons
    ```

    ??? info "Usage"

        In
        : <space>
          ```
          :bootstrap-emoji-sunglasses:
          ```

        ---

        Out
        : :bootstrap-emoji-sunglasses:

=== "Override blocks"

    To override the site title for example, add the following:

    ```html
    <!-- overrides/main.html -->
    {​% extends "base.html" %}

    {​% block htmltitle %}
      <title>Lorem ipsum dolor sit amet</title>
    {​% endblock %}
    ```

## References

- [Mkdocs-Material ➤ Customization](https://squidfunk.github.io/mkdocs-material-insiders/customization/)
- [Mkdocs-Material ➤ Changing the logo and icons](https://squidfunk.github.io/mkdocs-material-insiders/setup/changing-the-logo-and-icons/)
- [Mkdocs ➤ Styling ➤ Using the theme `custom_dir`](https://www.mkdocs.org/user-guide/styling-your-docs/#using-the-theme-custom_dir)

just partials test

<!-- >Includes -->
{% include 'abbreviations.md' %}
<!-- Includes -->
