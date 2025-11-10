thonimport json
import os

def export_data(data):
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "search_results.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Data has been exported to {output_file}")