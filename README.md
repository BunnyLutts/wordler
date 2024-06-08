# Worlder: A program to solve the ~~world~~ wordle

run wordler to solve normal wordle:

```bash
python wordler.py
```

run wordler with a larger dictionary[^1]:

``` python
import wordler
wordler.readDict('words_alpha.txt')
wordler.runGame()
```

If you want to skipped the guess by program, just press CTRL-C

[^1]: Dict from [this respository](https://github.com/dolph/dictionary)

## How does it works

The idea is basically choose a move that reduces the most choices in expectation each time.

In brief, we choose a word $w$ that minize $\sum_{i} \frac{cnt_i}{tot} \times cnt_i$ where $cnt_i$ means the number of configurations of the results, and $tot$ is the current words that can be an answer.
