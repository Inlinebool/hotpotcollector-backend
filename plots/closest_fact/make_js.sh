rm data_original_1000.js
rm data_onetime_1000.js
rm data_multihop_1000.js
cp closest_fact_1000_original.json data_original_1000.js
cp closest_fact_1000_onetime.json data_onetime_1000.js
cp closest_fact_1000_multihop.json data_multihop_1000.js
sed -i '1s/^/ var dataOriginal = /' data_original_1000.js
sed -i '1s/^/ var dataOnetime = /' data_onetime_1000.js
sed -i '1s/^/ var dataMultihop = /' data_multihop_1000.js