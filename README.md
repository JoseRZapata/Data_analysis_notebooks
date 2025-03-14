# Data analysis notebooks with python

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/charliermarsh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Test](https://github.com/JoseRZapata/Data_analysis_notebooks/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/JoseRZapata/Data_analysis_notebooks/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/JoseRZapata/Data_analysis_notebooks/graph/badge.svg?token=27YGHC6I19)](https://codecov.io/gh/JoseRZapata/Data_analysis_notebooks)

Jose Ricardo Zapata - <https://joserzapata.github.io/>

[![Invitame a un Cafe](https://img.buymeacoffee.com/button-api/?text=Invítame+a+un+Café&emoji=&slug=joserzapata&button_colour=328cc1&font_colour=ffffff&font_family=Comic&outline_colour=000000&coffee_colour=FFDD00)](https://www.buymeacoffee.com/joserzapata)

- Covid data plots with ploty
    - [Notebook](https://github.com/JoseRZapata/Data_analysis_notebooks/blob/main/notebooks/01-Covid19_visualization/01-Covid19_Visualizacion_es.ipynb)
    - [Blog post](https://joserzapata.github.io/post/covid19-visualizacion/)

## Repo cookiecutter Template

This repository uses the:

data-science-project-template - <https://github.com/JoseRZapata/data-science-project-template>

## 🗃️ Project structure

```bash
.
├── codecov.yml                         # configuration for codecov
├── .code_quality
│   ├── mypy.ini                        # mypy configuration
│   └── ruff.toml                       # ruff configuration
├── data
│   ├── 01_raw                          # raw immutable data
│   ├── 02_intermediate                 # typed data
│   ├── 03_primary                      # domain model data
│   ├── 04_feature                      # model features
│   ├── 05_model                        # model training, experimentation, and hyperparameter tuning.
│   ├── 06_evaluation                   # model training, evaluation, and hyperparameter tuning.
│   ├── 07_deploy                       # model packaging, deployment strategies.
│   ├── 08_reporting                    # reports, results, etc
│   └── README.md                       # description of the data structure
├── docs                                # documentation for your project
├── .editorconfig                       # editor configuration
├── .github                             # github configuration
│   ├── dependabot.md                   # github action to update dependencies
│   ├── pull_request_template.md        # template for pull requests
│   └── workflows                       # github actions workflows
│       ├── ci.yml                      # run continuous integration (tests, pre-commit, etc.)
│       ├── dependency_review.yml       # review dependencies
│       ├── docs.yml                    # build documentation (mkdocs)
│       └── pre-commit_autoupdate.yml   # update pre-commit hooks
├── .gitignore                          # files to ignore in git
├── Makefile                            # useful commands to setup environment, run tests, etc.
├── models                              # store final models
├── notebooks                           # All notebooks with analysis    
│   ├── notebook_template.ipynb         # template for notebooks
│   └── README.md                       # information about the notebooks
├── .pre-commit-config.yaml             # configuration for pre-commit hooks
├── pyproject.toml                      # dependencies for the project
├── README.md                           # description of your project
├── src                                 # source code for use in this project
├── tests                               # test code for your project
└── .vscode                             # vscode configuration
    ├── extensions.json                 # list of recommended extensions
    ├── launch.json                     # vscode launch configuration
    └── settings.json                   # vscode settings
```

## Credits

This project was generated from [@JoseRZapata]'s [data science project template] template.

---
[@JoseRZapata]: https://github.com/JoseRZapata

[data science project template]: https://github.com/JoseRZapata/data-science-project-template
