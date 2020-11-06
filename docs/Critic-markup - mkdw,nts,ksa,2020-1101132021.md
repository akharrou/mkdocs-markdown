# MKDW ➤ Critic-markup

## Synopsis

[Critic-markup](http://criticmarkup.com/) sytnax is supported.

!!! info "Mkdocs Configuration"

    Enable via `mkdocs.yml`:

    ```yaml
    markdown_extensions:
    - pymdownx.critic:
        mode: view
    ```

## Examples

=== "Basic"

    In
    : <space>

        ```
        Text can be {​--deleted--} and replacement text {​++added++}. This can also be
        combined into {​~~one~>a single~~} operation. {​==Highlighting==} is also
        possible {​>>and comments can be added inline<<}.

        {​==

        Formatting can also be applied to blocks, by putting the opening and closing
        tags on separate lines and adding new lines between the tags and the content.

        ==}
        ```

    ---

    Out
    : <space>

        Text can be {--deleted--} and replacement text {++added++}. This can also be
        combined into {~~one~>a single~~} operation. {==Highlighting==} is also
        possible {>>and comments can be added inline<<}.

        {==

        Formatting can also be applied to blocks, by putting the opening and closing
        tags on separate lines and adding new lines between the tags and the content.

        ==}

## References

- [Mkdocs-Material ➤ Formatting ➤ Critic](https://squidfunk.github.io/mkdocs-material-insiders/reference/formatting/?h=+mark#critic)
- [Pymdown-Extensions ➤ Critic](https://facelessuser.github.io/pymdown-extensions/extensions/critic/)
