import numpy as np
import random_num as rn
import powerspectrum as ps
import argparse

parser = argparse.ArgumentParser(description="")
parser.add_argument("--run_mode", dest="run_mode", default="no_random", help="run mode")
parser.add_argument("--use_random", dest="use_random", default=True, type=bool,help="whether use the random model")
#for no_random mode
parser.add_argument("--random_num", dest="random_num", type=int, default=3, help="number of random points")

#common
parser.add_argument('--p_name', dest='p_name',help='name of paramters', type=lambda s: [item for item in s.split(',')])

#for large and middle range
parser.add_argument('--p_start', dest='p_start',help='starts of paramters', type=lambda s: [float(item) for item in s.split(',')])
parser.add_argument('--p_end', dest='p_end', help='ends of paramters', type=lambda s: [float(item) for item in s.split(',')])
parser.add_argument('--p_step', dest='p_step',help='steps of paramters', type=lambda s: [float(item) for item in s.split(',')])

#for small and final
parser.add_argument('--p_value', dest='p_value',help='values of paramters', type=lambda s: [float(item) for item in s.split(',')])
parser.add_argument('--p_sigma',dest='p_sigma', help='sigmas of paramters', type=lambda s: [float(item) for item in s.split(',')])
parser.add_argument('--ranges', dest='ranges',help='search ranges', type=float, default=4.0)
parser.add_argument('--steps', dest='steps',help='search steps', type=float, default=8.0)


#read inter results
parser.add_argument("--root_x_z", dest="root_x_z", default="output/", help="root of reading x_e and z")

#save results
parser.add_argument("--root_result", dest="root_result", default="output/", help="root of results")

parser.add_argument("--isTrain", dest="isTrain", action='store_true', help="train or test")
parser.add_argument("--model_dir", dest="model_dir", default="./Model", help="Root directory to save learned model parameters")
args = parser.parse_args()

def main():
    if args.run_mode=="no_random":#random numbers haven't been generated
        pass
    elif args.run_mode=="large_range" or "middle_range":
        pass
    elif args.run_mode=="small_range" or "get_result":
        if args.use_random==True:
            redshifts=np.load(args.root_x_z+"totalz.npy")
            xes=np.load(args.root_x_z+"totalxe.npy")
            for i in range(len(redshifts)):
                point=rn.random_num(True,redshifts[i],xes[i])
                point.run()
                #check bias


