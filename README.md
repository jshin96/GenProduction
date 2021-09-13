# GenProduction
---
### initial setup
```
cmsrel CMSSW_10_2_3
cd CMSSW_10_2_3/src
cmsenv

git cms-init
git cms-addpkg GeneratorInterface/LHEInterface
cd GeneratorInterface/LHEInterface/data
wget https://raw.githubusercontent.com/cms-sw/cmssw/master/GeneratorInterface/LHEInterface/data/run_generic_tarball_xrootd.sh
chmod 755 run_generic_tarball_xrootd.sh
cd $CMSSW_BASE/src
scram b -j 6

# not clone the repository
mkdir Configuration && cd Configuration
git clone .../GenProduction
cd ..
scram b
```
