#!/bin/bash
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 NEW_PROJECT_NAME" >&2
  exit 1
fi
if ! [ -e "$1" ]; then
  echo "$1 not found" >&2
  exit 1
fi
if ! [ -d "$1" ]; then
  echo "$1 not a directory" >&2
  exit 1
fi
echo "Setting up $1/src directory for SOURCE files"

echo "Setting up $1/inc directory for HEADER files"

echo "Setting up $1/doc directory for DOXYGEN files"

echo "Setting up Makefile"
