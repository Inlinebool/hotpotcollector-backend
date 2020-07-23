rm data_original_10000.js
rm data_onetime_10000.js
rm data_multihop_10000.js
cp closest_fact_10000_original.json data_original_10000.js
cp closest_fact_10000_onetime.json data_onetime_10000.js
cp closest_fact_10000_multihop.json data_multihop_10000.js
sed -i '' '1s/^/ var dataOriginal = /' data_original_10000.js
sed -i '' '1s/^/ var dataOnetime = /' data_onetime_10000.js
sed -i '' '1s/^/ var dataMultihop = /' data_multihop_10000.js