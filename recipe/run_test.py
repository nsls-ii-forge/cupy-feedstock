# Configure CuPy to use 1 GPU for testing
import os
os.environ["CUPY_TEST_GPU_LIMIT"] = "1"

# Check CUDA_PATH is set
cuda_path = os.environ.get('CUDA_PATH')
assert cuda_path is not None
print("CUDA_PATH:", cuda_path)

# Check CUDA libraries are available
assert os.path.isfile(os.path.join(cuda_path, 'lib/libcudart.so'))

# Check for CuPy (without importing)
import pkgutil
pkgutil.find_loader("cupy")

# Try to import CuPy
import sys
try:
    #from cupy.cuda import cutensor
    import cupy
except ImportError as e:
    print('Got ImportError: \n%s' % str(e))
    print("No GPU available. Exiting without running CuPy's tests.")
    sys.exit(0)

## Check driver version (in the format XXX.XX)
#import subprocess
#subprocess.run(['nvidia-smi'])
#
## Print CuPy runtime info
#cupy.show_config()
#
## Run CuPy's test suite
#import py
#py.test.cmdline.main(["tests/cupy_tests"])
#py.test.cmdline.main(["tests/cupyx_tests"])
