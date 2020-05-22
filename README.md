# ikku

Discover haiku from text.
Thanks to https://github.com/r7kamura/ikku

## Requirements

- Python 3.8.x+
- MeCab with IPADIC (e.g. `brew install mecab mecab-ipadic`)

## Installation

```zsh
pip install ikku
``` 

## Example

Reviewer is the main interface for this library.

```python
from ikku import Reviwer
reviewer = Reviewer()
```

Judge if given text is valid song or not.

```python
reviewer.judge("古池や蛙飛び込む水の音") #=> true
reviewer.judge("ああ古池や蛙飛び込む水の音ああ") #=> false
```

Find one valid song from given text.

```python
reviewer.find("ああ古池や蛙飛び込む水の音ああ")
#=> <class 'ikku.song.Song'>
```

Search all valid songs from given text.

```python
reviewer.search("ああ古池や蛙飛び込む水の音ああ天秤や京江戸かけて千代の春ああ")
#=> [
#     [<class 'ikku.song.Song'>],
#     [<class 'ikku.song.Song'>],
#   ]
```

Return an Array of phrases of ikku.node.Node.

```python
song.phrases #=> [["古池", "や"], ["蛙", "飛び込む"], ["水", "の", "音"]]
```

Pass `rule` option to change the measure rule (default: `[5, 7, 5]`).

```python
reviewer = Reviewer(rule = [4, 3, 5])
reviewer.judge("古池や蛙飛び込む水の音") #=> false
reviewer.judge("すもももももももものうち") #=> true
```