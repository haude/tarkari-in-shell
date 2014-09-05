#!/bin/bash

DATE='09-02-2014'
URL='http://kalimatimarket.com.np/priceinfo/dlypricebulletin'
PRICE_TYPE='W'
DATA_PARAMS="cdate=`tr - / <<< $DATE`&pricetype=$PRICE_TYPE"

TMP_DIR=/tmp
TARKARI_DATA_FORMAT=$PRICE_TYPE\_$DATE

#curl the table
get_data(){
	curl -s $URL --data $DATA_PARAMS > $TARKARI_DATA_FORMAT.html
}

#filter the data
url_to_csv(){
cat $TARKARI_DATA_FORMAT.html|sed 's/<[^>]\+>/\n/g'|tr -d [$'\r'] |awk 'NF>0 {print}'|tail -n +3|paste -d',' - - - - - > $TMP_DIR/$TARKARI_DATA_FORMAT.csv
}

#convert csv to json
csv_to_json() {
	#first squeeze the header on csv
	sed -i 's/Commodity Name/cname/g' $TMP_DIR/$TARKARI_DATA_FORMAT.csv
	#then convert to json
	sh csv_to_json.sh $1 #> $TMP_DIR/$TARKARI_DATA_FORMAT.json
}

#get_data
url_to_csv
csv_to_json $TMP_DIR/$TARKARI_DATA_FORMAT.csv
