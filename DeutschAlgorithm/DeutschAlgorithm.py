import cirq
from cirq import H, X, CNOT, measure


def main():
    q0, q1 = cirq.LineQubit.range(2)

    bits = [int(input("bit = ")) for _ in range(2)]
    secretFunction = []
    for x in bits:
        if x > 0 :
           secretFunction.append(1);
        else :
           secretFunction.append(0);
    
    oracle = makeOracle(q0, q1, secretFunction)
    print('This is Secret function:\nf(x) = <{}>'.format(
        ', '.join(str(e) for e in secretFunction)))

    circuit = makeDeutschCircuit(q0, q1, oracle)
    print('This is Circuit:')
    print(circuit)

    simulator = cirq.Simulator()
    result = simulator.run(circuit)
    print('This is Result of f(0)⊕f(1):')
    print(result)


def makeOracle(q0, q1, secretFunction):
    if secretFunction[0]:
        yield [CNOT(q0, q1), X(q1)]

    if secretFunction[1]:
        yield CNOT(q0, q1)


def makeDeutschCircuit(q0, q1, oracle):
    c = cirq.Circuit()

    c.append([X(q1), H(q1), H(q0)])

    c.append(oracle)

    c.append([H(q0), measure(q0, key='result')])
    return c


if __name__ == '__main__':
    main()
