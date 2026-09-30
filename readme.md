# Text File Utils

A Python module for working with Json files.

## Usage

This repository is intended to be included in other projects as a Git submodule.

From the root directory of an existing project, run:

```bash
git submodule add https://github.com/RandomGgames/json_file_utils
```

This adds the repository to your project.

You can then import the utilities directly:

```python
from json_file_utils import read_json_file, write_json_file
```

## Cloning a Project with the Submodule

When cloning a project that contains this repository as a submodule, use:

```bash
git clone --recurse-submodules <project-repository-url>
```

If the project has already been cloned, initialize the submodule with:

```bash
git submodule update --init --recursive
```

## Updating the Utilities

The parent project tracks a specific commit of this repository. To update to the latest remote commit:

```bash
git submodule update --remote
```
