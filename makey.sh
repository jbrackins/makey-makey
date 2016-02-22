#!/bin/bash
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 NEW_PROJECT_NAME" >&2
  exit 1
fi
if ! [ -e "../$1" ]; then
  echo "$1 not found" >&2
  exit 1
fi
if ! [ -d "../$1" ]; then
  echo "$1 not a directory" >&2
  exit 1
fi

mkdir temp

echo "Generating $1 Project Files..."
./renamer.py $1

echo "Setting up $1/src directory for SOURCE files..."
mkdir ../$1/src
mv temp/temp.cpp ../$1/src/$1.cpp

echo "Setting up $1/inc directory for HEADER files..."
mkdir ../$1/inc
mv temp/temp.h ../$1/inc/$1.h

echo "Setting up $1/doc directory for DOXYGEN files..."
mkdir ../$1/doc
mv temp/temp.conf ../$1/doc/doxy.conf

echo "Setting up Makefile..."
mv temp/tempMakefile ../$1/Makefile

echo "Cleaning up..."
rm -rf temp