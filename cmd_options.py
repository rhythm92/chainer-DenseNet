#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import time


def create_log(args):
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s',
        filename=os.path.join(args.dir, 'options.txt'), level=logging.DEBUG)
    logging.info(args)


def create_result_dir(dir):
    if not os.path.exists('results'):
        os.mkdir('results')
    if dir:
        result_dir = os.path.join('results', dir)
    else:
        result_dir = os.path.join(
            'results', time.strftime('%Y-%m-%d_%H-%M-%S'))
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    return result_dir


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu', type=int, default=0)
    parser.add_argument('--augment', type=str, default='t', choices=['t', 'f'])
    parser.add_argument('--batchsize', type=int, default=64)
    parser.add_argument('--split_size', type=int, default=1)
    parser.add_argument('--lr', type=float, default=0.1)
    parser.add_argument('--weight_decay', type=float, default=1e-4)
    parser.add_argument('--depth', type=int, default=40)
    parser.add_argument('--growth_rate', type=int, default=12)
    parser.add_argument('--drop_ratio', type=float, default=0)  # 0.2 (cifar+)
    parser.add_argument('--block', type=int, default=3)
    parser.add_argument('--init_model', type=str, default='')
    parser.add_argument('--dir', type=str, default='')
    parser.add_argument('--dataset', type=str, default='cifar10',
                        choices=['cifar10', 'cifar100', 'SVHN'])
    args = parser.parse_args()

    if args.batchsize % args.split_size != 0:
        raise Exception('batchsize must be divisible by split_size')

    args.augment = True if args.augment == 't' else False
    args.dir = create_result_dir(args.dir)

    create_log(args)

    return args
