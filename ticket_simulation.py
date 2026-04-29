import random
from queue import Queue

class TicketCounterSimulation:
    def __init__(self, num_agents, num_seconds, arrival_prob, service_time_range):
        """
        num_agents: jumlah petugas loket
        num_seconds: lama simulasi (detik)
        arrival_prob: probabilitas kedatangan penumpang tiap detik (0–1)
        service_time_range: tuple (min_time, max_time)
        """
        self.num_agents = num_agents
        self.num_seconds = num_seconds
        self.arrival_prob = arrival_prob
        self.service_time_range = service_time_range

        self.queue = Queue()
        self.agents = [None] * num_agents  # tiap agent: (end_time, arrival_time)

        self.total_wait_time = 0
        self.num_served = 0

    def run(self):
        for cur_time in range(self.num_seconds):
            self._handleArrival(cur_time)
            self._handleEndService(cur_time)
            self._handleBeginService(cur_time)

        self._printResults()

    # ===============================
    # EVENT HANDLERS
    # ===============================

    def _handleArrival(self, cur_time):
        if random.random() < self.arrival_prob:
            # simpan waktu kedatangan
            self.queue.enqueue(cur_time)

    def _handleBeginService(self, cur_time):
        for i in range(self.num_agents):
            if self.agents[i] is None and not self.queue.isEmpty():
                arrival_time = self.queue.dequeue()

                service_time = random.randint(
                    self.service_time_range[0],
                    self.service_time_range[1]
                )

                end_time = cur_time + service_time

                # agent mulai melayani
                self.agents[i] = (end_time, arrival_time)

    def _handleEndService(self, cur_time):
        for i in range(self.num_agents):
            if self.agents[i] is not None:
                end_time, arrival_time = self.agents[i]

                if cur_time >= end_time:
                    wait_time = cur_time - arrival_time
                    self.total_wait_time += wait_time
                    self.num_served += 1

                    # agent kosong lagi
                    self.agents[i] = None

    # ===============================
    # OUTPUT
    # ===============================

    def _printResults(self):
        avg_wait = (
            self.total_wait_time / self.num_served
            if self.num_served > 0 else 0
        )

        print("\n=== HASIL SIMULASI ===")
        print(f"Total dilayani     : {self.num_served}")
        print(f"Masih dalam antrean: {self.queue.size()}")
        print(f"Rata-rata tunggu   : {avg_wait:.2f} detik")