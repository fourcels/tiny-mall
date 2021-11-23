import uvicorn
import argparse


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-r', '--reload',
        action=argparse.BooleanOptionalAction,
        help="Enable auto-reload."
    )
    args = parser.parse_args()
    uvicorn.run(
        "tiny_mall.main:app",
        host="0.0.0.0",
        port=8000,
        reload=args.reload,
    )


if __name__ == "__main__":
    run()
