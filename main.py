import sys

def auto_scale(cpu_usages, min_instances=2, max_instances=8, high=70, low=35):
    instances = min_instances
    for i, cpu in enumerate(cpu_usages):
        print(f"--- Iteration {i+1}/{len(cpu_usages)} ---")
        print(f"Current CPU: {cpu}% | Instances: {instances}")
        if cpu > high and instances < max_instances:
            instances += 1
            print(f"SCALE UP: Added instance. Total instances: {instances}")
        elif cpu < low and instances > min_instances:
            instances -= 1
            print(f"SCALE DOWN: Removed instance. Total instances: {instances}")
        else:
            print("CPU usage within acceptable range. No scaling needed.")
        print()

if __name__ == "__main__":
    # Example: Input file has one CPU usage percent per line
    if len(sys.argv) < 2:
        print("Usage: python main.py input.txt")
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        cpu_usages = [float(line.strip()) for line in f if line.strip()]
    auto_scale(cpu_usages)
