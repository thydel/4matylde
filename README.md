# enumerate.py

- compter de 0 à 99 en base 10 (10^2)

```bash
./enumerate.py 0123456789 2
```

- Compter de 0 à 31 en base 2 (2^5)

```bash
./enumerate.py 01 5
```

- Compter de AAAA à GGGG, de 0 à 255 (4^4) en nucléotide

```bash
./enumerate.py ATCG 4
```

- Une session

```console
$ ./enumerate.py ATCG 4 | wc -l
256
$ ./enumerate.py ATCG 4 | head
AAAA
AAAT
AAAC
AAAG
AATA
AATT
AATC
AATG
AACA
AACT
$ ./enumerate.py ATCG 4 | tail
GGTC
GGTG
GGCA
GGCT
GGCC
GGCG
GGGA
GGGT
GGGC
GGGG
```
