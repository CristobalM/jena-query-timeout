# build
```
mvn package
```
# run

```
java -jar target/jena-query-timeout-1.0-SNAPSHOT-jar-with-dependencies.jar \
-d <dataset-folder> -q <query-file> -t <timeout-ms>
```


# script
```
python3 generate_minus_1.py <output_file_nt> <left_size> <right_size>
```