#!/usr/bin/python
# -*- coding: UTF-8 -*-

def apply_patch(diffsrc, test_mode=0):
    return "cat " + (diffsrc + ["/dev/null"])[test_mode] + " | patch -d .tmp"

def run_pandoc(main_md):
    return (
        "pandoc -t context --template=src/template.pandoc " + main_md +
        "| sed -e s/subsubsection/section/ > " +
        ".tmp/${TARGET.file}"
        )

def link_src(alias):
    '''
    Current directory: build/a
    Link to src/a directory, assuming it exists.
    '''
    return "[ -L src ] || ln -s ../../src/" + alias + " src"
