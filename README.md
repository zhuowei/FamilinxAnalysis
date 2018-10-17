Tools for working with the [Familinx](https://familinx.org) dataset.

## Contents

`sql/`: PostgreSQL scripts for importing the data from Familinx.

- `create_db.psql`: Creates the `profiles` table
- `delete_db.psql`: Deletes the profiles table
- `import_db.psql`: Imports the database over the network. My database is in a virtual machine, you probably don't need it

## Tips

Remove the first line (the field names) from `profiles-anon.txt` before importing into Postgres.

## Licens

My code is licensed under the MIT license.

Data in the output/ directory is derived from the Familinx dataset and follows their license.
