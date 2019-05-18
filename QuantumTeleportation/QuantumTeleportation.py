import numpy as np
import cirq


def makeQuantumTeleportationCircuit(ranX, ranY):
    circuit = cirq.Circuit()
    MSG, user1, user2 = cirq.LineQubit.range(3)

    circuit.append([cirq.H(user1), cirq.CNOT(user1, user2)])
    circuit.append([cirq.X(MSG)**ranX, cirq.Y(MSG)**ranY])
    circuit.append([cirq.CNOT(MSG, user1), cirq.H(MSG)])
    circuit.append(cirq.measure(MSG, user1))
    circuit.append([cirq.CNOT(user1, user2), cirq.CZ(MSG, user2)])

    return circuit

def main():
    ranX = float(input('This is X = '))
    ranY = float(input('This is Y = '))
    circuit = makeQuantumTeleportationCircuit(ranX, ranY)

    print("This is Circuit:")
    print(circuit)

    sim = cirq.Simulator()

    q0, q1 = cirq.LineQubit.range(2)

    message = sim.simulate(cirq.Circuit.from_ops(
        [cirq.X(q0)**ranX, cirq.Y(q1)**ranY]))

    print("\nThis is Bloch Sphere of Message After X and Y Gates:")
    b0X, b0Y, b0Z = cirq.bloch_vector_from_state_vector(
        message.final_state, 0)
    print("This is x: ", np.around(b0X, 4),
          "This is y: ", np.around(b0Y, 4),
          "This is z: ", np.around(b0Z, 4))

    final_results = sim.simulate(circuit)

    print("\n This is Bloch Sphere of Qubit 2 at Final State:")
    b2X, b2Y, b2Z = cirq.bloch_vector_from_state_vector(
        final_results.final_state, 2)
    print("This is x: ", np.around(b2X, 4),
          "This is y: ", np.around(b2Y, 4),
          "This is z: ", np.around(b2Z, 4))


if __name__ == '__main__':
    main()
