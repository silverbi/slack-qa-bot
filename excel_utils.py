import pandas as pd

def read_function_spec_from_excel(file_bytes):
    return pd.read_excel(file_bytes)

def convert_to_testcase_df(all_cases):
    rows = []
    for case in all_cases:
        rows.append({
            "0depth": case.get("0depth", ""),
            "1depth": case.get("1depth", ""),
            "2depth": case.get("2depth", ""),
            "3depth": case.get("3depth", ""),
            "objective": case.get("objective", ""),
            "precondition": case.get("precondition", ""),
            "test step": case.get("test step", ""),
            "expected result": case.get("expected result", ""),
            "결과": "",
            "Bug 티켓": "",
            "비고": ""
        })
    return pd.DataFrame(rows)
