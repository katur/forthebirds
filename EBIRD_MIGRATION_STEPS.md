```
# Apply migration add optional ebird_id CharField

# Populate ebird_id field:

    ./manage.py add_ebird_ids eBird_v2015_csv.csv

# Apply migrations that add other optional ebird_id fields, and that set
# is_visible to default False.

# Populate those fields:

    ./manage.py import_ebird_data eBird_v2015_csv.csv
```

TODO
1) default/null value considerations for non-ebird fields of new rows
2) will id just magically start incrementing where it left off for new rows?
3) purge database of MinnesotaSpecies (just dump this to a google doc for now)
4) delete unneeded columns (model and code): nacc fields; french name
