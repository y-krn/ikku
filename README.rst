# Ikku
Discover haiku from text.

## Requirements
- Python 3.8.x+
- MeCab with IPADIC (e.g. `brew install mecab mecab-ipadic`)

## Example
### ikku.reviewer.Reviewer
Ikku::Reviewer class is the main interface for this library.

```python
import ikku
reviewer = Reviewer()
```

### ikku.reviewer.Reviewer#judge
Judge if given text is valid song or not.

```python
reviewer.judge("古池や蛙飛び込む水の音") #=> true
reviewer.judge("ああ古池や蛙飛び込む水の音ああ") #=> false
```

### ikku.reviewer.Reviewer#find
Find one valid song from given text.

```python
reviewer.find("ああ古池や蛙飛び込む水の音ああ")
#=> #<Ikku::Song>
```

### ikku.reviewer.Reviewer#search
Search all valid songs from given text.

```python
reviewer.search("ああ古池や蛙飛び込む水の音ああ天秤や京江戸かけて千代の春ああ")
#=> [
#     #<Ikku::Song>,
#     #<Ikku::Song>,
#   ]
```

### ikku.song.Song#phrases
Return an Array of phrases of `ikku.Node`.

```python
song.phrases #=> [["古池", "や"], ["蛙", "飛び込む"], ["水", "の", "音"]]
```

### Rule option
Pass `rule` option to change the measure rule (default: `[5, 7, 5]`).

```python
reviewer = Reviewer(rule = [4, 3, 5])
reviewer.judge("古池や蛙飛び込む水の音") #=> false
reviewer.judge("すもももももももものうち") #=> true
```
