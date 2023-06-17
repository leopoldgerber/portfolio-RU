# Setting up additional files

### save_config.py
Create and save a json file that contains database configuration. Should contains:
- Username
- Password
- Host
- Port
- Database

### exception_list.py
Since the dataframe load script processes columns before adding them to the database - it's good to have an exception list handy that cancels processing of selected columns. For example, if the "user duration" column contains the ":" character, we want to keep the character for further processing rather than replace it. To do this, we create an exception list or enter the columns manually if there is no exception.
