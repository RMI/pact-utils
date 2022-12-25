# pact-utils
Utilities for working with Pathfinder Framework V2 files

## Flattening
You can use pact-util.py to convert PACT json to a flat csv file.

```
pip3 install pandas
```

Run thusly:

```
 python3 pact-util.py to_csv -i samples/pact-sample-max.json -o samples/pact-sample-max.csv
```
