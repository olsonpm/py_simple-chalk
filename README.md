## Simple Chalk

<!-- pypiwarn -->

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Intro](#intro)
   - [What is it?](#what-is-it)
   - [Why create it?](#why-create-it)
   - [Why the subset of features?](#why-the-subset-of-features)
- [Install](#install)
- [Usage](#usage)
- [Api](#api)
   - [`chalk` (string) => string](#chalk-string--string)
   - [`newChalk` () => Chalk](#newchalk---chalk)
- [Test](#test)
- [Features included from js version of Chalk](#features-included-from-js-version-of-chalk)
- [Features omitted](#features-omitted)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


### Intro

##### What is it?

A terminal string styling library for python.  It implements a subset of
Sindre Sorhus' [chalk](https://github.com/chalk/chalk) (which is for js).

e.g. `chalk.green.bold("success")` prints like you'd expect in the console.

##### Why create it?

I am familiar with and enjoy the syntax of [chalk](https://github.com/chalk/chalk).
Anthonyalmarza's  [chalk](https://github.com/anthonyalmarza/chalk)
deviates from that syntax and so I created my own.

I'm also new to python so this was a good way to learn.


##### Why the subset of features?

I only use chalk for very simple purposes so I left out things like 256 colors.


### Install

```sh
$ pip install simple_chalk
```


### Usage

```python
from simple_chalk import chalk, green

# both of these are the same
print(chalk.green("success"))
print(green("success"))

# chained
print(green.bold("success"))

# assign combinations
success = green.bold.underline
print(success("we did it!"))

# last color wins
print(green.red("this is red"))

# background and foreground colors are separate
whyNot = green.bgWhite.red.bgGray
print(whyNot("this is red text with a gray background"))
```


### Api

`simple_chalk` exports the following

##### `chalk` (string) => string
 - A singleton that can be used instead of importing the colors and
   styles directly.
 - `chalk` and all exported colors/styles are chainable callables.  When called,
   they take a single string argument and return a string wrapped in the
   appropriate ascii color codes.

##### `newChalk` () => Chalk
 - You probably don't need this, but it creates a new chalk instance in case
   another library is misbehaving.

The following colors are exported

- black  
- red  
- green  
- yellow  
- blue  
- magenta  
- cyan  
- white  
- blackBright (also 'gray' and 'grey')
- redBright
- greenBright
- yellowBright
- blueBright
- magentaBright
- cyanBright
- whiteBright

Each color also has a camel-cased `bg` equivalent.  e.g. `bgBlack`
and `bgYellowBright`

Finally the following miscellaneous styles are exported

- bold
- dim
- underline
- hidden


### Test

```sh
hub clone olsonpm/py_simple-chalk
cd py_simple-chalk
python runTests.py
```


### Features included from js version of Chalk

- chainable api
- same color names (with added aliases)


### Features omitted

\*\* Features marked with `*` are ones I'd pull in should someone create a PR.

- 256 colors and TrueColor support
- multiple arguments, and thus nested styles
- \*color support detection
- \*blue -> blueBright auto conversion on windows
- \*ability to disable
- \*modifiers other than the miscellaneous styles noted above.
  e.g. `reset`, `italic`, `inverse` etc.
