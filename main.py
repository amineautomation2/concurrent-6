import sys
import os
import time
from chelseafinancial import chelsea_runner, write_data
from utils import get_random_user_agent, email_title


def main() -> None:
    data = chelsea_runner()
    write_data(data)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    elapsed_time = time.perf_counter() - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")
