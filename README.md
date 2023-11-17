
![bloomify](https://github.com/Hani-K/Bloomify/assets/16754560/4cf18bbb-a741-44cf-9d6a-c3fb8a72f79b)


# Bloomify
Bloom Filter generator and a list checker and manipulator using MurMurHash3 algorithm.
This is an efficient way to check against a long list of items without being resources demanding.

## Use Case
- Determine whether a password is likely to be part of a known compromised set without storing the actual passwords.
- Identify whether a particular URL is malicious or part of a blacklist.
- Check for spelling and quickly eliminate non-words, reducing the computational load when checking whether a word is spelled correctly.
- Determine whether a destination IP address is in a routing table.
- Identify and eleminate potential duplicate records before performing more resource-intensive operations.
- DNA sequence analysis to check for the presence of certain sequences or patterns in a large dataset.

## False Positive Rate
The optimal false positive rate is calculated automatically using the number of lines of the input list.
This optimal value gives a good balance between the size of the bloom filter and a very low false positivity.
You can however always choose to input a manual value.

## Usage
#### Install Python
Ubuntu/Debian: `sudo apt update && sudo apt install python3`

Fedora: `sudo dnf install python3`

CentOS: `sudo yum install python3`

Arch Linux: `sudo pacman -S python`

#### Install Dependencies
```
pip install bitarray
pip install mmh3
```

#### Usage
```bash
chmod +x BLOOMIFY.py
./BLOOMIFY.py
```

## Documentation
Coming Soon.
