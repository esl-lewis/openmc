import openmc
import os

os.environ.get('OPENMC_CROSS_SECTIONS')

openmc.run(particles=100,cwd='/opt/openmc/sinbad_benchmarks/auto-neutronics-benchmarking/mock-SINBAD')
