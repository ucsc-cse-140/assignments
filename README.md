# Assignments
These are the assignments for CSE140 at UCSC.  They are:
- [p0](p0/README.md)
- [p1](p1/README.md)
- [p2](p2/README.md)
- [p3](p3/README.md)

# CSE 140 Programming Assignment Setup
There are two repositories that are needed for CSE 140:

1.  [Assignments repo](https://github.com/ucsc-cse-140/assignments)
    -   This is used for turning in assignments and submitting to the autograder.
2.  [Pacman assignments](https://github.com/linqs/pacman)
    -   The coding structure for running the pacman and completing the
        assignments.

I recommend keeping these repos separate.  One for submission, and the
other for development and testing.

For each code base, you will:

1.  Checkout or download the zip file from github.
2.  Download the requirements with: `pip3 install --user -r requirements.txt`
    1.  For the assignments repo, you will need python version >= 3.10
    2.  For the pacman repository, you will need Tk, check the detailed
        instructions [here](https://github.com/ucsc-cse-140/assignments/tree/main/p1#running-code-on-your-local-machine).


## Submitting and using the Autograder in CSE 140

Make sure that the autograder is installed on your local machine by
typing: `python3 -m autograder.cli`.  If you see the `--help` option:

```nil
python -m autograder.cli
The autograder CLI package contains several tools for interacting with the autograder.
The following is a non-exhaustive list of CLI tools.
Invoke each command with the `--help` option for more details.
```

Then your autograder is downloaded correctly.  You will also need to
update the `config.json` file.  See examples in [p0](https://github.com/ucsc-cse-140/assignments/blob/main/p0/config.json) and [p1](https://github.com/ucsc-cse-140/assignments/blob/main/p1/config.json).  You will
need to update the:

-   `user` to your ucsc.edu email address
-   `pass` to the password sent from ucsc.autograder to your ucsc email
    account.  Email the teaching team if it has not been received.


### Using the autograder

The autograder command line interface (cli) is [documented](https://github.com/eriq-augustine/autograder-py).  As a
student in the class, the main commands you will use are:

-   `python3 -m autograder.cli.submit`: this will submit an assignment
    for a particular class and assignment.
-   `python3 -m autograder.cli.peek`: this will show you your last submission
-   `python3 -m autograder.cli.history`: this will show a summary of all
    your past submission
-   `python3 -m autograder.cli.style`: this will check the style of a
    particular assignment.
