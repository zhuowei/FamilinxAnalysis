Tools for working with the [Familinx](https://familinx.org) dataset.

## Contents

`sql/`: PostgreSQL scripts for importing the data from Familinx.

- `create_db.psql`: Creates the `profiles` table
- `delete_db.psql`: Deletes the profiles table
- `import_db.psql`: Imports the database over the network. My database is in a virtual machine, you probably don't need it
- `create_index.psql`: Creates an index over the Familinx table on birth/death year; slows down query to unusable; do not run
- `delete_index.psql`: Deletes the index
- `export_ids_alive_during_1809.psql`: Exports the IDs of everyone alive during 1809; the output is used by the filtering scripts
- `import_profile_ids_bfsout.psql`: imports the node IDs output by ReadNodes.java into a table.
- `create_joined_table_bfsout.psql`: Creates a new filtered table containing only the descendants that were output by ReadNodes.java and imported by the above script

`process_output/`: processes data exported from the Familinx database.

- `pick_one_in_twenty.py`, `picklist_ratio.py`: takes a text file, sorts it, then pseudorandomly picks a percentage of the lines. The first script hardcodes it to one in twenty; the second script is configurable
- `ReadNodes.java`: takes the Familinx relations-anon.txt list of nodes and a list of nodes, and prints out all the descendants of those nodes.
- `countsperyear_to_table.py`: formats the output of the psql scripts that dump the number of people alive per year.

`generate_sql`: scripts that generate PostgreSQL files for exporting data

- `make_queries_per_year.py`: outputs script that computes how many people are alive in any given year. Doesn't count currently alive people; used for 1800-1900
- `make_queries_per_year_alive.py`: same as above, but takes currently alive people into account. Used for 1900-2010
- `bfsout_make_queries_per_year.py`: combination of the two above scripts, used to process the one-in-twenty filtered data
- `varying_bfsout_make_queries_per_year.py`: same script as above, but with tweakable table name; used to process 1%, 10%, 15%, and 20% filtered data
- `import_profileids_ratio.py`: combines `import_profile_ids_bfsout.psql` and `create_joined_table_bfsout.psql` for the 1/10/15/20% alternate ratio BFS output

`graphtest`: a sample family tree for testing ReadNodes.java, and scripts to graph the result.

## Tips

Remove the first line (the field names) from `profiles-anon.txt` before importing into Postgres.

## License

My code is licensed under the MIT license.

Data in the output/ directory is derived from the Familinx dataset and follows their license.
