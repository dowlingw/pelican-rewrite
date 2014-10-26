Pelican Rewrite
===============
Plugin for [Pelican](http://www.getpelican.com/) to ease transition to Pelican from another CMS.


How to use
----------
This module will generate a .htaccess file in the root of the output with rewrite rules to direct users and web crawlers to the new location for content.

To enable redirection for a given page, add the `oldurl` metadata tag to an article. This script assumes an absolute path from the webroot, ie: `/node/1234`.

Currently this module outputs rewrite rules for [nginx](http://nginx.org/), however there is commented out code for Apache also.


Development Status
------------------
Buyer beware! This module was developed for personal use and probably contains plenty of bugs and omissions. 


TODO
----

-    Make output format configurable (nginx vs apache)


License
-------
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
