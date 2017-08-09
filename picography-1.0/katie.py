
import sys
from picography import *

def katie():

    timespan("1988-04-08", "2017-08-01", year_height=52)

    home("Bainbridge Island, WA", "1988-04-08", "2004-08-15", href="")
    home("Kathmandu, Nepal", "2004-08-18", "2005-06-15", href="")
    home("Bainbridge Island, WA", "2005-06-15", "2006-09-20", href="")
    home("Eugene, OR", "2006-09-20", "2008-05-20", href="")
    home("Elmira, OR", "2008-09-10", "2009-05-20", href="")
    home("Goldendale, WA", "2009-06-01", "2009-09-01", href="")
    home("Eugene, OR", "2009-09-10", "2010-05-23", href="")
    home("Portland, ME", "2010-08-15", "2016-03-18", href="")
    home("Brooklyn, NY", "2016-04-01", "2017-08-01", href="")

    roommate(1, "Chip", "2004-08-18", "2005-06-15")
    roommate(2, "Mara and Darcy", "2007-09-20", "2008-05-20")
    roommate(1, "Alison (and Sonny and Will)", "2010-09-01", "2011-06-01")
    roommate(1, "Chris and Megan", "2011-06-01", "2012-09-01")
    roommate(3, "Sarah", "2012-09-01", "2013-09-01")
    roommate(2, "Johnicholas", "2013-09-01", "2017-08-01")

make_pico(katie, sys.argv[1:])
