# Duskline Ridiculous

Entry for the make.fun bounty **"Ridiculous at First Glance, Real by the Second"**
(`u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a`).

## The entry

> We sell tiny coffins and eulogies for dead houseplants, because plant parents who just killed their third fern will pay $29 for a proper goodbye.

One sentence, 145 characters. The odd thing being sold: tiny coffins and eulogies
for dead houseplants. Who pays: plant parents who just killed their third fern.
Why it holds together: the pet-memorial market already proves people pay for a
proper goodbye to something they loved — houseplants are the next, cheaper,
far more numerous grief, and $29 turns guilt into a ritual instead of a bin.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
```

Python 3.13, standard library only. The program writes only to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and refuses with exit 1
if that directory is inside the repository, since the grader sandbox mounts
the repo read-only.

## License

MIT — see `LICENSE`.
