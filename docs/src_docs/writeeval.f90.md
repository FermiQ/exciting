# writeeval.f90

## Overview

  Outputs the second-variational eigenvalues and occupation numbers to the
  file {\tt EIGVAL.OUT}.

  Created June 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE writeeval

## Important Variables/Constants

- `Integer :: ik, ist, is, ia, ias` (No comment)
- `Type (xmlf_t), Save :: xf` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- Fox_wxml
- modinput
- modmain

**Calls:**
- xml_AddAttribute
- xml_Close
- xml_EndElement
- xml_NewElement
- xml_OpenFile
