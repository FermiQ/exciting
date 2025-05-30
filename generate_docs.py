#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates Markdown documentation from Fortran source files.
"""
import argparse
import os
import re
import sys

def parse_fortran_file(filepath):
    """
    Parses a Fortran file and extracts information for documentation.

    Args:
        filepath (str): Path to the Fortran source file.

    Returns:
        dict: A dictionary containing extracted information, or None if parsing fails.
              Keys: 'overview', 'components', 'variables', 'dependencies', 'calls', 'filename'
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        return None

    filename = os.path.basename(filepath)
    extracted_data = {
        'overview': [],
        'components': [],
        'variables': [],
        'dependencies': {'uses': [], 'calls': []},
        'filename': filename
    }

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except IOError as e:
        print(f"Error reading file {filepath}: {e}", file=sys.stderr)
        return None

    in_description_block = False

    for i, line_raw in enumerate(lines):
        line = line_raw.strip()

        # Overview
        if re.match(r"!\s*!DESCRIPTION:", line, re.IGNORECASE):
            in_description_block = True
            # Capture text after "! !DESCRIPTION:" on the same line if any
            match = re.match(r"!\s*!DESCRIPTION:(.*)", line, re.IGNORECASE)
            if match and match.group(1).strip():
                 extracted_data['overview'].append(match.group(1).strip())
            continue

        if in_description_block:
            if line.startswith("!"):
                # Remove the leading "!" and optional space
                comment_text = re.sub(r"^!\s?", "", line)
                if not comment_text.strip().startswith("!"): # Avoid lines like "!!" or "!!!" as start of content
                    extracted_data['overview'].append(comment_text)
                # If the line is just "!" or "!!", it might signify the end or a separator
                elif not comment_text.strip():
                    extracted_data['overview'].append("") # Keep empty lines for paragraph breaks
            else:
                # End of description block if a non-comment line is encountered
                in_description_block = False

        # Key Components
        # MODULE
        match = re.match(r"^\s*MODULE\s+([a-zA-Z_][a-zA-Z0-9_]*)", line, re.IGNORECASE)
        if match:
            extracted_data['components'].append(f"MODULE {match.group(1)}")
            continue # Avoid double parsing if it's also a variable line

        # SUBROUTINE
        match = re.match(r"^\s*(?:RECURSIVE\s+)?SUBROUTINE\s+([a-zA-Z_][a-zA-Z0-9_]*)", line, re.IGNORECASE)
        if match:
            extracted_data['components'].append(f"SUBROUTINE {match.group(1)}")
            continue

        # FUNCTION
        match = re.match(r"^\s*(?:RECURSIVE\s+)?(?:[a-zA-Z0-9_(),\s]+\s+)?FUNCTION\s+([a-zA-Z_][a-zA-Z0-9_]*)", line, re.IGNORECASE)
        if match:
            # Make sure it's not a type declaration like `TYPE(FUNCTION_POINTER) :: FP`
            if not re.match(r"^\s*TYPE\s*\(", line, re.IGNORECASE):
                 extracted_data['components'].append(f"FUNCTION {match.group(1)}")
            continue

        # Important Variables/Constants
        # Basic types, TYPE(), and PARAMETER
        # Covers: INTEGER :: var, REAL(8) :: var, TYPE(mytype) :: var, INTEGER, PARAMETER :: p = 1
        var_match = re.match(
            r"^\s*(TYPE\s*\(\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\)"  # TYPE(custom_type)
            r"|INTEGER(?:\s*\(.*?\))?"  # INTEGER or INTEGER(kind=...)
            r"|REAL(?:\s*\(.*?\))?"     # REAL or REAL(kind=...)
            r"|COMPLEX(?:\s*\(.*?\))?"  # COMPLEX or COMPLEX(kind=...)
            r"|LOGICAL(?:\s*\(.*?\))?"  # LOGICAL or LOGICAL(kind=...)
            r"|CHARACTER(?:\s*\(.*?\))?" # CHARACTER or CHARACTER(len=...)
            r")"
            r"(?:\s*,\s*(?:PARAMETER|ALLOCATABLE|DIMENSION\s*\(.*?\)|POINTER|TARGET|SAVE|INTENT\s*\(.*?\)))*" # Attributes
            r"\s*::\s*([a-zA-Z_][a-zA-Z0-9_]*(?:\s*\(.*?\))?(?:\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*(?:\s*\(.*?\))?)*)" # Variable names list
            r"(?:\s*=\s*.*?)?" # Optional initialization
            r"(\s*!.*)?$", # Optional comment group 3
            line, re.IGNORECASE
        )
        if var_match:
            declaration_part = line.strip()
            comment_part = ""
            # Corrected group index from 4 to 3 for the comment
            if var_match.group(3) and var_match.group(3).strip():
                comment_part = var_match.group(3).strip()
                # Remove comment from declaration part for cleaner output
                declaration_part = line_raw[:line_raw.find(comment_part)].strip()

            # If it's a parameter, format it slightly differently
            if "parameter" in declaration_part.lower():
                 extracted_data['variables'].append(f"`{declaration_part}` (Comment: {comment_part.lstrip('!') if comment_part else 'N/A'})")
            else:
                 extracted_data['variables'].append(f"`{declaration_part}` (Comment: {comment_part.lstrip('!') if comment_part else 'N/A'})")
            continue


        param_match = re.match(
            r"^\s*(INTEGER|REAL|LOGICAL|CHARACTER(?:\s*\(.*?\))?)\s*,\s*PARAMETER\s*::\s*([a-zA-Z_][a-zA-Z0-9_]*(?:\s*=\s*.*?)?(?:\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*(?:\s*=\s*.*?)?)*)"
            r"(\s*!.*)?$",
            line, re.IGNORECASE
        )
        if param_match:
            declaration_part = line.strip()
            comment_part = ""
            if param_match.group(3) and param_match.group(3).strip():
                comment_part = param_match.group(3).strip()
                declaration_part = line_raw[:line_raw.find(comment_part)].strip()

            extracted_data['variables'].append(f"`{declaration_part}` (Comment: {comment_part.lstrip('!') if comment_part else 'N/A'})")
            continue

        # Dependencies and Interactions
        # USE statements
        use_match = re.match(r"^\s*USE\s+([a-zA-Z_][a-zA-Z0-9_]*)", line, re.IGNORECASE)
        if use_match:
            module_name = use_match.group(1)
            if module_name.lower() != "intrinsic": # Exclude Fortran intrinsic modules if accidentally caught
                if module_name not in extracted_data['dependencies']['uses']:
                    extracted_data['dependencies']['uses'].append(module_name)
            continue

        # CALL statements
        call_match = re.match(r"^\s*CALL\s+([a-zA-Z_][a-zA-Z0-9_]*)", line, re.IGNORECASE)
        if call_match:
            subroutine_name = call_match.group(1)
            if subroutine_name not in extracted_data['dependencies']['calls']:
                 extracted_data['dependencies']['calls'].append(subroutine_name)
            continue

    # Clean up overview: remove leading/trailing empty strings
    while extracted_data['overview'] and not extracted_data['overview'][0]:
        extracted_data['overview'].pop(0)
    while extracted_data['overview'] and not extracted_data['overview'][-1]:
        extracted_data['overview'].pop(-1)

    return extracted_data

