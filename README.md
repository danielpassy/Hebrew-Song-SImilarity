# Compare-Hebrew-Songs

## This project was discontinued


A lexical similarity analyzer and scrapper Hebrew song

Built on top of [YAP](https://github.com/onlplab/yap) and [scrappy](https://github.com/scrapy/scrapy)
<br>


It scraps Hebrew lyrics from shironet.mako.co.il/, and their [lemmas](https://en.wikipedia.org/wiki/Lemma_(morphology)) are extracted <br>
Lemmas are, acordding to wikipedia
>In morphology and lexicography, a lemma (plural lemmas or lemmata) is the canonical form,[1] dictionary form, or citation form of a set of words (headword). In English, for example, run, runs, ran and running are forms of the same lexeme
Songs are compared one against one, resulting in a similarity index <br>
The similarity index determine how many lemmas two songs have in common as follows.

The song A have similiraty index to the song B according to the following equation:
```
(lemmas in common)/(total distinct lemmas of A) = % simmilarity
```
Important to notice that the simmiliraty of (A,B) is different than the simmilarity of (B,A) as the second may contain more lemmas. <br>

To indicate real simmiliraty, we may use the average of the two simmilarities
```
(Similarity(A,B) + Similiratity (B,A)) 2/ 2
```


## Contributions
Contributions are welcome.
Just make sure to write the appropriate tests.

## License
[MIT](https://choosealicense.com/licenses/mit/)


