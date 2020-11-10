for d in $(ls | grep nonapod_inputs_); do
  python postprocess_nonapod.py $d
done
