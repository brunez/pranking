# Pranking
## What is Pranking
Pranking is a Python script that generates a ranking out of
the commit history of a git repository.
    
## How to run
Place the script inside a git repository directory and run:
    $ python rank.py
This will generate a ranking via stdout.

## Usage:
    python rank.py [OPTIONS]

    OPTIONS:
	    -t DAYS, --time=DAYS 
		    Only commits from the last DAYS days are considered. DAYS
            must be a positive integer.
            
        -p, --pretty 
            A string of as many asterisks as commits correspond to the
            Author will be printed.

## Example
A usage example is included in the 'example' directory. This
script uses pranking.py to generate a ranking, which is written into
a file and uploaded to a server. Afterwards a php script is run
that sends an email to all participants of the project.
