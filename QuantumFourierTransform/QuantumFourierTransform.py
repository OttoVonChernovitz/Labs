import numpy as np
import cirq

def main():
    qftCircuit = generateGridCircuit()
    print('This is Circuit:')
    print(qftCircuit)

    simulator = cirq.Simulator()
    result = simulator.simulate(qftCircuit)
    print()
    print('This is FinalState')
    print(np.around(result.final_state, 5))

def czAndSwap(q0, q1, rot):
    yield cirq.CZ(q0, q1)**rot
    yield cirq.SWAP(q0,q1)


def generateGridCircuit():
    a,b,c,d = [cirq.GridQubit(0, 0), cirq.GridQubit(0, 1),
               cirq.GridQubit(1, 1), cirq.GridQubit(1, 0)]

    circuit = cirq.Circuit.from_ops(
        cirq.H(a),
        czAndSwap(a, b, 1),
        czAndSwap(b, c, 0.5),
        czAndSwap(c, d, 0.25),
        cirq.H(a),
        czAndSwap(a, b, 0.5),
        czAndSwap(b, c, 0.25),
        czAndSwap(c, d, 0.125),
        cirq.H(a),
        czAndSwap(a, b, 0.25),
        czAndSwap(b, c, 0.125),
        cirq.H(a),
        czAndSwap(a, b, 0.125),
        cirq.H(a),
        strategy=cirq.InsertStrategy.EARLIEST
    )
    return circuit

if __name__ == '__main__':
    main()
