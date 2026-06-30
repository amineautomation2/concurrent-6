import argparse
import time

from chelseafinancial import chelsea_total_pages, process_per_worker
from utils import create_spreadsheet, get_xlsx_filepath
from worker import merge_csv_to_xlsx, write_csv_by_id


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=str, help="id worker")
    parser.add_argument("--max", type=str, help="max worker")
    parser.add_argument("--fresh", action="store_true", help="create fresh spreadsheet")
    parser.add_argument("--merge", action="store_true", help="merge csvs")
    args = parser.parse_args()

    xlsx_out = get_xlsx_filepath("chelsea_financial.xlsx")
    cols = ["name", "isin", "url", "is_closed"]

    if args.id and args.max:
        total = chelsea_total_pages()
        data = process_per_worker(int(args.id), int(args.max), total)
        csv_file = f"chelsea_{int(args.id)}_Funds.csv"
        for d in data:
            d.pop("type_code")
            is_closed = d.get("is_closed")
            if is_closed is not None:
                d.update(dict(is_closed=not is_closed))

        write_csv_by_id(csv_file, data, cols)

    elif args.merge:
        merge_csv_to_xlsx(xlsx_out, cols, "Funds")

    elif args.fresh:
        create_spreadsheet(xlsx_out, ["Funds"], ["Name", "ISIN", "URL", "OPEN"])

    # data = chelsea_runner()
    # write_data(data)
    # for fund in data:
    #    if fund.get("url"):
    #        isin = isin_from_pdf(fund["url"])
    #        fund.update(dict(isin=isin))
    #    break
    # for fund in data:
    #    print(fund)


if __name__ == "__main__":
    start_time = time.perf_counter()

    main()
    elapsed_time = time.perf_counter() - start_time
    print(f"Execution time: {elapsed_time:.2f} seconds")
