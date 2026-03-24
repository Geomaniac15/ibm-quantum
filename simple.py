from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

# create circuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# simulator backend
sim = Aer.get_backend('aer_simulator')

# compile (transpile) for backend
compiled = transpile(qc, sim)

# run circuit
result = sim.run(compiled, shots=1000).result()

# get results
counts = result.get_counts()

print(counts)