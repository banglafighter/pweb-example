#!/bin/bash

dependencies="dependencies"
source venv/Scripts/activate
for name in $( ls $dependencies ); do
  path="$dependencies/$name"
  cd "$path"
  python setup.py develop --uninstall
  python setup.py develop
  git pull
  cd ../..
  echo -e "\n\n\n"
done

