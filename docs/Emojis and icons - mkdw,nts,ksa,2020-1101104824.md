# MKDW ➤ Emojis and icons

## Synopsis

Inline emojis are supported with the `:emoji:` syntax.

## Examples

=== "Emojis"

    In
    : <space>

        ```markdown
        - :smile: :heart: :thumbsup:
        ```

    ---

    Out
    : <space>

        - :smile: :heart: :thumbsup:

=== "SVG Icons"

    You can inline SVG icons with syntax similar to emojis (`:emoji:`) by referencing a valid path to any icon bundled with the theme which are located in the theme's `.icons/` directory or your custom `overrides/.icons/` directory.

    In
    : <space>

        ```css
        /* docs/stylesheets/extra.css */
        .twitter {
            color: #1DA1F2;
        }

        .heart {
            color: #E53935;
            animation: heart 1000ms infinite;
        }

        @keyframes heart {
            0%, 40%, 80%, 100% {
                transform: scale(1);
            }
            20%, 60% {
                transform: scale(1.15);
            }
        }
        ```

        ```yaml
        # mkdocs.yml
        extra_css:
          - stylesheets/extra.css
        ```

        ```markdown
        <!-- docs/*.md -->
        - :fontawesome-regular-laugh-wink:
        :fontawesome-brands-twitter:{: .twitter }
        :octicons-heart-fill-24:{: .heart }
        :bootstrap-emoji-sunglasses:{: .heart }
        ```

    ---

    Out
    : <space>

        - :fontawesome-regular-laugh-wink: – `:::bash .icons/fontawesome/regular-laugh-wink.svg`

        - :fontawesome-brands-twitter:{: .twitter } – `:::bash .icons/fontawesome/brands/twitter.svg`

        - :octicons-heart-fill-24:{: .heart } – `:::bash .icons/octicons/heart-fill-24.svg`

        - :bootstrap-emoji-sunglasses:{: .heart} – `:::bash overrides/.icons/bootstrap/emoji-sunglasses.svg`

## References

- [Pymdown-Extensions ➤ Emoji](https://facelessuser.github.io/pymdown-extensions/extensions/emoji/)
- [Mkdocs-Material ➤ Chaning the logo and icons](https://squidfunk.github.io/mkdocs-material-insiders/setup/changing-the-logo-and-icons/#additional-icons)
- [Mkdocs-Material ➤ Customization](https://squidfunk.github.io/mkdocs-material-insiders/customization/#extending-the-theme)
- [[Extending mkdocs-material - mkdw,nts,ksa,2020-1101214900|MKDW ➤ Extending `mkdocs-material`]]
