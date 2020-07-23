rm data_original_100.js
rm data_onetime_100.js
rm data_multihop_100.js
cp closest_fact_100_original.json data_original_100.js
cp closest_fact_100_onetime.json data_onetime_100.js
cp closest_fact_100_multihop.json data_multihop_100.js
sed -i '' '1s/^/ var dataOriginal = /' data_original_100.js
sed -i '' '1s/^/ var dataOnetime = /' data_onetime_100.js
sed -i '' '1s/^/ var dataMultihop = /' data_multihop_100.js