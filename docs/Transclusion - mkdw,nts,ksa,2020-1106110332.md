# MKDW ➤ Transclusion

## Synopsis

Include contents of another file within the working page.

??? info "Mkdocs configurations"

    Syntax: `-​-8<-- "filename.ext"`
    : <space>
        ```bash
        pip install mkdocs-material
        pip install mkdocs-material-extensions
        ```

        ```yaml
        # mkdocs.yml
        markdown_extensions:
            - pymdownx.snippets
        ```

        !!! success "Supports indentations."

        !!! fail "Doesn't support including parts of a file."

    ---

    Syntax: `{​% include "filename.ext" %}`
    : <space>
        ```bash
        pip install mkdocs-macros-plugin
        ```

        ```yaml
        # mkdocs.yml
        plugins:
            - macros
        ```

        !!! warning "Doesn't support including parts of a file, but you can create a custom macro that does just that."

        !!! warning "Doesn't support indentations, but you can create a custom macro that does just that."

## Examples

=== "Include entire file"

    In
    : <space>

        ````markdown
        This is my variables `.yml` file:

        ```yaml
        -​-8<-- "includes/vars.yml"
        ```
        ````

    ---

    Out
    : <space>

        This is the `.yml` file that contains some of my global variables:

        ```yaml
        --8<-- "includes/vars.yml"
        ```

=== "Include parts of file"

    In
    : <space>

        ```python
        # includes/main.py
        import os

        @env.macro
        def include_file(filename, start=0, stop=None, indent=0, spaces=2):
            """
            Include a file, optionally indicating start and stop (starts
            counting from 0). The path is relative to the top directory of
            the documentation project.
            """

            full_filename = os.path.join(env.project_dir, filename)
            with open(full_filename, 'r') as f:
                lines = f.readlines()
            line_range = lines[start:stop]
            return ((' ' * spaces) * indent).join(line_range)
        ```

        ````markdown
        <!-- docs/*.md -->
        Here's the CSS stylesheet for my the progess bar:

        ```
        {​{ include_file('docs/stylesheets/extra.css', start=23, stop=86, indent=4) }}
        ```
        ````

    ---

    Out
    : <space>

        Here's the CSS stylesheet for my the progess bar:

        ```
        {{ include_file('docs/stylesheets/extra.css', start=23, stop=86, indent=4) }}
        ```

=== "Include glossary"

    In
    : <space>

        ```markdown
        HTML is the language of the web.

        {​% include "glossary.md" %}
        ```

    ---

    Out
    : <space>

        HTML is the language of the web.

## References

- [Mkdocs-Material ➤ Snippets](https://squidfunk.github.io/mkdocs-material-insiders/reference/code-blocks/#snippets)
- [Pymdown-Extensions ➤ Snippets](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/)
- [Mkdocs-Macros ➤ Advanced Usage ➤ Including snippets in pages](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#including-snippets-in-pages)
- [Mkdocs-Macros ➤ Tips and tricks ➤ Include parts of files](https://mkdocs-macros-plugin.readthedocs.io/en/latest/tips/#i-would-like-to-include-a-text-file-from-line-a-to-line-b)
