"""
Sorting Assignment Starter Code
Implement five sorting algorithms and benchmark their performance.
"""

import json
import time
import random
import tracemalloc


# ============================================================================
# PART 1: SORTING IMPLEMENTATIONS
# ============================================================================

def bubble_sort(arr):
    """Bubble sort algorithm (stable)."""
    n = len (arr)
    a = arr.copy()
    for i in range(n): 
        for j in range(0, n - i - 1): 
            if a[j] > a[j+ 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a 
    

def selection_sort(arr):
    """Selection sort algorithm (unstable)."""
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]: 
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    """Insertion sort algorithm (stable)."""
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i[
        j = i - 1
        while j >= 0 and a[j] > key: 
            a[j + 1] = key
        return a


def merge_sort(arr):
    """Merge sort algorithm (stable)."""
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else: 
                merged.append(right[j])
                j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
    
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])
    return merge(left_sorted, right_sorted) 


# ============================================================================
# PART 2: STABILITY DEMONSTRATION
# ============================================================================

def demonstrate_stability():
    "Test which algorithms preserve order for equal elements."""
    products = [
        {"name": "Widget A", "price": 1999, "original_position": 0},
        {"name": "Gadget B", "price": 999, "original_position": 1},
        {"name": "Widget C", "price": 1999, "original_position": 2},
        {"name": "Tool D", "price": 999, "original_position": 3},
        {"name": "Widget E", "price": 1999, "original_position": 4},
    ]
    
   def is_stable(sorted_products):
       last_price = None 
       last_positions = []
       for p in sorted_products: 
               if p["price"] != last_price: 
                   last_price = p["price"]
                   last_position = [p["original_position"]]
               else:
                   last_positions.append(p["original_position"])
                   if last_positions != sorted(last_positions):
                       return False 
        return True 

    results = {}
    algorithms = {
        "bubble_sort": "Not tested",
        "selection_sort": "Not tested", 
        "insertion_sort": "Not tested",
        "merge_sort": "Not tested"
    }
    
    for name, func in algorithms.items(): 
        prices = [p["price"] for p in products]
        sorted_prices = func(prices)
        sorted_products = []
        for price in sorted_prices: 
            for p in products: 
                if p not in sorted_Products and p["price"] == price:
                    sorted_products.append(p)
                    break 
        results[name] = "Stable" if is_stable(sorted_products) else "Unstable"
    
    return results


# ============================================================================
# PART 3: PERFORMANCE BENCHMARKING
# ============================================================================

def load_dataset(filename):
    """Load a dataset from JSON file."""
    with open(f"datasets/{filename}", "r") as f:
        return json.load(f)


def load_test_cases():
    """Load test cases for validation."""
    with open("datasets/test_cases.json", "r") as f:
        return json.load(f)


def test_sorting_correctness():
    """Test that sorting functions work correctly on small test cases."""
    print("="*70)
    print("TESTING SORTING CORRECTNESS")
    print("="*70 + "\n")
    
    test_cases = load_test_cases()
    
    test_names = ["small_random", "small_sorted", "small_reverse", "small_duplicates"]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    for test_name in test_names:
        print(f"Test: {test_name}")
        print(f"  Input:    {test_cases[test_name]}")
        print(f"  Expected: {test_cases['expected_sorted'][test_name]}")
        print()
        
        for algo_name, algo_func in algorithms.items():
            try:
                result = algo_func(test_cases[test_name].copy())
                expected = test_cases['expected_sorted'][test_name]
                status = "✓ PASS" if result == expected else "✗ FAIL"
                print(f"    {algo_name:20s}: {result} {status}")
            except Exception as e:
                print(f"    {algo_name:20s}: ERROR - {str(e)}")
        
        print()


def benchmark_algorithm(sort_func, data):
    data_copy = data.copy()
    tracemalloc.start()
    start_time = time.perf_counter()
    sort_func(data_copy)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return (end - start) * 100, peak / 1024 

def benchmark_all_datasets():
    datasets = {
        "orders.json": ("Order Processing Queue", 50000, 5000),
        "products.json": ("Product Catalog", 100000, 5000),
        "inventory.json": ("Inventory Reconciliation", 25000, 5000),
        "activity_log.json": ("Customer Activity Log", 75000, 5000)
    }
    
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    for filename, (description, full_size, sample_size) in datasets.items():
        print(f"Dataset: {description} ({sample_size:,} element sample)")        
        data = load_dataset(filename)[:sample_size]
        for algo_name, algo_func in algorithms.items():
            try:
                exec_time, memory = benchmark_algorithm(algo_func, data_sample)
                print(f"  {algo_name:20s}: {exec_time:8.2f} ms | {memory:8.2f} KB")
            except Exception as e:
                print(f"  {algo_name:20s}: ERROR - {str(e)}")
        
        print()


def analyze_stability():
    """Test and display which algorithms are stable."""
    print("="*70)
    print("STABILITY ANALYSIS")
    print("="*70 + "\n")
    
    print("Testing which algorithms preserve order of equal elements...\n")
    
    results = demonstrate_stability()
    
    for algo_name, stability in results.items():
        print(f"  {algo_name:20s}: {stability}")
    
    print()


if __name__ == "__main__":
    print("SORTING ASSIGNMENT - FINAL CODE\n")

    test_sorting_correctness()

    benchmark_all_datasets()

    analyze_stablity()
