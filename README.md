<h1 align="center">Welcome to Gitcln 👋</h1>
<p>
  <a href="https://github.com/HadiZakiAlQattan/gitcln/actions?query=workflow%3ACI"><img alt="CI" src="https://github.com/HadiZakiAlQattan/gitcln/workflows/CI/badge.svg"/>
  </a>
  <a href="https://github.com/HadiZakiAlQattan/gitcln/actions?query=workflow%3ACD"><img alt="CD" src="https://github.com/HadiZakiAlQattan/gitcln/workflows/CD/badge.svg"/>
  </a>
  <a href="https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=HadiZakiAlQattan/gitcln&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/83e7567f13a3406a81bcc37f7f5289f6"/>
  </a>
  <a href="https://pypi.org/project/gitcln/" target="_blank">  
    <img alt="Version" src="https://img.shields.io/github/release/HadiZakiAlQattan/gitcln.svg" />
  </a>
  <a href="https://pypi.org/project/gitcln/"><img alt="Pyversions" src="https://img.shields.io/pypi/pyversions/gitcln.svg">
  </a>
  <a href="https://docutils.sourceforge.io/rst.html"><img alt="Docstrings: reStructuredText" src="https://img.shields.io/badge/docstrings-reStructuredText-gree.svg">
  </a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
  </a>
  <a href="https://github.com/HadiZakiAlQattan/sudoku/blob/master/LICENSE" target="_blank">  
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg" />
  </a>
</p>

> CLI tool aim to clean local git repository from .gitignore file(s)/folder(s).

> you can create or [download .gitignore](https://github.com/github/gitignore) file and use this tool anywhere.

# Installation ⚓

```shell 
$ pip install gitcln
```

# Usage 🗝

|Arg|Shortcut|Type|Description|Default|
|:---:|:---:|:---:|:---:|:---:|
|--directories|-d|optional|directory(ies) to ignore|[ ]|
|--files|-f|optional|file(s) to ignore|[ ]|
```shell 
$ gitcln --help
```
```shell
usage: gitcln [-h] [-d [DIRECTORIES [DIRECTORIES ...]]] [-f [FILES [FILES ...]]]

CLI tool aim to clean local git repository from .gitignore file(s)/folder(s).

optional arguments:

  -h, --help            show this help message and exit

  -d [DIRECTORIES [DIRECTORIES ...]], --directories [DIRECTORIES [DIRECTORIES ...]]
                        Directory(ies) to ignore. (default: [])

  -f [FILES [FILES ...]], --files [FILES [FILES ...]]
                        File(s) to ignore. (default: [])
```

### Examples : 

- Remove all .gitignore file(s)/folder(s) :
    ```shell 
    $ gitcln
    ```
- Remove all .gitignore file(s)/folder(s) except specific directory(ies) :
    ```shell 
    $ gitcln -d __pycache__
    ```
- Remove all .gitignore file(s)/folder(s) except specific file(s) :
    ```shell 
    $ gitcln -f bytes.pyc
    ```

# Tests 🧪

> Only integration tests for gitcln module runs on the CI pipeline.

# Roadmap 📈

* Add additional CLI option to skip .gitignore ignores by unique comment.
* Add .gitcln file to ignore file(s) folder(s) from scanning.
* Filter .gitignore by section name.

# Copyright ©

👤 **Hadi Zaki AlQattan**

* Github: [@HadiZakiAlQattan](https://github.com/HadiZakiAlQattan)
* Email: <alqattanhadizaki@gmail.com>

📝 **License**

Copyright © 2020 [Hadi Zaki AlQattan](https://github.com/HadiZakiAlQattan).<br />
This project is [MIT](https://github.com/HadiZakiAlQattan/sudoku/blob/master/LICENSE) licensed.

***
Give a ⭐️ if this project helped you!
