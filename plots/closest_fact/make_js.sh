rm data_original_1000.js
rm data_tfidf_coref_1000.js
cp original_pos_1000.json data_original_1000.js
cp closest_fact_1000_tfidf_coref.json data_tfidf_coref_1000.js
sed -i '' '1s/^/ var dataOriginal = /' data_original_1000.js
sed -i '' '1s/^/ var dataTfidfCoref = /' data_tfidf_coref_1000.js