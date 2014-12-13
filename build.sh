#!/bin/bash
rm -rf build
mkdir build
cp avgrabber.py ./build/
cp install-deps.bat ./build
cp README.txt ./build
cp -R ./core ./build
cp -R ./utils ./build
cd build
zip -r avgrabber.zip *