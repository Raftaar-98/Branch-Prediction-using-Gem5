# -- an example to run SPEC 429.mcf on gem5, put it under 429.mcf folder --
export GEM5_DIR=/home/012/s/ss/ssy220000/P1/gem5
export BENCHMARK1=/home/012/s/ss/ssy220000/P1/Project1_SPEC-master/401.bzip2/src/benchmark
export ARGUMENT1=/home/012/s/ss/ssy220000/P1/Project1_SPEC-master/401.bzip2/data/input.program
export OUTPATH1=/home/012/s/ss/ssy220000/P1/Project1_SPEC-master/401.bzip2

export BENCHMARK2=/home/012/s/ss/ssy220000/P1/Project1_SPEC-master/429.mcf/src/benchmark
export ARGUMENT2=/home/012/s/ss/ssy220000/P1/Project1_SPEC-master/429.mcf/data/inp.in
export OUTPATH2=/home/012/s/ss/ssy220000/P1/Project1_SPEC-master/429.mcf




time $GEM5_DIR/build/X86/gem5.opt -d $OUTPATH1/m5out $GEM5_DIR/configs/example/se.py -c $BENCHMARK1 -o "$ARGUMENT1" -I 5000000 --cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64

time $GEM5_DIR/build/X86/gem5.opt -d $OUTPATH2/m5out $GEM5_DIR/configs/example/se.py -c $BENCHMARK2 -o "$ARGUMENT2" -I 5000000 --cpu-type=atomic --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64

