# Test-structures

## Functions

The list data type has some more methods. Here are all of the methods of list objects:

list.**append**(x)
: <space>
    Add an item to the end of the list. Equivalent to `a[len(a):] = [x]`.

list.**extend**(iterable)
: <space>
    Extend the list by appending all the items from the iterable. Equivalent to `a[len(a):] = iterable`.

list.**insert**(i, x)
: <space>
    Insert an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to a.append(x).

list.**expand**(x)
: <space>
    Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.**pop**([i])
: <space>
    Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

???+ example "Example"

    An example that uses most of the list methods:

    ```
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    fruits.count('apple')

    fruits.count('tangerine')

    fruits.index('banana')

    fruits.index('banana', 4)  # Find next banana starting a position 4

    fruits.reverse()
    fruits

    fruits.append('grape')
    fruits

    fruits.sort()
    fruits

    fruits.pop()
    ```

    You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 1 This is a design principle for all mutable data structures in Python.

    Another thing you might notice is that not all data can be sorted or compared. For instance, [None, 'hello', 10] doesn’t sort because integers can’t be compared to strings and None can’t be compared to other types. Also, there are some types that don’t have a defined ordering relation. For example, 3+4j < 5+7j isn’t a valid comparison.

### In depth

```cpp
mathematics.add(int rhs, int lhs, char *color)
```
: <space>

    ???+ info "Synopsis"

        Performs subtraction on two the operands, `rhs`, `lhs`. Returns [`int`] result, colored in `color`.

    ???+ tldr "Details"

        === "Parameters"

            === "`rhs`"
                Right hand side operand.

            === "`lhs`"
                Left hand side operand.

            === "`color`"
                Color of the output. Takes:

                - `red`

                - `green`

                - `blue`

        === "Return"
            Integer (`int`). Subtraction result of: `rhs` - `lhs`.

        === "Exceptions"
            None.

        === "Source"
            ```
            mathematics.add(rhs, lhs) {
                return (rhs + lhs);
            }
            ```

    ???+ example "Examples"

        === "Simple"

            In
            : <space>
                ```
                mathematics.sub(4, 3)
                ```

            ---

            Out
            : <space>
                ```
                1
                ```

        === "Complex"

            In
            : <space>
                ```
                mathematics.sub(
                    mathematics.div(732, 2),
                    mathematics.add(3,4)
                )
                ```

            ---

            Out
            : <space>
                ```
                32
                ```

```cpp
mathematics.sub(int rhs, int lhs, char *color)
```
: <space>

    ???+ info "Synopsis"

        Performs subtraction on two the operands, `rhs`, `lhs`. Returns [`int`] result, colored in `color`.

    ???+ tldr "Details"

        === "Parameters"

            === "`rhs`"
                Right hand side operand.

            === "`lhs`"
                Left hand side operand.

            === "`color`"
                Color of the output. Takes:

                - `red`

                - `green`

                - `blue`

        === "Return"
            Integer (`int`). Subtraction result of: `rhs` - `lhs`.

        === "Exceptions"
            None.

        === "Source"
            ```
            mathematics.add(rhs, lhs) {
                return (rhs + lhs);
            }
            ```

    ???+ example "Examples"

        === "Simple"

            In
            : <space>
                ```
                mathematics.sub(4, 3)
                ```

            ---

            Out
            : <space>
                ```
                1
                ```

        === "Complex"

            In
            : <space>
                ```
                mathematics.sub(
                    mathematics.div(732, 2),
                    mathematics.add(3,4)
                )
                ```

            ---

            Out
            : <space>
                ```
                32
                ```

```cpp
mathematics.mul(int rhs, int lhs, char *color)
```
: <space>

    ???+ info "Synopsis"

        Performs subtraction on two the operands, `rhs`, `lhs`. Returns [`int`] result, colored in `color`.

    ???+ tldr "Details"

        === "Parameters"

            === "`rhs`"
                Right hand side operand.

            === "`lhs`"
                Left hand side operand.

            === "`color`"
                Color of the output. Takes:

                - `red`

                - `green`

                - `blue`

        === "Return"
            Integer (`int`). Subtraction result of: `rhs` - `lhs`.

        === "Exceptions"
            None.

        === "Source"
            ```
            mathematics.add(rhs, lhs) {
                return (rhs + lhs);
            }
            ```

    ???+ example "Examples"

        === "Simple"

            In
            : <space>
                ```
                mathematics.sub(4, 3)
                ```

            ---

            Out
            : <space>
                ```
                1
                ```

        === "Complex"

            In
            : <space>
                ```
                mathematics.sub(
                    mathematics.div(732, 2),
                    mathematics.add(3,4)
                )
                ```

            ---

            Out
            : <space>
                ```
                32
                ```

```cpp
mathematics.div(int rhs, int lhs, char *color)
```
: <space>

    ???+ info "Synopsis"

        Performs subtraction on two the operands, `rhs`, `lhs`. Returns [`int`] result, colored in `color`.

    ???+ tldr "Details"

        === "Parameters"

            === "`rhs`"
                Right hand side operand.

            === "`lhs`"
                Left hand side operand.

            === "`color`"
                Color of the output. Takes:

                - `red`

                - `green`

                - `blue`

        === "Return"
            Integer (`int`). Subtraction result of: `rhs` - `lhs`.

        === "Exceptions"
            None.

        === "Source"
            ```
            mathematics.add(rhs, lhs) {
                return (rhs + lhs);
            }
            ```

    ???+ example "Examples"

        === "Simple"

            In
            : <space>
                ```
                mathematics.sub(4, 3)
                ```

            ---

            Out
            : <space>
                ```
                1
                ```

        === "Complex"

            In
            : <space>
                ```
                mathematics.sub(
                    mathematics.div(732, 2),
                    mathematics.add(3,4)
                )
                ```

            ---

            Out
            : <space>
                ```
                32
                ```


### Highlight code

- "**Parameters**"
: <space>

    - "**`N-start`**"
    : <space>

        Counter starts counting at `N-start`.

            `hello`
            : <space>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.

            `world`
            : <space>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.

            `james`
            : <space>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.

    - "**`N-step`**"
    : <space>
        counter steps by `N-step`

    - "**`N-special`**"
    : <space>
        renders every `N-special` lines a darker grey color

- "Examples"
: <space>

    - "Number all lines"
    : <space>

        ``` {linenums="1"}
        try:
        with open(file, 'r') as rf:
            with open(f'copy_{filename}{ext}', 'w') as wf:
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            wf.write(
                re.sub(
                pattern = rgx_pat,
                repl    = custom_sub_fn,
                string  = rf_chunk
                )
            )
        except FileNotFoundError:
        print(f'Error: No such file or directory: \'{file}\'')
        ```

        ---

        ````
        ``` {linenums="1"}
        code
        ```
        ````

    - "Number every other line"

        **Render**
        : <space>

            ```{linenums="2 2"}
            try:
            with open(file, 'r') as rf:
                with open(f'copy_{filename}{ext}', 'w') as wf:
                chunk_size = 4096
                rf_chunk = rf.read(chunk_size)
                wf.write(
                    re.sub(
                    pattern = rgx_pat,
                    repl    = custom_sub_fn,
                    string  = rf_chunk
                    )
                )
            except FileNotFoundError:
            print(f'Error: No such file or directory: \'{file}\'')
            ```

        ---

        **Source**
        : <space>
            ````
            ``` {linenums="2 2"}
            code
            ```
            ````
