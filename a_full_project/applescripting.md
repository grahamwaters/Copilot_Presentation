To install XCode I need to have space to install the 8GB files.

# Apple Scripting to move applications that I don't want to have on my harddrive to an external harddrive

the script below moves all applications that are not in the list of applications that I want to keep on my harddrive to an external harddrive and updates the symbolic links to the applications.

```applescript
on run {input, parameters}

	set string password to "password"
	do shell script "cd /Applications" user name "grahamwaters" password (text returned of password) with administrator privileges
	do shell script "sudo cp -R Microsoft Word.app /Volumes/CodeFiles/" user name "grahamwaters" password (text returned of password) with administrator privileges
	do shell script "cd /Volumes/CodeFiles/" user name "grahamwaters" password (text returned of password) with administrator privileges
	do shell script "sudo ln -s /Volumes/CodeFiles/Microsoft Word.app /Applications/Microsoft Word.app" user name "grahamwaters" password (text returned of password) with administrator privileges
	do shell script "sudo rm -rf /Applications/Microsoft Word.app" user name "grahamwaters" password (text returned of password) with administrator privileges
	return input
end run
```
This has errors in it. I need to fix it. The corrected version is here:

```applescript
on run {input, parameters}

    set string password to "password"
    do shell script "cd /Applications" user name "grahamwaters" password (text returned of password) with administrator privileges
    do shell script "sudo cp -R Microsoft Word.app /Volumes/CodeFiles/" user name "grahamwaters" password (text returned of password) with administrator privileges
    do shell script "cd /Volumes/CodeFiles/" user name "grahamwaters" password (text returned of password) with administrator privileges
    do shell script "sudo ln -s /Volumes/CodeFiles/Microsoft Word.app /Applications/Microsoft Word.app" user name "grahamwaters" password (text returned of password) with administrator privileges
    do shell script "sudo rm -rf /Applications/Microsoft Word.app" user name "grahamwaters" password (text returned of password) with administrator privileges
    return input
end run
```
what changed?
- I added the word "string" to the line that sets the password
- I added the word "text" to the line that returns the password

why?
- I added the word "string" to the line that sets the password because the password is a string
- I added the word "text" to the line that returns the password because the password is a string

This is still causing errors. What I will do is create a series of terminal commands that I can run in the terminal. I will then create a script that will run those commands in the terminal.

```bash
cd /Applications
sudo cp -R Microsoft Word.app /Volumes/CodeFiles/
cd /Volumes/CodeFiles/
sudo ln -s /Volumes/CodeFiles/Microsoft Word.app /Applications/Microsoft Word.app
sudo rm -rf /Applications/Microsoft Word.app
```
# example_repo


Here is the filestructure of the data files in this analysis project. I am a python developer and this project's goal is to analyze the data in these files which show power data from austin energy for February 1st, 2023 (as a starting point).

The filestructure:

* [data/](./example_repo/data)
  * [ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure)
    * [2d_Agg_AS_Offers_OFFNS-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Agg_AS_Offers_OFFNS-01-FEB-23.csv)
    * [2d_Agg_AS_Offers_ONNS-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Agg_AS_Offers_ONNS-01-FEB-23.csv)
    * [2d_Agg_AS_Offers_REGDN-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Agg_AS_Offers_REGDN-01-FEB-23.csv)
    * [2d_Agg_AS_Offers_REGUP-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Agg_AS_Offers_REGUP-01-FEB-23.csv)
    * [2d_Agg_AS_Offers_RRSFFR-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Agg_AS_Offers_RRSFFR-01-FEB-23.csv)
    * [2d_Agg_AS_Offers_RRSPFR-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Agg_AS_Offers_RRSPFR-01-FEB-23.csv)
    * [2d_Agg_AS_Offers_RRSUFR-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Agg_AS_Offers_RRSUFR-01-FEB-23.csv)
    * [2d_Cleared_DAM_AS_NSPIN-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Cleared_DAM_AS_NSPIN-01-FEB-23.csv)
    * [2d_Cleared_DAM_AS_REGDN-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Cleared_DAM_AS_REGDN-01-FEB-23.csv)
    * [2d_Cleared_DAM_AS_REGUP-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Cleared_DAM_AS_REGUP-01-FEB-23.csv)
    * [2d_Cleared_DAM_AS_RRSFFR-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Cleared_DAM_AS_RRSFFR-01-FEB-23.csv)
    * [2d_Cleared_DAM_AS_RRSPFR-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Cleared_DAM_AS_RRSPFR-01-FEB-23.csv)
    * [2d_Cleared_DAM_AS_RRSUFR-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Cleared_DAM_AS_RRSUFR-01-FEB-23.csv)
    * [2d_Self_Arranged_AS_NSPIN-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Self_Arranged_AS_NSPIN-01-FEB-23.csv)
    * [2d_Self_Arranged_AS_NSPNM-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Self_Arranged_AS_NSPNM-01-FEB-23.csv)
    * [2d_Self_Arranged_AS_REGDN-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Self_Arranged_AS_REGDN-01-FEB-23.csv)
    * [2d_Self_Arranged_AS_REGUP-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Self_Arranged_AS_REGUP-01-FEB-23.csv)
    * [2d_Self_Arranged_AS_RRSFFR-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Self_Arranged_AS_RRSFFR-01-FEB-23.csv)
    * [2d_Self_Arranged_AS_RRSPFR-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Self_Arranged_AS_RRSPFR-01-FEB-23.csv)
    * [2d_Self_Arranged_AS_RRSUFR-01-FEB-23.csv](./example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Self_Arranged_AS_RRSUFR-01-FEB-23.csv)
* [CONTRIBUTORS.md](./example_repo/CONTRIBUTORS.md)
* [LICENSE](./example_repo/LICENSE)
* [analysis.ipynb](./example_repo/analysis.ipynb)
* [data_description.md](./example_repo/data_description.md)
* [main.py](./example_repo/main.py)
* [requirements.txt](./example_repo/requirements.txt)

_______

Act as a python programmer.
Write a simple python script using `os` and `pandas` and load the data from the `../data` folder into pandas dataframes organized into folders that are named by the following convention:
"../data/{day}/{file_set}/{file_name}"
as an example: "example_repo/data/ext.00013057.0000000000000000.20230201.032307367.2_Day_AS_Disclosure/2d_Cleared_DAM_AS_RRSFFR-01-FEB-23.csv"
this file should be now saved as a pandas dataframe called `2d_Cleared_DAM_AS_RRSFFR_df` in this folder structure: `example_repo/processed_data/dfs/02_01_2023/`

Produce the files for 2/1/2023 to 2/5/2023 using the pattern shown in the example filestructure above changing "01-FEB-23" to "02-FEB-23" and so on.

You will provide your response in a code block with no extra commentary, only well-written python code that conforms to the best practices for pythonic, efficient programming.
Is that understood?
