# BookBot

BookBot is a simple Python tool that analyzes books (in .txt format) and provides word and character statistics.

## Features

- **Word Count**: Counts the total number of words in a text file.
- **Character Frequency**: Counts the frequency of each alphabetic character (case-insensitive) and displays them sorted by frequency in descending order.

## Usage

To use BookBot, run the script with a path to a text file as an argument:

```bash
python3 main.py <path_to_book>
```

For example:

```bash
python3 main.py books/frankenstein.txt
```

## Output Example

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78147 total words
--------- Character Count -------
e: 46043
t: 29427
a: 26743
o: 25552
i: 24687
n: 24367
s: 21263
h: 19709
r: 18603
d: 16863
l: 12739
u: 10424
m: 10616
c: 9241
w: 7953
f: 8731
y: 7912
p: 6517
g: 5974
b: 5027
v: 3833
k: 1755
x: 677
j: 504
q: 324
z: 243
============= END ===============
```

## Requirements

- Python 3.x

## Files

- `main.py`: The main script to run the analysis.
- `stats.py`: Contains helper functions for counting words and characters.
- `books/`: Directory containing sample text files (e.g., Frankenstein, Moby-Dick, Pride and Prejudice).

## Contributing

Special thanks to [Boot.dev](https://www.boot.dev).
