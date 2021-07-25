# openaltrainer

## Installation

This step is NOT ready

```bash
pip install openaltrainer
```

## Development

The project require only install tox and piptools in your user.

```bash
pip install tox pip-tools --user
```

The first time you want to use, install dependencies in a virtual folder `.tox` using tox with:

```bash
make env-create
```

Remember to compile `requirements.txt` if you add more dependencies in `requirements.in`:

```bash
make env-compile
```

## Run

In each terminal / IDE, remember load the environment before using it. In terminal:

```bash
source ./.tox/openaltrainer/bin/activate
```

And run the example:

```bash
TODO
```
