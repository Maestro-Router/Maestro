# a-python-project-template

A Python project template.

Sources:

- [.gitignore](.gitignore): [Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
- [uv](https://docs.astral.sh/uv/) setup: [uv-fastapi-example](https://github.com/astral-sh/uv-fastapi-example)

## Developer environment setup

```bash
set -a; source .env; set +a
``` 

Create virtual environment:

```bash
uv sync
```

Available commands:

```bash
task --list
```

See [Taskfile.yml](Taskfile.yml)

...