#!/bin/bash
set -e -x

# Compile wheels
for PYBIN in /opt/python/*/bin; do
    mkdir -p /io/build
    cd /io/build
    cmake .. -DBUILD_TESTS=OFF -DBUILD_PYTHON=ON -DPYTHON_EXECUTABLE=${PYBIN}/python
    make -j12
    "${PYBIN}/pip" wheel /io/build/python -w /io/wheelhouse/
    rm -rf /io/build/python
done

# Bundle external shared libraries into the wheels
for whl in /io/wheelhouse/*.whl; do
    auditwheel repair "$whl" -w /io/wheelhouse/
done

# Install packages and test
for PYBIN in /opt/python/*/bin/; do
    "${PYBIN}/pip" install -r /io/python/dev-requirements.txt
    "${PYBIN}/pip" install opengv --no-index -f /io/wheelhouse
    (cd "$HOME"; "${PYBIN}/python" /io/python/tests/tests.py)
done