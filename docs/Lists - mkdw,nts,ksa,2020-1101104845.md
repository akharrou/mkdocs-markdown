# MKDW ➤ Lists

## Synopsis

There are few types of lists:

- **Ordered**, **Unordered** lists (supported via standard Markdown)
- **Definition**, **Task** lists (supported via extensions)

??? info "Mkdocs configurations"

    ```bash
    pip install mkdocs-material
    pip install mkdocs-material-extensions
    ```

    ```yaml
    # mkdocs.yml
    markdown_extensions:
      - def_list
      - pymdownx.tasklist:
          custom_checkbox: true
          clickable_checkbox: true
      - pymdownx.superfences # enables nesting of content blocks within lists
    ```

## Examples

=== "Unordered lists"

    In
    : <space>
      ```
      * Item
          * Item
          * Item
              * Item
              * Item
          * Item
      ```

    ---

    Out
    : <space>

      * Item
          * Item
          * Item
              * Item
              * Item
          * Item

=== "Ordered lists"

    In
    : <space>
      ```
      1. Item
          1. Item
          2. Item
              1. Item
              2. Item
          3. Item
      ```

    ---

    Out
    : <space>

      1. Item
          1. Item
          2. Item
              1. Item
              2. Item
          3. Item

=== "Definition lists"

    In
    : <space>
      ```
      Symbol
      :   Lorem ipsum dolor sit amet, consectetur adipiscing elit,
          sed do eiusmod tempor incididunt ut.

      `math.add(int a, int b)`
      :   Lorem ipsum dolor sit amet, consectetur adipiscing elit,
          sed do eiusmod tempor incididunt ut.

      `param`
      :   Lorem ipsum dolor sit amet, consectetur adipiscing elit,
          sed do eiusmod tempor incididunt ut.
      ```

    ---

    Out
    : <space>

    Symbol
    : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut.

    `math.add(int a, int b)`
    : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut.

    `param`
    : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut.

=== "Task lists"

    In
    : <space>
      ```
      * [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
      * [ ] Vestibulum convallis sit amet nisi a tincidunt
          * [x] In hac habitasse platea dictumst
          * [x] In scelerisque nibh non dolor mollis congue sed et metus
          * [ ] Praesent sed risus massa
      * [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque
      ```

    ---

    Out
    : * [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
      * [ ] Vestibulum convallis sit amet nisi a tincidunt
          * [x] In hac habitasse platea dictumst
          * [x] In scelerisque nibh non dolor mollis congue sed et metus
          * [ ] Praesent sed risus massa
      * [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque

=== "Nesting"

    In
    : <space>

        ````
        - item

            ```
            nested code block
            ```

        - [x] Write specification

            ```
            nested code block
            ```

        Term
        :   <space>
            ```
            nested code block
            ```
        ````

    ---

    Out
    : <space>

        - item

            ```
            nested content block
            ```

        - [x] Write specification

            ```
            nested content block
            ```

        Term
        :   too much nesting messes up definition lists

## References

- [Mkdocs-Material ➤ Lists](https://squidfunk.github.io/mkdocs-material-insiders/reference/lists/)
- [Pymdown-extension ➤ Superfences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/)
