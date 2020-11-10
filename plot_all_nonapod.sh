for d in $(ls | grep nonapod_inputs_); do
    cd $d
    python ../plot_objective_values.py results
    cd ..
done
