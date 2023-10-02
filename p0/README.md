## Project 0: Unix/Python Tutorial

### <a name="introduction">Introduction</a>

This project will cover the basics of working in the Unix environment and a small introduction to Python.
               In this course, we will only be using **Python 3**.
               You may remotely connect to the [SOE servers](https://support.soe.ucsc.edu/linux-servers) or use lab workstations as well as your own computer.

### Submission

To get you familiarized with the automatic grading system, we will ask you to submit answers for problems 1 ([`buyLotsOfFruit`](#buylotsoffruit)) and 2 ([`shopSmart`](#shopsmart)).
               The project may seem simple, but this is a good thing: learning the basics of Python now will save you many headaches later in the course.
               Take this easy project as an opportunity to **learn Python**.

Here is the code provided for this assignment: [p0.zip](p0.zip).

To submit your code, you will:
  Open up `config.json` and put your information in there:
     - `course` -- The current course you are enrolled in (already set).
     - `assignment` -- The current assignment you are working on (already set).
     - `server` -- The autograding server to submit assignment to (already set).
     - `user` -- Your username (email) for the autograder.
     - `pass` -- The password that was emailed to you in the beginning of this course.
                     If you didn't get the password, forgot it, etc; talk to a TA.

For example, Sammy Slug would have a `config.json` for P0 that looks like:

```json
    {
        "course": "CSE140",
        "assignment": "p0",
        "server": "http://lighthouse.soe.ucsc.edu",
        "user": "sslug@ucsc.edu",
        "pass": "1234567890"
    }
```

When you are ready to submit,
    you can do so using the command:

```sh
    python3 -m autograder.cli.submit buyLotsOfFruit.py shopSmart.py
```

This will take your `config.json`, `buyLotsOfFruit.py`, and `shopSmart.py` from your current directory and send them to the autograding server.    The autograderwill get your code and run a bunch of secret tests on it to assign you a grade.
It will return output formatted about the same as the local tests.

The autograder records all your submissions (the code, time, and
score).  The score you received on your most recent submission is
your current grade for the assignment (not counting late
assignments and manually graded components).

You can make as many attempts as you want.
However if we find you abusing the autograder (e.g. repeatedly failing tests that would have been caught by testing locally),
then you can lose points.
Any attempt to willingly circumvent the autograder (e.g. "hacking" it)
may result in an immediate F in this class and a referral for academic integrity.



### Resources

There are many great resources online for learning Unix and Python.

#### UNIX

* [UNIX Tutorial for Beginners](http://www.ee.surrey.ac.uk/Teaching/Unix/)
* [UNIX Tutorial](https://people.ischool.berkeley.edu/~kevin/unix-tutorial/toc.html)

#### Text Editors

Being familiar with a powerful text editor can make a surprising difference.
               In the programming world, there are two text editors that have stayed on the top for over 30 years.
               Vi (Vim) and Emacs are two very powerful terminal-based text editors (although both have GUI versions).
               The arguments about which one is better have been going on for decades and will never be resolved.
               In truth, they are both amazing editors and will greatly increase your productivity once you learn how to use them.
               There are also many online resources for each:

* Vim
  - [Interactive Vim Tutorial](https://www.openvim.com/)
  - [Visual Vim Tutorial](https://scotch.io/tutorials/getting-started-with-vim-an-interactive-guide)
  - [Vim Videos](http://derekwyatt.org/vim/tutorials/)
  - [Game-based Vim Tutorial](https://vim-adventures.com/)
* Emacs
  - [Practical Emacs Tutorial](http://ergoemacs.org/emacs/emacs.html)
  - [Another Emacs Tutorial](https://www.gnu.org/software/emacs/tour/)
  - [Visual Emacs Tutorial](http://www.jesshamrick.com/2012/09/10/absolute-beginners-guide-to-emacs/)

#### Git

Git is currently the most popular [Version Control System](https://en.wikipedia.org/wiki/Version_control), period.
               Learning how to use source control is a must for all programmers in today's world.
               We **strongly** encourage all students to use source control for their coursework.
               Of course, keep your repositories private so other students cannot see.
               Here are several resources for learning how to use git:

* [The full Pro Git book](https://git-scm.com/book/en/v2)
* [Git for Computer Scientists](https://eagain.net/articles/git-for-computer-scientists/)
* [A Visual Git Reference](http://marklodato.github.io/visual-git-guide/index-en.html?no-svg)
* [A git Primer](https://danielmiessler.com/study/git/)

#### Python

Python is one of the [most popular](https://insights.stackoverflow.com/survey/2018/#technology-programming-scripting-and-markup-languages) programming languages.
               So, there are many online resource available for it.
               Here are just a few useful resources:

* [The full "Think Python" Book](https://greenteapress.com/wp/think-python-2e/)
* [Official Tutorial](https://docs.python.org/3/tutorial/index.html)
* [Official Beginning Guide](https://wiki.python.org/moin/BeginnersGuide)
* [Hitchhiker's Guide to Python](https://docs.python-guide.org/index.html)
* [Data Structures in Python (Official)](https://docs.python.org/3/tutorial/datastructures.html#)
* [Data Structures in Python (Unofficial)](https://python.swaroopch.com/data_structures.html)
* [List Comprehensions in Python](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Lambda Functions in Python](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

### Assignment

For this assignment, you will be filling in two methods in two different Python files.

### <a name="buylotsoffruit">Problem 1: Buy Lost Of Fruit</a>

Implement the `buyLotsOfFruit` function in the `buyLotsOfFruit.py` file.
               This function will take a list of `(fruit, weight)` tuples and returns the cost of your list.
               If there is some fruit in the list which doesn't appear in `FRUIT_PRICES`, your function should print an error message and return `None` (which is like `null` in C and Java).
               Please do not change the `FRUIT_PRICES` dict.

### <a name="shopsmart">Problem 2: Shop Smart</a>

Implement the `shopSmart` function in the `shopSmart.py` file.
               This function takes two arguments:

1. `orderList` - Like the kind passed in to `buyLotsOfFruit()`.
2. `fruitShops` - A list of `FruitShop`.

This function returns the `FruitShop` where your total order costs the least amount.

               Don't change the file name or variable names, please.
               Note that we will provide the `shop.py` implementation as a "support" file, so you don't need to submit yours.

### Frequent Errors

Here are some common problems (and their solutions) that new Python students have:

#### ImportError - .py

**Problem:**

You get the following error when running your program:

`
                  ImportError: No module named py
               `

**Solution:**

When using `import`, do not include the ".py" from the filename.
                  For example, you should say: `import shop`
**not:** `import shop<strong>.py</strong>`.

#### NameError - not defined

**Problem:**

You get the following error when running your program:

`
                  NameError: name 'my_variable' is not defined
               `

**Solution:**

To access a member of a module, you have to type `module_name.member_name`, where `module_name` is the name of the `.py` file,
                  and `member_name` is the name of the variable (or function) you are trying to access.

#### TypeError - dict not callable

**Problem:**

You get the following error when running your program:

`
                  TypeError: 'dict' object is not callable
               `

**Solution:**

Dictionary looks up are done using square brackets: [ and ].
                  NOT parenthesis: ( and ).

#### ValueError - too many to unpack

**Problem:**

You get the following error when running your program:

`
                  ValueError: too many values to unpack
               `

**Solution:**

Make sure the number of variables you are assigning to a variable or in a `for` loop matches the number of elements in each item of the list.
                  Similarly for working with tuples.

For example, if `pair` is a tuple of two elements (e.g. `pair = ('apple', 2.0)`) then the following code would cause the "too many values to unpack error":

```
pair = ('apple', 2.0)
(a, b, c) = pair
```

Here is a problematic scenario involving a `for` loop:

```
pairList = [('apples', 2.00), ('oranges', 1.50), ('pears', 1.75)]
for fruit, price, color in pairList:
   print('%s fruit costs %f and is the color %s' % (fruit, price, color))
```

#### AttributeError - list length

**Problem:**

You get the following (or similar) error when running your program:

`
                  AttributeError: 'list' object has no attribute 'length'
               `

**Solution:**

Finding length of lists is done using `len(myList)`.
