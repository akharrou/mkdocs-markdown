# MKDW ➤ Images

## Synopsis

Images are supported with the `![alt](path)` syntax, and with third party plugins, wiki-link syntax `![[​img|alt]]` also becomes available.

??? warning "Mkdocs Only Feature"

        With the [Attribute List](https://python-markdown.github.io/extensions/attr_list/) extension, you can add HTML attributes and CSS classes to markdown elements, such as images. You can use this to align images easily.

        Enabled via `mkdocs.yml`:

        ```yaml
        markdown_extensions:
          - attr_list
        ```

## Examples

=== "Default"

    In
    : <space>
      ```
      ![](_assets/lion.jpg)
      ```
      ```
      ![[​lion.jpg]]
      ```

    ---

    Out
    : <space>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. <br><br>![[lion.jpg]]<br><br>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Interdum posuere lorem ipsum dolor sit. Vitae nunc sed velit dignissim sodales ut eu sem. Justo eget magna fermentum iaculis eu. Viverra nam libero justo laoreet sit. Eget magna fermentum iaculis eu. Scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Aliquet bibendum enim facilisis gravida neque convallis a cras. Sit amet porttitor eget dolor morbi non arcu risus quis. Aliquam purus sit amet luctus venenatis lectus magna fringilla. Urna nec tincidunt praesent semper feugiat nibh sed. Commodo quis imperdiet massa tincidunt nunc pulvinar. Euismod nisi porta lorem mollis aliquam ut porttitor leo. Arcu cursus euismod quis viverra. Euismod nisi porta lorem mollis aliquam ut porttitor leo a.

=== "Right Aligned"

    In
    : <space>
      ```
      ![](_assets/lion.jpg){: align=right}
      ```
      ```
      ![[​lion.jpg]]{: align=right}
      ```

    ---

    Out
    : <space>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      <br>
      ![[lion.jpg]]{: align=right}
      <br>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Interdum posuere lorem ipsum dolor sit. Vitae nunc sed velit dignissim sodales ut eu sem. Justo eget magna fermentum iaculis eu. Viverra nam libero justo laoreet sit. Eget magna fermentum iaculis eu. Scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Aliquet bibendum enim facilisis gravida neque convallis a cras. Sit amet porttitor eget dolor morbi non arcu risus quis. Aliquam purus sit amet luctus venenatis lectus magna fringilla. Urna nec tincidunt praesent semper feugiat nibh sed. Commodo quis imperdiet massa tincidunt nunc pulvinar. Euismod nisi porta lorem mollis aliquam ut porttitor leo. Arcu cursus euismod quis viverra. Euismod nisi porta lorem mollis aliquam ut porttitor leo a.<br><br>Proin sed libero enim sed faucibus turpis in eu. Duis at consectetur lorem donec massa sapien faucibus et. Laoreet non curabitur gravida arcu ac tortor dignissim. Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras. Semper viverra nam libero justo laoreet sit amet.

=== "Left Aligned, Sized"

    In
    : <space>
      ```
      ![](_assets/lion.jpg){: align=left style=width:40% }
      ```
      ```
      ![[​lion.jpg]]{: align=left style=width:40% }
      ```

    ---

    Out
    : <space>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      <br>
      ![[lion.jpg]]{: align=left style=width:40% }
      <br>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Interdum posuere lorem ipsum dolor sit. Vitae nunc sed velit dignissim sodales ut eu sem. Justo eget magna fermentum iaculis eu. Viverra nam libero justo laoreet sit. Eget magna fermentum iaculis eu. Scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Aliquet bibendum enim facilisis gravida neque convallis a cras. Sit amet porttitor eget dolor morbi non arcu risus quis. Aliquam purus sit amet luctus venenatis lectus magna fringilla. Urna nec tincidunt praesent semper feugiat nibh sed. Commodo quis imperdiet massa tincidunt nunc pulvinar. Euismod nisi porta lorem mollis aliquam ut porttitor leo. Arcu cursus euismod quis viverra. Euismod nisi porta lorem mollis aliquam ut porttitor leo a.<br><br>Proin sed libero enim sed faucibus turpis in eu. Duis at consectetur lorem donec massa sapien faucibus et. Laoreet non curabitur gravida arcu ac tortor dignissim. Tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras.

=== "Centered, Sized, Captioned"

    In
    : <space>
      ```
      <figure>
        <img src="../_assets/lion.jpg" style="width:80%" />
        <figcaption>Image caption</figcaption>
      </figure>
      ```

    ---

    Out
    : <space>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      <br><br>
      <figure>
        <img src="../_assets/lion.jpg" style="width:80%" />
        <figcaption>Image caption</figcaption>
      </figure>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quisque id diam vel quam elementum pulvinar. Orci nulla pellentesque dignissim enim. Magna fringilla urna porttitor rhoncus dolor purus. Mollis nunc sed id semper risus in hendrerit gravida rutrum.

## References

- [Mkdocs-Material ➤ Images](https://squidfunk.github.io/mkdocs-material-insiders/reference/images/)
