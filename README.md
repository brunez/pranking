# Pranking
## How to run
    Place the script inside a git repository directory and run:
    $ python rank.py
    This will generate a ranking via stdout.

##Usage:
    python rank.py [OPTIONS]

    OPTIONS:
	    -t DAYS, --time=DAYS 
		    Only commits from the last DAYS days are considered. DAYS
            must be a positive integer.
            
        -p, --pretty 
            A string of as many asterisks as commits correspond to the
            Author will be printed.
