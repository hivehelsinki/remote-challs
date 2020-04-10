<h1 align="center"><code>Chall05 / Philosophy</code></h1>

<div align="center">
  <sub>Created by <a href="https://github.com/jgengo">Jordane Gengo (Titus)</a>, <a href="">Oleksii Martynovskyi (Disky)</a>, <a href="">Paula Lantran (Ablette)</a></sub>
</div>
<div align="center">
  <sub>From <a href="https://hive.fi">Hive Helsinki</a> for all the 42 Network</sub>
</div>

---

### Instructions

<sub>**Turn-in directory:** `chall05/`</sub><br />
<sub>**Files to turn in:** `<xlogin>.rb`</sub><br />
<sub>**Language:** `Ruby` *(specify the version you used in the top of your code commented)*</sub>
  
<sub>**Deadline:** 10.04.2020 - 10:42am</sub>
<br /><br />
### Subject
  
<p align="center">
  <img width="450" height="350" src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Jean-L%C3%A9on_G%C3%A9r%C3%B4me_-_Diogenes_-_Walters_37131.jpg">
</p>

Clicking on the first link in the main text of a Wikipedia article, and then repeating the process for subsequent articles, would usually lead to the Philosophy article. 

Code an executable ruby scripts that display the "road to philosophy".

You can either decide to detect loops or decide to skip the first link if you already visited it.

 <br /><br />
### Examples

```
[titus@pentest-lab ~ ]$ ./wikipedia.rb wdwdDowdwd
no wikipedia page for this word!
```


```
[titus@pentest-lab ~ ]$ ./wikipedia.rb Markdown
	Going to Lightweight_markup_language (counter: 1)
	Going to Markup_language (counter: 2)
	Going to Annotation (counter: 3)
	Going to Document (counter: 4)
	Going to Thought (counter: 5)
	Going to Ideas (counter: 6)
!!! Reach Philosophy !!!
```

```
[titus@pentest-lab ~]$ ./wikipedia.rb Pentesting
	Going to Cyberattack (counter: 1)
	Going to Computer (counter: 2)
	Going to Sequence (counter: 3)
	Going to Mathematics (counter: 4)
	Going to Ancient_Greek (counter: 5)
	Going to Greek_language (counter: 6)
	Going to Modern_Greek (counter: 7)
	Going to Dialect (counter: 8)
	Going to Latin (counter: 9)
	Going to Classical_language (counter: 10)
	Going to Language (counter: 11)
	Going to Grammar (counter: 12)
	Going to Linguistics (counter: 13)
	Going to Science (counter: 14)
Skip Latin, already seen this one
	Going to Knowledge (counter: 15)
	Going to Fact (counter: 16)
	Going to Reality (counter: 17)
	Going to Object_of_the_mind (counter: 18)
	Going to Object_(philosophy) (counter: 19)
!!! Reach Philosophy !!!
```

### Reward

 - The first one to submit a working solution will earn `20` points for their coalition.
 - Everyone else submitting a working solution *(not yet submitted)* will earn `7` points for their coalition.
 - Every participant that tried to solve the challenge and pushed a solution will earn `4` points for their coalition.
 
<br /><br />
Good luck!
