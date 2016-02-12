```
# Apply migration to add optional ebird_id CharField

./manage.py migrate birds/0014_species_ebird_id
./manage.py migrate birds/0015_auto_20160210_2157


# Apply migrations to add other, currently optional ebird fields, and that
# set is_visible to default False going forward

./manage.py migrate birds/0016_auto_20160210_2224
./manage.py migrate birds/0017_auto_20160210_2225
./manage.py migrate birds/0018_auto_20160210_2341


# Apply migration to delete NACC fields and french fields

./manage.py migrate birds/0019_auto_20160211_1717


# Populate ebird_id field

./manage.py add_ebird_ids eBird_v2015_csv.csv


# STOP HERE FIRST TIME


# Run MySQL query to change bird species id to autoincrement INT

LOCK TABLES
    birds_species WRITE,
    creations_creation_species WRITE;

ALTER TABLE creations_creation_species
    DROP FOREIGN KEY creations_creati_species_id_27f3ca1253e3b048_fk_birds_species_id,
    MODIFY species_id INT;

ALTER TABLE birds_species MODIFY id INT AUTO_INCREMENT;

ALTER TABLE creations_creation_species
    ADD FOREIGN KEY creations_creati_species_id_27f3ca1253e3b048_fk_birds_species_id (species_id)
    REFERENCES birds_species (id);

UNLOCK TABLES;


# Apply migration that SHOULD have applied the MySQL above, but that causes
# a MySQL error due to a foreign key not getting updated

./manage.py migration birds/0020_auto_20160211_2005


# Populate those fields:

./manage.py import_ebird_data eBird_v2015_csv.csv
```
