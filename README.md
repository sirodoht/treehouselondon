# treehouselondon

Housing Co-operatives & Intentional Communities Directory for London, UK

## Development

This project uses [rye](https://github.com/astral-sh/rye) for Python and dependencies
management.

```sh
rye sync
```

## Deploy

```
cd ansible/
rye run ansible-playbook -v playbook.yaml
```

## License

MIT
