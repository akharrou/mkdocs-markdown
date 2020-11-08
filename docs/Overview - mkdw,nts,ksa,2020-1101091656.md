# MKDW ➤ Overview

The following is an quick overview of the features that Markdown permits and the features that its extensions permit.

## Basic syntax

???+ tldr "[[Headings - mkdw,nts,ksa,2020-1108084619|Headings]]"

    Differentiate content heads with 6 different levels `##..`, `<h1>` through `<h6>`.

???+ tldr "[[Formatting - mkdw,nts,ksa,2020-1101125635|Formatting]]"

    Format text to _**emphasis**_ what you want to stand out, ^^underline^^, ~~strikethrough~~ and even ==highlight== text to your liking. Add [[Superscript and subscript - mkdw,nts,ksa,2020-1101104802|subscript to and superscript]] as desired (e.g. for chemistry: H~2~O). You can trademark (c) with [[Special characters - mkdw,nts,ksa,2020-1101131621|special characters]] and more.

    You even have access to the [[Critic-markup - mkdw,nts,ksa,2020-1101132021|critic-markup]] syntax allowing you to make corrections {~~edt~~>edit~~} on the fly or to make clear what changed in a file.


    You additionally have access to [[Math - mkdw,nts,ksa,2020-1101104905|math notation]] (e.g. LaTeX).

???+ tldr "[[Lists - mkdw,nts,ksa,2020-1101104845|Lists]]"

    You can create bullet, numbered, definition and even task lists on the fly.

???+ tldr "[[Code - mkdw,nts,ksa,2020-1106142858|Code]]"

    You can write `inline code` as well as

    ```
    code blocks
    ```

    super easily. You can add code syntax highlighting, number codeblock lines, highlight certain lines and go even beyond with custom CSS styling.

???+ tldr "[[Math - mkdw,nts,ksa,2020-1101104905|Math]]"

    Fullfil all your math needs with support for LaTeX math notation

    $$
    E(\mathbf{v}, \mathbf{h}) = -\sum_{i,j}w_{ij}v_i h_j - \sum_i b_i v_i - \sum_j c_j h_j
    $$

    \begin{align}
        p(v_i=1|\mathbf{h}) & = \sigma\left(\sum_j w_{ij}h_j + b_i\right) \\
        p(h_j=1|\mathbf{v}) & = \sigma\left(\sum_i w_{ij}v_i + c_j\right)
    \end{align}

    {>>totally know what that means<<}

???+ tldr "[[Tables - mkdw,nts,ksa,2020-1101095858|Tables]]"

    You can create tables:

    | Method      | Description                          |
    | ----------  | -----------------------------------  |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |

???+ tldr "[[Links - mkdw,nts,ksa,2020-1108081611|Links]]"

    You can cross-reference with links to local files as well as reference ouside sources with links to webpages.

???+ tldr "[[Images - mkdw,nts,ksa,2020-1101104836|Images]]"

    Insert helpful images or showcase your favorite ones:

    ![[lion.jpg]]

???+ tldr "[[Blockquotes - mkdw,nts,ksa,2020-1108085601|Blockquotes]]"

    Blockquotes:

    > Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    >> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    >>> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

## Extended syntax

???+ tldr "[[Footnotes - mkdw,nts,ksa,2020-1101104435|Footnotes]]"

    Add additional content[^1] without breaking the flow of your paragraphs with footnotes.

???+ tldr "[[Lists - mkdw,nts,ksa,2020-1101104845|Definition lists]]"

    Definition Lists
    :    Define away all your terms and parameters with definition lists.

???+ tldr "[[Lists - mkdw,nts,ksa,2020-1101104845|Task lists]]"

    - [x] Jot down tasks and check them out when completed with task lists.

## Python markdown syntax

???+ tldr "Emojis and icons"

    Capture your emotions and moods with emojis 👑 😎 🎩 . [[Mkdocs - mkdw,nts,ksa,2020-1101200211|MkDocs]] :octicons-heart-fill-24:{: .heart } :bootstrap-emoji-sunglasses:{: .heart} !

???+ tldr "[[Abbreviations and glossaries - mkdw,nts,ksa,2020-1105182229|Abbreviations and glossaries]]"

    You can finally stop confusing your audience or save them a journey of looking things up by making glossaries. Glossary terms will be underlined and will have definitions show up when users hover over them.

???+ tldr "[[Admonitions and details - mkdw,nts,ksa,2020-1031114253|Admonitions and details]]"

    ???+ warning "Warning, very useful ! {>>and addictive<<}"

        Create admonitions (callouts) and hide away details with decorated collapsible or non-collapsible content blocks.

    !!! quote

        "I am the wiset man alive, for I know one thing, and that is that I know nothing."
        -- Plato

???+ tldr "[[Tabs - mkdw,nts,ksa,2020-1106091728|Tabs]]"

    === "Tab"
        Write content horizontally with browser-like tabs

    === "More tabs"
        You get the point.

???+ tldr "[[Transclusion - mkdw,nts,ksa,2020-1106110332|Transclusion]]"

    Reuse (include) content straight from other files and save your self a few minutes or days.

???+ tldr "[[Keyboard keys - mkdw,nts,ksa,2020-1106100206|Keyboard keys]]"

    Fancy keyboard keys.

    !!! info "Did you know"

        You can press ++f++ or ++slash++ to search anything across this documentation.

???+ tldr "[[Buttons - mkdw,nts,ksa,2020-1106101115|Buttons]]"

    Fancy [Buttons](){: .md-button } !

???+ tldr "[[Diagrams - mkdw,nts,ksa,2020-1106222521|Diagrams]]"

    Didn't even {~~believe~>BELIEVE~~} this one either, but you can generate diagrams from code... [Mermaid style](https://mermaid-js.github.io/mermaid/).

    === "Like this one"

        ![[mermaid flowcharts - mkdw,imgs,ksa,2020-1106223024.jpg]]

    === "Or this one"

        ![[mermaid class diagrams - mkdw,imgs,ksa,2020-1106223158.jpg]]

    === "Or even this one"

        ![[mermaid state diagram - mkdw,imgs,ksa,2020-1106223300.jpg]]

???+ tldr "[[Meta tags - mkdw,nts,ksa,2020-1101104945|Meta tags]]"

    You can have meta data at the top of each page:

    ```yaml
    ---
    title: MKDW ➤ Overview
    description: overview of markdown features
    authors: $Your's\space Truely$
    ---
    ```

???+ tldr "[[Macros and variables - mkdw,nts,ksa,2020-1101105007|Macros and variables]]"

    And last but not least, the ==**most powerful feature of all**==: the ability to create and access global/local variables, support for Jinja templating straight from inside your Markdown page, and the ability to create custom {>>Python<<} macros (functions) and call them from Jinja templates.

    **TL;DR**
    :   Basically you can turn your Markdown file into a full fledged application {>>, kinda<<}.

## References

- [Markdown Guide ➤ Basic Syntax](https://www.markdownguide.org/basic-syntax)
- [Markdown Guide ➤ Extended Syntax](https://www.markdownguide.org/extended-syntax)
- [Python Markdown](https://python-markdown.github.io/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
- [Mkdocs-Material](https://squidfunk.github.io/mkdocs-material-insiders/)

<!-- Foonotes -->
[^1]: additional footnote content
<!-- >Foonotes -->

<!-- Includes -->
{% include "includes/glossary.md" %}
<!-- >Includes -->
