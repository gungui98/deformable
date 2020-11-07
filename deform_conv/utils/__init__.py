# flake8: noqa
# Copyright (c) Open-MMLab. All rights reserved.

import torch
from .logging import get_logger, print_log
from .registry import Registry

__all__ = ['get_logger',
           'print_log',
           'Registry'
           ]
