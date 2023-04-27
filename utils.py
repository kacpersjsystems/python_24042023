import argparse


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('--operation', required=True)
    args.add_argument('--name')
    args.add_argument('--event_at')
    args.add_argument('--id', type=int)
    return args.parse_args()