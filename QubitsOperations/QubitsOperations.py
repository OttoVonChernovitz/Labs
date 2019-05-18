import cirq
import numpy as np


# Here is shown one qubit
print("One qubit:")
qubit = cirq.GridQubit(0, 0)

circuit = cirq.Circuit.from_ops(
    cirq.X(qubit)**0.5, 
    cirq.measure(qubit, key='m')
)
print("This is CIRQUIT:")
print(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Result of calculation:")
print(result)
print()


# Here is shown multy qubits
print("This is Multy qubits:")
length = 3

qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]
print(qubits)
print()


# Here is shown  place of qubits
print("Place of qubits:")
print("Length 10 line on Bristlecone:")
line = cirq.google.line_on_device(cirq.google.Bristlecone, length=10)
print(line)

print("This is Initial circuit:")
n = 10
dpth = 2
circuit = cirq.Circuit.from_ops(
    cirq.SWAP(cirq.LineQubit(j), cirq.LineQubit(j + 1))
    for i in range(dpth)
    for j in range(i % 2, n - 1, 2)
)
circuit.append(cirq.measure(*cirq.LineQubit.range(n), key='all'))
print(circuit)

print()
print("This is Xmon circuit:")
translated = cirq.google.optimized_for_xmon(
    circuit=circuit,
    new_device=cirq.google.Bristlecone,
    qubit_map=lambda q: line[q.x])
print(translated)
print()


# Bell Inequality
print("This is  Bell Inequality:")
def makeBellTestCircuit():
    alice = cirq.GridQubit(0, 0)

    bob = cirq.GridQubit(1, 0)

    aliceReferee = cirq.GridQubit(0, 1)

    bobReferee = cirq.GridQubit(1, 1)

    circuit = cirq.Circuit()

    circuit.append([
        cirq.H(alice),
        cirq.CNOT(alice, bob),
        cirq.X(alice)**-0.25,
    ])

    circuit.append([
        cirq.H(aliceReferee),
        cirq.H(bobReferee),
    ])

    circuit.append([
        cirq.CNOT(aliceReferee, alice)**0.5,
        cirq.CNOT(bobReferee, bob)**0.5,
    ])

    circuit.append([
        cirq.measure(alice, key='a'),
        cirq.measure(bob, key='b'),
        cirq.measure(aliceReferee, key='x'),
        cirq.measure(bobReferee, key='y'),
    ])

    return circuit


def bitstring(bits):
    return ''.join('1' if e else '_' for e in bits)

circuit = makeBellTestCircuit()
print('This is another Circuit:')
print(circuit)

print()
repetitions = 100
print('This is repetitions of Simulating {}'.format(repetitions))
result = cirq.Simulator().run(program=circuit, repetitions=repetitions)

a = np.array(result.measurements['a'][:, 0])
b = np.array(result.measurements['b'][:, 0])
x = np.array(result.measurements['x'][:, 0])
y = np.array(result.measurements['y'][:, 0])
outcomes = a ^ b == x & y
winPercent = len([e for e in outcomes if e]) * 100 / repetitions

print()
print('This is Results')
print('This is a:', bitstring(a))
print('This is b:', bitstring(b))
print('This is x:', bitstring(x))
print('This is y:', bitstring(y))
print('This is (a XOR b) == (x AND y):\n  ', bitstring(outcomes))
print('This is Win rate: {}%'.format(winPercent))








