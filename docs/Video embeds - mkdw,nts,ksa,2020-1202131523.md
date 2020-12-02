# MKDW ➤ Video embeds

## Synopsis

Embedding gifs and video players are supported.

## Examples

=== "Gif"

    In
    : <space>
      ```
      ![[test gif.gif]]
      ```
      ```
      ![​[test gif.gif]]
      ```

    ---

    Out
    : <space>
      ![[test gif - mkdw,imgs,ksa,2020-1202132052.gif]]

=== "Youtube"

    In
    : <space>
      ```
      <iframe width="720" height="360" src="https://www.youtube.com/embed/
      9r-nbbTRCjQ" frameborder="0" allow="accelerometer; autoplay;
      clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen></iframe>
      ```

    ---

    Out
    : <space>
      <iframe width="720" height="360" src="https://www.youtube.com/embed/9r-nbbTRCjQ" frameborder="0" allow="accelerometer; autoplay;clipboard-write; encrypted-media; gyroscope; picture-in-picture"allowfullscreen></iframe>

=== "Loom"

    In
    : <space>
      ```
      <iframe width="720" height="360" src="https://www.loom.com/embed/
      8eba9957e00f482797dfcbe2fa93ce3b" frameborder="0" webkitallowfullscreen
      mozallowfullscreen allowfullscreen></iframe>
      ```

    ---

    Out
    : <space>
      <iframe width="720" height="360" src="https://www.loom.com/embed/8eba9957e00f482797dfcbe2fa93ce3b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
