# combine-files
Combine multiple CSV files into one dataframe and output to a master CSV or Excel file

This python script reads in multiple CSV files from a directory and does a union merge of the files. The files can have different data schemas. All columns will be preserved. A new column can be added to show the source file.

While a task like this seems trivial, common tools such as Excel's data import or Microsoft Windows copy command can only handle files with the same data schema.  
