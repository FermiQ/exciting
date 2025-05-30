# dbxcplot.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE dbxcplot

## Important Variables/Constants

- `Integer :: idm, is, ia, ias, ir` (No comment)
- `Real (8), Allocatable :: grfir (:, :)` (No comment)
- `Real (8), Allocatable :: grfmt (:, :, :, :)` (No comment)
- `Real (8), Allocatable :: rfir (:)` (No comment)
- `Real (8), Allocatable :: rfmt (:, :, :)` (No comment)
- `Real (8), Allocatable :: rvfir (:, :)` (No comment)
- `Real (8), Allocatable :: rvfmt (:, :, :, :)` (No comment)
- `type(plotlabels),pointer ::labels` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain
- modplotlabels

**Calls:**
- destroy_plotlablels
- gradrf
- init0
- plot1d
- plot2d
- plot3d
- readstate
- set_plotlabel_axis
