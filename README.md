# IP-Blacklist-Scraper
Scrapes the firehol repository and converts IPs into plain text

## **Configuration**

If a specific set is wanted from the Firehol repository, edit the URL parameter in the configuration to the **raw text** URL. 
 
If no set is specified or the config file is not found, it will default to https://github.com/firehol/blocklist-ipsets/blob/master/firehol_level1.netset

The source repository can be found at https://github.com/firehol/blocklist-ipsets

Since these repositories are automatically updated, there is no need to update the code. Simply rerun the program and it will automatically provide an updated list.
