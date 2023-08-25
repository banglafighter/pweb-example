#!/bin/bash

dependencies="dependencies"

source venv/Scripts/activate
for name in $( ls $dependencies ); do
  path="$dependencies/$name"
  cd "$path"
  git pull
  pip install -e .
  cd ..
done