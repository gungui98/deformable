### Prerequisites
- Cuda/ Cuda toolkit-11.0
- NVCC (install along with cuda)
- Pytorch >= 1.5.0

### Install from source

```bash
git clone https://github.com/gungui98/deformable.git
cd deformable
```

install silently by type:

```
pip install -e .
```

or with full compile logs:

```
python setup.py install develop
```

### Usage

``` python
from deform_conv.ops import DeformConv2dPack
    
conv2d = DeformConv2dPack(1, 3, 3).cuda()
out = conv2d(torch.randn((1, 3, 256, 256).cuda())
```