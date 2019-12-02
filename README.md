# combine-files
Combine multiple CSV files into one dataframe and output to a master CSV or Excel file

This python script reads in multiple CSV files from a directory and does a union merge (on column) of the files. The files can have different data schemas, and the columns do not have to be in the same order. All columns will be preserved. Optionally, a new column can be added to show the source file.

While a task like this seems trivial, common tools such as Excel's data import or Microsoft Windows copy command can only handle files with the same data schema.  
