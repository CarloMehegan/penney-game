# Example Project
"Sometimes I like to include a quote to grab attention! If so, I usually think long and hard about a _relevant_ quote!" - Ron

## Description
This repository is an example designed for my students who asked how to design a github repository. You should always begin with a high-level explanation of what the project is about. Do not include too many specific details here - imagine you are talking to a friend/family/coworker and just telling them what your project is about. You can (and should) provide much more detailed information later on in the README, or perhaps in a separate document.

After reading your description, a reasonable person should be expected to answer, "What is this project about?" in a manner satisfactory to you, the author.

For this example, there is no project, it's just an example for folks who are learning how to design their own repositories.

While explaining what my project is about, I would also include relevant links and citations, similar to writing a research report. For example, [How to write a good README](https://github.com/banesullivan/README). While I might not be as enthusiastic about emojis as that author, it's a wonderful example!

Other useful links include:

- GitHub's own [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

- [Guido van Rossum on Lex Fridman's podcast](https://www.youtube.com/watch?v=-DVyjdw4t9I)


For the current intended audience (working on Project Penney) you would probably want to include links to the wikipedia, the Humble-Nishiyama paper, and anything else you have found that would be relevant background to a newcomer (there's at least one wonderful youtube video about it that I will let you search for yourself.)

## Getting Started
Now explain to a new user how your code works. Give them a jumping-off point.

To run this code yourself:

```python
import main
main.do_the_thing()
```

Now explain the options available to the user:

Options:

- `n`: How many times to do  the thing (default = 1)
- `mode`: Which way to do the thing. Options include `modeA` (default), `modeB`.
- etc.

Keep this part short and sweet. Later on in the documentation, give those who are interested the info they need to dig deeper.


## Files\Folders Included

`data/`: This directory contains the raw data for the project. It is stored as a bunch of bits on materials that could have been made into a rock or piece of glass instead. **NOTE: For the purposes of Project Penney, you may have too much raw data for the free version of GitHub. You can modify your .gitignore to skip files here. If so, add a file to this folder called `files_too_large`.**

`figures/`: Any pre-prepared output should be stored in clearly labeled directories. You should also provide a high-level description of what these files are here. As discussed in class, this should contain both .html and .png versions of your figures.

`src/`: This directory contains the code and other resources used to make the thing. Usually, we put code, databases, images, and other things that the user does not need to worry themselves with into a directory called `src`.

If there were actual files in here, I would provide a high-level description of what the code in each file is for. I would also be sure that the code itself is well-documented (i.e., all functions are type-hinted, contain docstrings, and have ample comments throughout the code). The only time I would deviate from this rule is _if I did not care about my readers being able to understand my code._

`results/`: Describe the contents of the results.json that should be found here. **NOTE: For the purposes of Project Penney, we have decided in class that this directory should contain a single file called `results.json`**. Your repository must contain this file!

## Details

Now explain how it works. It's up to you how much info you think is important, or if you want to put things like this into a separate document smoewhere else. Put yourself in the shoes of the person viewing your repo. What would you want to know? What questions would you have? How well documented is your code? Do you have any future plans?

As your professor, I would like you to explain, at a minimum:

- How does your random data generation work? Translate your code into words, but do so in such a way that the competent reader would be able to confirm that your code does indeed match the words used to describe it.

- Once the data is generated, it is scored... how? Explain to a newcomer. Explain the algorithm in words, so that someone with a CS background might be able to do a cursory complexity analysis (e.g. "Oh that sounds like O($n^2$) to me!"). Also, are any assumptions being made? Is there anything displayed in the results that was assumed rather than computed, due to some symmetry?

- Explain how the results are presented. Even if the figures are clearly labeled, give a brief reiteration of what we are looking at. Is the diagonal grayed out? That deserves at least a sentence! Etc.
