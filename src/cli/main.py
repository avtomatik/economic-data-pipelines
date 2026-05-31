from datasets.imf.pipeline import run

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"Pipeline failed: {e}")