def generate_markdown(data, output_dir):
    """
    Generates a Markdown file from the extracted Fortran data.

    Args:
        data (dict): Dictionary of data extracted by parse_fortran_file.
        output_dir (str): Directory to save the Markdown file.
    """
    if not data:
        return

    md_filename = data['filename'] + ".md"
    md_filepath = os.path.join(output_dir, md_filename)

    os.makedirs(output_dir, exist_ok=True)

    with open(md_filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {data['filename']}\n\n")

        f.write("## Overview\n\n")
        if data['overview']:
            for line in data['overview']:
                f.write(f"{line}\n")
            f.write("\n")
        else:
            f.write("*No overview extracted.*\n\n")

        f.write("## Key Components\n\n")
        if data['components']:
            for comp in sorted(list(set(data['components']))): # Sort and unique
                f.write(f"- {comp}\n")
            f.write("\n")
        else:
            f.write("*No key components (modules, subroutines, functions) identified.*\n\n")

        f.write("## Important Variables/Constants\n\n")
        if data['variables']:
            for var in sorted(list(set(data['variables']))): # Sort and unique
                 # Ensure comments are handled cleanly
                if "(Comment: )" in var:
                    var = var.replace("(Comment: )", "(No comment)")
                elif "(Comment: N/A)" in var:
                    var = var.replace("(Comment: N/A)", "(No comment)")
                f.write(f"- {var}\n")
            f.write("\n")
        else:
            f.write("*No important variables or constants identified.*\n\n")

        f.write("## Usage Examples\n\n")
        f.write("*TODO: Add usage examples if applicable.*\n\n")
        # Stretch goal: Attempt to find calls to public routines defined in this file
        # This is a simplified heuristic
        # own_routines = [name.split()[-1] for name in data['components'] if name.startswith("SUBROUTINE") or name.startswith("FUNCTION")]
        # if own_routines and data['dependencies']['calls']:
        #     simple_examples = []
        #     for called_routine in data['dependencies']['calls']:
        #         if called_routine in own_routines:
        #             # This is very basic, would need full line for context
        #             simple_examples.append(f"CALL {called_routine}(...)")
        #     if simple_examples:
        #         f.write("**Potential internal calls (heuristic):**\n")
        #         for ex in sorted(list(set(simple_examples))):
        #             f.write(f"- `{ex}`\n")
        #         f.write("\n")


        f.write("## Dependencies and Interactions\n\n")
        f.write("**Uses:**\n")
        if data['dependencies']['uses']:
            for use in sorted(list(set(data['dependencies']['uses']))):
                f.write(f"- {use}\n")
        else:
            f.write("- *None identified.*\n")
        f.write("\n")

        f.write("**Calls:**\n")
        if data['dependencies']['calls']:
            for call in sorted(list(set(data['dependencies']['calls']))):
                f.write(f"- {call}\n")
        else:
            f.write("- *None identified.*\n")
        f.write("\n")

    print(f"Successfully generated Markdown: {md_filepath}")


def main():
    """Main function to handle argument parsing and script execution."""
    parser = argparse.ArgumentParser(description="Generate Markdown documentation from a Fortran source file.")
    parser.add_argument("fortran_file", help="Path to the Fortran source file (.f90, .F90, .f)")

    args = parser.parse_args()

    fortran_filepath = args.fortran_file
    output_directory = "docs/src_docs"

    if not os.path.exists(fortran_filepath):
        print(f"Error: Input Fortran file not found: {fortran_filepath}", file=sys.stderr)
        sys.exit(1)

    if not (fortran_filepath.endswith(".f90") or \
            fortran_filepath.endswith(".F90") or \
            fortran_filepath.endswith(".f")):
        print(f"Warning: Input file '{fortran_filepath}' does not have a typical Fortran extension (.f90, .F90, .f).", file=sys.stderr)

    # Ensure output directory exists
    try:
        os.makedirs(output_directory, exist_ok=True)
    except OSError as e:
        print(f"Error: Could not create output directory {output_directory}: {e}", file=sys.stderr)
        sys.exit(1)

    parsed_data = parse_fortran_file(fortran_filepath)

    if parsed_data:
        generate_markdown(parsed_data, output_directory)
    else:
        print(f"Could not parse Fortran file: {fortran_filepath}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
