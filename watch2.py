import time
import threading

# Globals
running = False
start_time = 0
elapsed = 0
laps = []

def format_time(t):
    minutes = int(t // 60)
    seconds = int(t % 60)
    milliseconds = int((t - int(t)) * 1000)
    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

def display_timer():
    while True:
        if running:
            current = time.time() - start_time
            print("\rStopwatch: " + format_time(current), end="")
        time.sleep(0.05)

def stopwatch():
    global running, start_time, elapsed, laps
    print("Console Stopwatch with Lap")
    print("Commands:")
    print("  s - Start")
    print("  p - Pause")
    print("  r - Reset")
    print("  l - Lap")
    print("  q - Quit\n")

    threading.Thread(target=display_timer, daemon=True).start()

    while True:
        command = input("\nEnter command (s/p/r/l/q): ").strip().lower()

        if command == 's':
            if not running:
                start_time = time.time() - elapsed
                running = True
                print("Started.")
            else:
                print("Already running.")

        elif command == 'p':
            if running:
                elapsed = time.time() - start_time
                running = False
                print(f"\nPaused at {format_time(elapsed)}")
            else:
                print("Already paused.")

        elif command == 'r':
            running = False
            elapsed = 0
            start_time = 0
            laps.clear()
            print("\nReset to 00:00:000")

        elif command == 'l':
            if running:
                lap_time = time.time() - start_time
                laps.append(format_time(lap_time))
                print(f"\nLap {len(laps)}: {laps[-1]}")
            else:
                print("Cannot record lap while paused.")

        elif command == 'q':
            print("\nExiting stopwatch.")
            if laps:
                print("\n--- Lap Times ---")
                for i, lap in enumerate(laps, start=1):
                    print(f"Lap {i}: {lap}")
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    stopwatch()
