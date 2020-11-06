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

        !!! success "Preserves styling (e.g. being fenced) and indentations"

        !!! fail "Doesn't support including parts of a file"

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

        !!! success "You can create your own macro that includes parts of a file"

        !!! fail "Gives unexpected behavior when fenced and/or indented"

## Examples

=== "Include file"

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

=== "Include parts of file"

    In
    : <space>

        ```python
        # includes/main.py
        import os

        def define_env(env):
            """
            This is the hook for defining variables, macros and filters

            - variables: the dictionary that contains the environment variables
            - macro: a decorator function, to declare a macro.
            """

            @env.macro
            def include_file(filename, start_line=0, end_line=None):
                """
                Include a file, optionally indicating start_line and end_line
                (start counting from 0)
                The path is relative to the top directory of the documentation
                project.
                """
                full_filename = os.path.join(env.project_dir, filename)
                with open(full_filename, 'r') as f:
                    lines = f.readlines()
                line_range = lines[start_line:end_line]
                return '\n'.join(line_range)
        ```

        ````markdown
        <!-- *.md -->
        Here is the description:

        ```
        {​{ include_file('mkdocs.yml', 0, 4) }}
        ```
        ````

    ---

    Out
    : <space>

        !TODO

## References

- [Mkdocs-Material ➤ Snippets](https://squidfunk.github.io/mkdocs-material-insiders/reference/code-blocks/#snippets)
- [Pymdown-Extensions ➤ Snippets](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/)
- [Mkdocs-Macros ➤ Advanced Usage ➤ Including snippets in pages](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#including-snippets-in-pages)
- [Mkdocs-Macros ➤ Tips and tricks ➤ Include parts of files](https://mkdocs-macros-plugin.readthedocs.io/en/latest/tips/#i-would-like-to-include-a-text-file-from-line-a-to-line-b)

{% include "includes/glossary.md" %}
