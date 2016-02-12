```
# Apply migrations to add optional ebird_id CharField

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


# Apply migration to delete minnesota species

./manage.py migrate birds 0020_remove_minnesotaspecies


# Run MySQL query to change bird species id to autoincrement INT

LOCK TABLES
    birds_species WRITE,
    creations_creation_species WRITE;

ALTER TABLE creations_creation_species
    DROP FOREIGN KEY creations_creati_species_id_27f3ca1253e3b048_fk_birds_species_id,
    MODIFY species_id INT NOT NULL;

ALTER TABLE birds_species MODIFY id INT AUTO_INCREMENT;

ALTER TABLE creations_creation_species
    ADD FOREIGN KEY creations_creati_species_id_27f3ca1253e3b048_fk_birds_species_id (species_id)
    REFERENCES birds_species (id);

UNLOCK TABLES;


# Apply migration that *should* have applied the MySQL above, but that causes
# a MySQL error due to a foreign key not getting updated

./manage.py migrate birds 0021_add_autoid


############### THIS IS WHERE I CURRENTLY AM ON WEBFACTION ###############




# Run script that populates new eBird fields; updates common, slug, and
# scientific names if they are different in eBird; and adds eBird species
# not previously present in the database (these all default to not visible).
# For new species, id will autoincrement.
# Had to do this to convert linebreaks in original ebird file:
# http://stackoverflow.com/questions/811193/how-to-convert-the-m-
#     linebreak-to-normal-linebreak-in-a-file-opened-in-vim
# Also had to replace enyays and umlots in thes:

# These need ñ
#   marcre1 nartap2 marspi3 marthr2 hoomoc1

# These need ü (do :%s/Ÿ/ü/g)
#   ruegri1 ruebus1 ruepar1 ruewar1 rurcha1 ruecha1 ruegls1 ruewea1

./manage.py import_ebird_data eBird_v2015_csv.csv


# Set up redirects for the common names that changed during switch to eBird

# Set various fields to `required` that should be: ebird_id, taxon_order,
family, order, taxon_order (family_common?, en_IOC?)

# Modify code to use eBird taxonomy instead of NACC taxonomy. Then delete
# the parent pointer and separate taxonomy tables.

# Modify code to use taxon_order instead of absolute_position. Then delete
# absolute_position.

```
