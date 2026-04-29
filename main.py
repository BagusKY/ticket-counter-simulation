from ticket_simulation import TicketCounterSimulation

def main():
    sim = TicketCounterSimulation(
        num_agents=2,
        num_seconds=100,
        arrival_prob=0.3,
        service_time_range=(2, 5)
    )
    sim.run()

if __name__ == "__main__":
    main()