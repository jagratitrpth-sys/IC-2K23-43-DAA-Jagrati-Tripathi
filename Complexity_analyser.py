import time
import random
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(25000)

class PerformanceAnalyzer:
    @staticmethod
    def measure_time(func, *args):
        start = time.perf_counter()
        func(*args)
        return time.perf_counter() - start

    @staticmethod
    def run_and_plot(algorithms, sizes, data_generator, title, ylabel="Time (seconds)"):
        results = {alg.__name__: [] for alg in algorithms}

        print(f"Running benchmarks for {title}...")
        for n in sizes:
            # Generate fresh data for this size
            test_data = data_generator(n)
            
            for alg in algorithms:
                # Use a copy of the data so in-place sorts don't affect each other
                time_taken = PerformanceAnalyzer.measure_time(alg, test_data.copy() if isinstance(test_data, list) else test_data)
                results[alg.__name__].append(time_taken)

        # Plotting logic
        plt.figure(figsize=(10, 6))
        markers = ['o', 's', '^', 'x', 'd', '*', '+']
        
        for idx, (alg_name, times) in enumerate(results.items()):
            plt.plot(sizes, times, label=alg_name, marker=markers[idx % len(markers)])

        plt.title(title)
        plt.xlabel("Input Size (N)")
        plt.ylabel(ylabel)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        
        # Save instead of just showing, fulfilling the file storage requirement
        filename = f"{title.replace(' ', '_').lower()}_graph.png"
        plt.savefig(filename)
        print(f"Graph saved as {filename}")
        plt.show()