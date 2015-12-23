# load-zipcodes
These python scripts use the python module <a href="https://pypi.python.org/pypi/uszipcode">uszipcode</a> (<a href="http://www.wbh-doc.com.s3.amazonaws.com/uszipcode/index.html"documentation</a>) to populate a postgresql database table.  As I was writing another app, I found it more useful to have all the zipcodes loaded into a database instead of running uszipcode inline.  So I decided to write this little script to get the job done.

At the time of this posting, it is up-to-date as of October, 2015 (which corresponds to uszipcode v0.0.7).  I have also posted the SQL files which will be much easier for you, but if uszipcode has updated with newer data, you will want to run the script instead.

Feel free to branch this to add support of other databases.

Requires <a href="https://pypi.python.org/pypi/uszipcode">uszipcode</a>, <a href="https://pypi.python.org/pypi/psycopg2">psycopg2, <a href="https://docs.python.org/2/library/pprint.html">pprint</a>, sys

<strong><a href"https://github.com/rubix1138/load-zipcodes/blob/master/loadZips.py">loadZips.py</a></strong> is the base file.
<strong><a href"https://github.com/rubix1138/load-zipcodes/blob/master/loadZips2.py">loadZips2.py</a></strong> is file I actually used because I wanted to link the states to my state table.  I used <a href="http://statetable.com/">StateTable.com</a> to build my state table.


