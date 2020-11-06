# MKDW ➤ Formatting

## Synopsis

Possible text formatting:

- [[Emphasis - mkdw,nts,ksa,2020-1101131959|Emphasis (bold, italic)]]
- [[Underline - mkdw,nts,ksa,2020-1101131945|Underline]]
- [[Strike-through - mkdw,nts,ksa,2020-1101131644|Strike-through]]
- [[Superscript and subscript - mkdw,nts,ksa,2020-1101104802|Superscript and subscript]]
- [[Special characters - mkdw,nts,ksa,2020-1101131621|Special characters]]
- [[Highlight marks - mkdw,nts,ksa,2020-1101115332|Highlighting marks]]
- [[Critic-markup - mkdw,nts,ksa,2020-1101132021|Critic-markup]]

??? info "Mkdocs configurations"

    ```bash
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    ```

    ```yaml
    # mkdocs.yml
    markdown_extensions:

      # improved emphasis
      - pymdownx.betterem:
          smart_enable: all

      # strike-through, subscript
      - pymdownx.tilde:
          smart_delete: true
          delete: true
          subscript: true

      # underline, superscript
      - pymdownx.caret:
          insert: true
          superscript: true

      # special characters
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

      # highlighting
      - pymdownx.mark:
          smart_mark: true

      # critic-markup
      - pymdownx.critic:
          mode: view
    ```

## Examples

=== "Bold, Italics, Highlight, Underline, Strike-through"

    In
    : <space>

        ```
        * *This was bolded*
        * **This was italicized**
        * ==This was highlighted==
        * ^^This was underlined^^
        * ~~This was striked-through~~
        * ==~~^^***This was bolded, italicized, highlighted, underlined and striked-through***^^~~==
        ```

    ---

    Out
    : <space>

      * *This was bolded*
      * **This was italicized**
      * ==This was highlighted==
      * ^^This was underlined^^
      * ~~This was striked-through~~
      * ==~~^^***This was bolded, italicized, highlighted, underlined and striked-through***^^~~==

=== "Superscript, Subscript"

    In
    : <space>

        ```
        - December 12^th^.
        - H~2~0
        - A^T^A
        ```

    ---

    Out
    : <space>

      - December 12^th^.
      - H~2~0
      - A^T^A

=== "Special characters"

    In
    : <space>

        ```
        (tm)
        (c)
        (r)
        +/-
        -->
        <--
        <-->
        =/=
        1/4
        1st 2nd 3rd 4th 12th
        ```

    ---

    Out
    : <space>

        (tm)
        (c)
        (r)
        +/-
        -->
        <--
        <-->
        =/=
        1/4
        1st 2nd 3rd 4th 12th

=== "Critic-markup"

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

- [Mkdocs-Material ➤ Formatting](https://squidfunk.github.io/mkdocs-material-insiders/reference/formatting/)
