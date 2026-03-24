from qiskit import QuantumCircuit

# create a circuit with one qubit and classical bit
qc = QuantumCircuit(1,1)

# applies a hadamard gate to qubit 0
qc.h(0)

# store reault in classical bit 0
qc.measure(0,0)