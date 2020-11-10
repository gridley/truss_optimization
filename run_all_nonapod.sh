for dir in $(ls | grep nonapod_inputs_); do
    cd $dir
    for input in $(cut -d \  -f 3 input_list); do
        ../a.out $input
    done
    cd ..
done
