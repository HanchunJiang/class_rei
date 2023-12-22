for num in {1..5..1}  
do  
echo ${num}
rm -rf output/chi1_"${num}"_*dat
echo $num
done

