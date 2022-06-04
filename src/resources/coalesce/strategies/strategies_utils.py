from typing import Dict, List


class StrategiesUtils:
    @classmethod
    def group_by_key(cls, datasets_list: List[Dict[str, int]]):
        grouped = dict()
        for dataset in datasets_list:
            for key, value in dataset.items():
                if key in grouped:
                    grouped[key].append(value)
                else:
                    grouped[key] = [value]
        return grouped
