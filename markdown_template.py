MARKDOWN_TEMPLATE = """# {filename}

## Overview

(Placeholder for a brief description of the code file)

## Key Components

(Placeholder for a list of primary functions, classes, or modules)

## Important Variables/Constants

(Placeholder for descriptions of critical variables or constants)

## Usage Examples

```fortran
(Placeholder for code snippets or examples)
```

## Dependencies and Interactions

(Placeholder for notes on dependencies and interactions with other parts of the code, or external libraries)
"""

if __name__ == '__main__':
    # This part is just for testing the template string.
    # It won't be executed by the agent but can be run locally.
    print("Markdown Template String:")
    print(MARKDOWN_TEMPLATE.format(filename="example_file.f90"))
