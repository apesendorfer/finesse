# Finesse Writing + AI Project

Project Team:
Alex and Ben

Supervisors:
Katy, Jaan

We have created a tool that looks at your writing, picks out imperfect word choice, and makes suggestions. We take a dataset of great writing, look at its tf_idf words, and only suggest from those. This tool is useful for editing your 4th draft or finding the perfect word. It’s an improvement over a thesaurus because it’s context dependent and fasttext trained. 

We also hope it can be a foundation for other word-recommendation tools that can check for racial and gender biased language or make other more tailored writing suggestions.

Our principles are speed, effectiveness, and creative choice. 


Example:
Input sentence: Tokarczuk postulates the book’s ambiguous and fluid nature in the few first pages, developing a narrator with a yearning for the past, present, and future.

Output:

Word: Tokarczuk POS: NNP
<ipython-input-121-6aa3b574028c>:25: RuntimeWarning: invalid value encountered in double_scalars
  current = dot(user_word_vec, arr[i]) / (norm(user_word_vec) * norm(arr[i]))
---
Word: postulates POS: VBZ
argues
contradicts
suggests
contends
underlies
---
Word: the POS: DT
every
half
---
Word: book POS: NN
novel
author
ERROR: pos dictionary
read
chapter
autobiography
---
Word: 's POS: POS
---
Word: ambiguous POS: JJ
vague
confusing
contradictory
unclear
nebulous
---
Word: and POS: CC
---
Word: fluid POS: JJ
osmotic
bodily
---
Word: nature POS: NN
essence
wildness
beauty
mutability
sacredness
---
Word: in POS: IN
near
around
---
Word: the POS: DT
every
half
---
Word: few POS: JJ
several
many
countless
little
plenty
---
Word: first POS: JJ
second
third
last
next
seventh
---
Word: pages POS: NNS
chapters
links
ERROR: pos dictionary
biographies
sections
illustrations
---
Word: , POS: ,
---
Word: developing POS: VBG
creating
improving
establishing
adapting
acquiring
---
Word: a POS: DT
---
Word: narrator POS: NN
ERROR: pos dictionary
ERROR: pos dictionary
heroine
author
reader
listener
writer
---
Word: with POS: IN
along
alongside
despite
amidst
amid
---
Word: a POS: DT
---
Word: yearning POS: NN
longing
desire
hankering
craving
wistfulness
---
Word: for POS: IN
besides
except
---
Word: the POS: DT
every
half
---
Word: past POS: NN
decade
year
week
time
month
---
Word: , POS: ,
---
Word: present POS: JJ
past
future
given
---
Word: , POS: ,
---
Word: and POS: CC
---
Word: future POS: NN
potential
possibility
past
promise
fruition
---
Word: . POS: .
---
