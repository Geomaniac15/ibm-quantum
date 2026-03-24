from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

qc = QuantumCircuit(2, 2)

qc.h(0)        # put qubit 0 into superposition
qc.cx(0, 1)    # entangle qubit 1 with qubit 0

qc.measure([0,1], [0,1])

sim = Aer.get_backend('aer_simulator')
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=1000).result()

print(result.get_counts())