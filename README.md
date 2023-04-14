# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/TUW-GEO/eotransform/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                     |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|--------------------------------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| src/eotransform/\_\_init\_\_.py                          |        1 |        0 |        0 |        0 |    100% |           |
| src/eotransform/\_version.py                             |        1 |        0 |        0 |        0 |    100% |           |
| src/eotransform/apply.py                                 |        9 |        0 |        0 |        0 |    100% |           |
| src/eotransform/collection\_transformation.py            |       18 |        0 |       16 |        1 |     97% |  13->exit |
| src/eotransform/protocol/\_\_init\_\_.py                 |        0 |        0 |        0 |        0 |    100% |           |
| src/eotransform/protocol/sink.py                         |        4 |        0 |        0 |        0 |    100% |           |
| src/eotransform/protocol/stream.py                       |        4 |        0 |        0 |        0 |    100% |           |
| src/eotransform/protocol/transformer.py                  |        9 |        0 |        0 |        0 |    100% |           |
| src/eotransform/result.py                                |       31 |        0 |        4 |        0 |    100% |           |
| src/eotransform/sinks/\_\_init\_\_.py                    |        0 |        0 |        0 |        0 |    100% |           |
| src/eotransform/sinks/filtered.py                        |        9 |        0 |        2 |        0 |    100% |           |
| src/eotransform/sinks/result.py                          |       12 |        0 |        2 |        0 |    100% |           |
| src/eotransform/sinks/sink\_to\_progress\_report.py      |       13 |        2 |        0 |        0 |     85% |       6-7 |
| src/eotransform/sinks/with\_performance\_clock.py        |       11 |        0 |        2 |        1 |     92% |  15->exit |
| src/eotransform/streamed\_process.py                     |       67 |        1 |       16 |        0 |     99% |        23 |
| src/eotransform/transformers/\_\_init\_\_.py             |        0 |        0 |        0 |        0 |    100% |           |
| src/eotransform/transformers/apply\_to\_enumeration.py   |       12 |        0 |        4 |        0 |    100% |           |
| src/eotransform/transformers/chain.py                    |        7 |        0 |        0 |        0 |    100% |           |
| src/eotransform/transformers/compose.py                  |       11 |        0 |        2 |        0 |    100% |           |
| src/eotransform/transformers/identity.py                 |        6 |        0 |        0 |        0 |    100% |           |
| src/eotransform/transformers/map.py                      |        9 |        0 |        0 |        0 |    100% |           |
| src/eotransform/transformers/repeat.py                   |        9 |        0 |        0 |        0 |    100% |           |
| src/eotransform/transformers/result.py                   |       18 |        0 |        2 |        0 |    100% |           |
| src/eotransform/transformers/send\_to\_stream.py         |       10 |        0 |        0 |        0 |    100% |           |
| src/eotransform/transformers/to\_tuple.py                |        6 |        0 |        0 |        0 |    100% |           |
| src/eotransform/transformers/with\_performance\_clock.py |       12 |        0 |        2 |        1 |     93% |  16->exit |
| src/eotransform/utilities/\_\_init\_\_.py                |        0 |        0 |        0 |        0 |    100% |           |
| src/eotransform/utilities/profiling.py                   |       58 |        1 |       10 |        2 |     96% |70, 72->75 |
|                                                **TOTAL** |  **347** |    **4** |   **62** |    **5** | **98%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/TUW-GEO/eotransform/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/TUW-GEO/eotransform/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/TUW-GEO/eotransform/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/TUW-GEO/eotransform/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FTUW-GEO%2Feotransform%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/TUW-GEO/eotransform/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.