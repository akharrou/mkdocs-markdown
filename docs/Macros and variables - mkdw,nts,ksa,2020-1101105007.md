---
author: 'John Doe'
collaborators: [
  Steve Smith,
  Carla Beritt,
  Sam Walden
]
---
# MKDW ➤ Macros and variables

## Synopsis

In [MkDocs](https://www.mkdocs.org/), the [`mkdocs-macros-plugin`](https://github.com/fralau/mkdocs_macros_plugin) adds support for referencing variables, calling macros (functions) and supports [Jinja](https://jinja.palletsprojects.com/) templating directly from Markdown.

??? info "Mkdocs configurations"

    ```bash
    pip install mkdocs-macros-plugin
    ```

    ```yaml
    plugins:
      - macros
    ```

## Examples

=== "User Defined Variables"

    Regular variables can be **defined in five different ways**:

    1. **Global**, i.e. for the whole documentation project:
        1. (for designers of the website): in the **`mkdocs.yml` file**, under the extra heading
        2. (for contributors): in **external yaml** definition files
        3. (for programmers): in a **`main.py` file** (Python), by adding them to a dictionary
    2. **Local**, i.e. in each Markdown page (for contributors):
        1. in the **YAML header**
        2. **in the text**, with a `{​%set variable = value %}` statement

    === "(Global) `mkdocs.yml`"

        In
        : <space>
          ```yaml
          # mkdocs.yml
          extra:
              price: 12.50
              company:
                  name: Acme
                  address: acme@labs.com
                  website: www.acme.com
          ```
          ```
          <!-- *.md -->
          The price of the product is {​{ price }}.

          See [more information on the website]({​{ company.website }}).

          See <a href="{​{ company.website }}">more information on the website</a>.

          Contact us at {​{ company.address }}.
          ```

        ---

        Out
        : <space>

            The price of the product is {{ price }}. {{ company.website }}

            See [more information on the website]({{ company.website }}).

            See <a href="{{ company.website }}">more information on the website</a>.

            Contact us at {{ company.address }}.

    === "(Global) External `.yml`"

        In
        : <space>
          ```yaml
          # foo.yaml
          class:
            teacher: Sam Walten
            students: [
              John Doe,
              Steve Smith,
              Carla Dennis
            ]
          ```
          ```bash
          .
          ├── docs
          │   ├── index.md
          │   └── *.md
          ├── includes
          │   ├── foo.yaml
          │   └── bar.yml
          └── mkdocs.yml
          ```
          ```yaml
          # mkdocs.yml
          plugins:
              - macros:
                  include_yaml:
                    - includes/foo.yaml
                    - includes/bar.yml
          ```
          ```plaintext
          <!-- *.md -->
          Obj: `{​{ class }}`

          Today's class teacher will be {​{ class.teacher }}. {​{ class.students|length }} students
          will be attending the class, they are:
          {​%- for student in class.students -%}
            {​{ ", " if not loop.first }} {​{ "and " if loop.last }} {​{ student }}
          {​%- endfor -%}
          ```

            !!! note

                Upon loading, the plugin will read each yaml file in order and merge the variables with those read from the main configuration file. In case of conflicts, the latest value will override the earlier ones.

        ---

        Out
        : <space>

          Obj: `:::python {{ class }}`

          Today's class teacher will be {{ class.teacher }}. {{ class.students|length }} students will be attending the class, they are:
          {%- for student in class.students -%}
            {{ ", " if not loop.first }} {{ "and " if loop.last }} {{ student }}
          {%- endfor -%}
          .

    === "(Global) Python file"

        In
        : <space>
          ```python
          # includes/main.py
          def define_env(env):

            env.variables['greeting'] = 'Hello'
            env.variables['farewell'] = 'Goodbye'
          ```
          ```bash
          .
          ├── docs
          │   ├── index.md
          │   └── *.md
          ├── includes
          │   └── main.py
          └── mkdocs.yml
          ```
          ```yaml
          # mdkdocs.yml
          plugins:
             - macros:
                 module_name: includes/main
          ```
          ```markdown
          <!-- *.md -->
          {​{ greeting }} and {​{ farewell }} !
          ```

        ---

        Out
        : {{ greeting }} and {{ farewell }} !

    === "(Local) Page meta"

        Variables can be defined in the YAML header; locally scoped.

        In
        : <space>
          ```
          <!-- *.md -->
          ---
          author: '**==John Doe==**'
          collaborators: [
            Steve Smith,
            Carla Beritt,
            Sam Walden
          ]
          ---

          {​{ page.meta }}
          {​{ context(page.meta) | pretty }} # ouputs a pretty table

          The title of this page is "^^{​{ page.title }}^^", the main author
          is ==**{​{ page.meta.author }}**== and his main collaborators are:
          {​%- for user in page.meta.collaborators -%}
                {​{ ", " if not loop.first }} {​{ "and " if loop.last }} {​{ user }}
          {​%- endfor -%}
          . They a did a really great job.
          ```

        ---

        Out
        : Variable|Type|Content
          -|-|-
          author|str|'John Doe'
          collaborators|list|['Steve Smith', 'Carla Beritt', 'Sam Walden']
          git_revision_date_localized|str|'6 hours ago'

            The title of this page is "^^{{page.title}}^^", the main author is ==**{{ page.meta.author }}**== and his main collaborators are:
              {%- for user in page.meta.collaborators -%}
                {{ ", " if not loop.first }} {{ "and " if loop.last }} {{ user }}
              {%- endfor -%}
              . They a did a really great job.

    === "(Local) Page set"

        Variables can be defined in the text, with a `{​%set variable = value %}` statement; locally scoped.

        In
        : <space>
          ```
          <!-- *.md -->
          {​% set weather = 'cloudy' %}
          {​% set temperature = 12.5 %}

          Today it's the weather is ^^{​{ weather }}^^ and ^^{​{ temperature }}^^℃.
          ```

        ---

        Out
        : <space>
          {% set weather = 'cloudy' %}
          {% set temperature = 12.5 %}

          Today it's the weather is ^^{{ weather }}^^ and ^^{{ temperature }}^^℃.

=== "User Defined Macros/Filters"

      In
      : <space>
        ```python
        # includes/main.py
        def define_env(env):

          env.variables['greeting'] = 'Hello'
          env.variables['farewell'] = 'Goodbye'

          @env.macro
          def helloworld():
              return "Hello, world !"

          @env.filter
          def reverse(x):
              "Reverse a string (and uppercase)"
              return x.upper()[::-1]

          env.macro(len)
          env.filter(len, "flen")
        ```
        ```bash
        .
        ├── docs
        │   ├── index.md
        │   └── *.md
        ├── includes
        │   └── main.py
        └── mkdocs.yml
        ```
        ```yaml
        # mdkdocs.yml
        plugins:
            - macros:
                module_name: includes/main
        ```
        ```markdown
        <!-- *.md -->
        '{​{ helloworld() }}' is {​{ helloworld()|flen }} characters in length.
        '{​{ farewell }}' is {​{ len(farewell) }} characters in length !
        {​{ greeting | reverse }} is a funny word, real funny.
        ```

      ---

      Out
      : '{{ helloworld() }}' is {{ helloworld()|flen }} characters in length. '{{ farewell }}' is {{ len(farewell) }} characters in length ! {{ greeting | reverse }} is a funny word, real funny.

=== "Predefined Variables"

    === "config.*"

        In
        : <space>
          ```python
          {​{ config }}
          {​{ context(config) | pretty }} # ouputs a pretty table
          ```

        ---

        Out
        : Variable|Type|Content
          -|-|-
          config_file_path|str|'/Users/johndoe/things/mkdocs.yml'
          site_name|str|'Johndoe's Notes'
          nav|list|[{'Home': [{'Welcome': 'index.md'}]}, {'Notebooks': [{'': 'notebooks.md'}, {'Markdown (MKDW)': [{'MKDW ➤ Overview': 'Overview.md'}, {'MKDW ➤ Callouts': 'Callouts.md'}, {'MKDW ➤ Tables': 'Tables.md'}, {'MKDW ➤ Footnotes': 'Footnotes.md'}, {'MKDW ➤ Emojis and icons': 'Emojis and icons.md'}, {'MKDW ➤ Images': 'Images.md'}, {'MKDW ➤ Lists': 'Lists.md'}, {'MKDW ➤ Math notation': 'Math notation.md'}, {'MKDW ➤ Meta tags': 'Meta tags.md'}, {'MKDW ➤ Macros and variables': 'Macros and variables.md'}, {'MKDW ➤ Formatting': 'Formatting.md'}, {'MKDW ➤ Emphasis': 'Emphasis.md'}, {'MKDW ➤ Strike-through': 'Strike-through.md'}, {'MKDW ➤ Underline': 'Underline.md'}, {'MKDW ➤ Special characters': 'Special characters.md'}, {'MKDW ➤ Subscript': 'Subscript.md'}, {'MKDW ➤ Superscript': 'Superscript.md'}, {'MKDW ➤ Highlight marks': 'Highlight marks.md'}, {'MKDW ➤ Critic-markup': 'Critic-markup.md'}, {'MKDW ➤ Mkdocs': 'Mkdocs.md'}, {'MKDW ➤ Extending mkdocs-material': 'Extending mkdocs-material.md'}]}, {'LaTeX (LTEX)': [{'Waiting Room': 'tmp.md'}]}, {'Philosophy (PHLO)': [{'Waiting Room': 'tmp.md'}]}, {'Mathematics (MTH)': [{'Waiting Room': 'tmp.md'}]}, {'Physics (PHSC)': [{'Waiting Room': 'tmp.md'}]}]}]
          pages|NoneType|None
          site_url|str|'http://127.0.0.1:8000/'
          site_description|str|'Documentation website to capture the state of my knowledge and understanding.'
          site_author|str|'John Doe'
          theme|Theme|Theme(name='material', dirs=['/Users/johndoe/things/overrides', '/usr/local/lib/python3.9/site-packages/material', '/usr/local/lib/python3.9/site-packages/mkdocs/templates'], static_templates=['404.html', 'sitemap.xml'], language='en', direction=None, features=['navigation.tabs', 'navigation.instant'], palette=[{'scheme': 'default', 'primary': 'black', 'accent': 'deep purple'}], font={'text': 'Roboto', 'code': 'Roboto Mono'}, icon={'logo': 'material/apps', 'repo': 'fontawesome/brands/github'}, favicon='_assets/alfred.png', include_search_page=False, search_index_only=True)
          docs_dir|str|'/Users/johndoe/things/docs'
          site_dir|str|'/var/folders/xs/vs26qr452dsdx83w7zq_yp100000gn/T/mkdocs__jirv1h0'
          copyright|str|'Copyright © 2020 💎 johndoe'
          google_analytics|NoneType|None
          dev_addr|Address|Address(host='127.0.0.1', port=8000)
          use_directory_urls|bool|True
          repo_url|str|'https://github.com/johndoe/'
          repo_name|str|'💎 johndoe'
          edit_uri|str|''
          extra_css|list|['css/timeago.css', 'stylesheets/extra.css']
          extra_javascript|list|['js/timeago.min.js', 'js/timeago.locales.min.js', 'js/timeago_mkdocs_material.js', 'javascripts/config.js', 'https://polyfill.io/v3/polyfill.min.js?features=es6', 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js']
          extra_templates|list|[]
          markdown_extensions|list|['toc', 'tables', 'fenced_code', 'abbr', 'meta', 'admonition', 'pymdownx.details', 'footnotes', 'def_list', 'pymdownx.tasklist', 'pymdownx.superfences', 'pymdownx.tabbed', 'pymdownx.inlinehilite', 'pymdownx.highlight', 'pymdownx.critic', 'pymdownx.betterem', 'pymdownx.caret', 'pymdownx.mark', 'pymdownx.tilde', 'pymdownx.smartsymbols', 'pymdownx.keys', 'pymdownx.arithmatex', 'pymdownx.snippets', 'pymdownx.emoji', 'attr_list']
          mdx_configs|dict|toc [dict], pymdownx.tasklist [dict], pymdownx.superfences [dict], pymdownx.highlight [dict], pymdownx.critic [dict], pymdownx.betterem [dict], pymdownx.caret [dict], pymdownx.mark [dict], pymdownx.tilde [dict], pymdownx.smartsymbols [dict], pymdownx.keys [dict], pymdownx.arithmatex [dict], pymdownx.snippets [dict], pymdownx.emoji [dict]
          strict|bool|False
          remote_branch|str|'gh-pages'
          remote_name|str|'origin'
          extra|SubConfig|{'social': [{'icon': 'fontawesome/brands/github', 'link': 'https://github.com/johndoe'}, {'icon': 'fontawesome/brands/twitter', 'link': 'https://twitter.com/_johndoe'}, {'icon': 'fontawesome/brands/linkedin', 'link': 'https://linkedin.com/in/johndoe/'}]}
          plugins|PluginCollection|search [SearchPlugin], git-revision-date-localized [GitRevisionDateLocalizedPlugin], add-number [AddNumberPlugin], exclude [Exclude], minify [MinifyPlugin], roamlinks [RoamLinksPlugin], macros [MacrosPlugin]

    === "page.*"

        In
        : <space>
          ```python
          {​{ page }}
          {​{ context(page) | pretty }} # ouputs a pretty table
          ```

        ---

        Out
        : Variable|Type|Content
          -|-|-
          file|File|page [Page], src_path = 'Macros and variables.md', abs_src_path = '/Users/johndoe/Macros and variables.md', name = 'Macros and variables', dest_path = 'Macros and variables/index.html', abs_dest_path = '/var/folders/xs/vs26qr452dsdx83w7zq_yp100000gn/T/mkdocs_r7aus56a/Macros and variables/index.html', url = 'Macros%20and%20variables/'
          title|str|'MKDW ➤ Macros and variables'
          parent|Section|title = 'Markdown (MKDW)', children = [Page(title='MKDW ➤ Overview', url='/Overview/'), Page(title='MKDW ➤ Callouts', url='/Callouts/'), Page(title='MKDW ➤ Tables', url='/Data%20tables/'), Page(title='MKDW ➤ Footnotes', url='/Footnotes/'), Page(title='MKDW ➤ Emojis and icons', url='/Emojis%20and%20icons/'), Page(title='MKDW ➤ Images', url='/Images/'), Page(title='MKDW ➤ Lists', url='/Lists/'), Page(title='MKDW ➤ Math notation', url='/Math%20notation/'), Page(title='MKDW ➤ Meta tags', url='/Meta%20tags/'), Page(title='MKDW ➤ Macros and variables', url='/Macros%20and%20variables/'), Page(title='MKDW ➤ Formatting', url='/Formatting/'), Page(title='MKDW ➤ Emphasis', url='/Emphasis/'), Page(title='MKDW ➤ Strike-through', url='/Strike-through/'), Page(title='MKDW ➤ Underline', url='/Underline/'), Page(title='MKDW ➤ Special characters', url='/Special%20characters/'), Page(title='MKDW ➤ Subscript', url='/Subscript/'), Page(title='MKDW ➤ Superscript', url='/Superscript/'), Page(title='MKDW ➤ Highlight marks', url='/Highlight%20marks/'), Page(title='MKDW ➤ Critic-markup', url='/Critic-markup/'), Page(title='MKDW ➤ Mkdocs', url='/Mkdocs/'), Page(title='MKDW ➤ Extending mkdocs-material', url='/Extending%20mkdocs-material/')], parent [Section], _Section__active = False, is_section = True, is_page = False, is_link = False
          children|NoneType|None
          previous_page|Page|Page(title='MKDW ➤ Meta tags', url='/Meta%20tags/')
          next_page|Page|Page(title='MKDW ➤ Formatting', url='/Formatting/')
          _Page__active|bool|False
          is_section|bool|False
          is_page|bool|True
          is_link|bool|False
          update_date|str|'2020-11-03'
          canonical_url|str|'http://127.0.0.1:8000/Macros%20and%20variables/'
          abs_url|str|'/Macros%20and%20variables/'
          edit_url|NoneType|None
          markdown|str|'# MKDW ➤ Macros and variables\n\n## Synopsis\n\n!!! warning "For [Mkdocs](https://www.mkdocs.org/) only !"\n\n The [`mkdocs-macros-plugin`](https://github.com/fralau/mkdocs_macros_plugin) adds support to reference variables, call macros (functions) and supports [Jinja](https://jinja.palletsprojects.com/) templating directly from Markdown.\n\n ...
          content|NoneType|None
          toc|list|[]
          meta|dict|author = 'John Doe', collaborators = ['Steve Smith', 'Carla Beritt', 'Sam Walden'], git_revision_date_localized = '7 hours ago'

    === "navigation.*"

        In
        : <space>
          ```python
          {​{ navigation }}
          {​{ context(navigation) | pretty }} # ouputs a pretty table
          ```

        ---

        Out
        : Variable|Type|Content
          -|-|-
          0|Section|title = 'Home', children = [Page(title='Welcome', url='/')], parent [NoneType], _Section__active = False, is_section = True, is_page = False, is_link = False
          1|Section|title = 'Notebooks', children = [Page(title='', url='/notebooks/'), Section(title='Markdown (MKDW)'), Section(title='LaTeX (LTEX)'), Section(title='Philosophy (PHLO)'), Section(title='Mathematics (MTH)'), Section(title='Physics (PHSC)')], parent [NoneType], _Section__active = False, is_section = True, is_page = False, is_link = False

    === "navigation.pages[*]"

        In
        : <space>
          ```python
          {​{ navigation.pages }}
          {​{ context(navigation.pages) | pretty }} # ouputs a pretty table
          ```

        ---

        Out
        : Variable|Type|Content
          -|-|-
          [Page(title='Welcome', url='/'), Page(title='', url='/notebooks/'), Page(title='MKDW ➤ Overview', url='/Overview/'), Page(title='MKDW ➤ Callouts', url='/Callouts/'), Page(title='MKDW ➤ Tables', url='/Data%20tables/'), Page(title='MKDW ➤ Footnotes', url='/Footnotes/'), Page(title='MKDW ➤ Emojis and icons', url='/Emojis%20and%20icons/'), Page(title='MKDW ➤ Images', url='/Images/'), Page(title='MKDW ➤ Lists', url='/Lists/'), Page(title='MKDW ➤ Math notation', url='/Math%20notation/'), Page(title='MKDW ➤ Meta tags', url='/Meta%20tags/'), Page(title='MKDW ➤ Macros and variables', url='/Macros%20and%20variables/'), Page(title='MKDW ➤ Formatting', url='/Formatting/'), Page(title='MKDW ➤ Emphasis', url='/Emphasis/'), Page(title='MKDW ➤ Strike-through', url='/Strike-through/'), Page(title='MKDW ➤ Underline', url='/Underline/'), Page(title='MKDW ➤ Special characters', url='/Special%20characters/'), Page(title='MKDW ➤ Subscript', url='/Subscript/'), Page(title='MKDW ➤ Superscript', url='/Superscript/'), Page(title='MKDW ➤ Highlight marks', url='/Highlight%20marks/'), Page(title='MKDW ➤ Critic-markup', url='/Critic-markup/'), Page(title='MKDW ➤ Mkdocs', url='/Mkdocs/'), Page(title='MKDW ➤ Extending mkdocs-material', url='/Extending%20mkdocs-material/'), Page(title='Waiting Room', url='/tmp/'), Page(title='Waiting Room', url='/tmp/'), Page(title='Waiting Room', url='/tmp/'), Page(title='Waiting Room', url='/tmp/')]|list|[Page(title='Welcome', url='/'), Page(title='', url='/notebooks/'), Page(title='MKDW ➤ Overview', url='/Overview/'), Page(title='MKDW ➤ Callouts', url='/Callouts/'), Page(title='MKDW ➤ Tables', url='/Data%20tables/'), Page(title='MKDW ➤ Footnotes', url='/Footnotes/'), Page(title='MKDW ➤ Emojis and icons', url='/Emojis%20and%20icons/'), Page(title='MKDW ➤ Images', url='/Images/'), Page(title='MKDW ➤ Lists', url='/Lists/'), Page(title='MKDW ➤ Math notation', url='/Math%20notation/'), Page(title='MKDW ➤ Meta tags', url='/Meta%20tags/'), Page(title='MKDW ➤ Macros and variables', url='/Macros%20and%20variables/'), Page(title='MKDW ➤ Formatting', url='/Formatting/'), Page(title='MKDW ➤ Emphasis', url='/Emphasis/'), Page(title='MKDW ➤ Strike-through', url='/Strike-through/'), Page(title='MKDW ➤ Underline', url='/Underline/'), Page(title='MKDW ➤ Special characters', url='/Special%20characters/'), Page(title='MKDW ➤ Subscript', url='/Subscript/'), Page(title='MKDW ➤ Superscript', url='/Superscript/'), Page(title='MKDW ➤ Highlight marks', url='/Highlight%20marks/'), Page(title='MKDW ➤ Critic-markup', url='/Critic-markup/'), Page(title='MKDW ➤ Mkdocs', url='/Mkdocs/'), Page(title='MKDW ➤ Extending mkdocs-material', url='/Extending%20mkdocs-material/'), Page(title='Waiting Room', url='/tmp/'), Page(title='Waiting Room', url='/tmp/'), Page(title='Waiting Room', url='/tmp/'), Page(title='Waiting Room', url='/tmp/')]

    === "environment.*"

        In
        : <space>
          ```python
          {​{ environment }}
          {​{ context(environment) | pretty }} # ouputs a pretty table
          ```

        ---

        Out
        : Variable|Type|Content
          -|-|-
          system|str|'MacOs'
          system_version|str|'10.15.7'
          python_version|str|'3.9.0'
          mkdocs_version|str|'1.1.2'
          macros_plugin_version|str|'0.4.18'
          jinja2_version|str|'2.11.2'

    === "git.*"

        In
        : <space>
          ```python
          {​{ git }}
          {​{ context(git) | pretty }} # ouputs a pretty table
          ```

        ---

        Out
        : Variable|Type|Content
          --|--|--
          status|bool|True
          date|datetime|datetime.datetime(2020, 11, 3, 12, 2, 2, tzinfo=tzoffset(None, 10800))
          short_commit|str|'60a9cs9'
          commit|str|'60a8419c82f5e0b08j3ha75549548ds90ef69fae'
          author|str|'johndoe'
          tag|str|''
          date_ISO|str|'2020-11-03 12:02:02 +0300'
          message|str|'message'
          raw|str|'commit 60a8419c82f5e0b08j3ha75549548ds90ef69fae\nAuthor: johndoe \nDate: Tue Nov 3 12:02:02 2020 +0300\n\n message'
          root_dir|str|'/Users/johndoe/repo'

    === "plugin.*"

        In
        : <space>
          ```python
          {​{ plugin }}
          {​{ context(plugin) | pretty }} # ouputs a pretty table
          ```

        ---

        Out
        : Variable|Type|Content
          -|-|-
          module_name|str|'main'
          include_dir|str|'includes'
          include_yaml|list|[]
          j2_block_start_string|str|''
          j2_block_end_string|str|''
          j2_variable_start_string|str|''
          j2_variable_end_string|str|''

## References

- [Mkdocs-Material ➤ Variables](https://squidfunk.github.io/mkdocs-material-insiders/reference/variables/)
- [`mkdocs-macros-plugin` ➤ Home](https://mkdocs-macros-plugin.readthedocs.io/)
