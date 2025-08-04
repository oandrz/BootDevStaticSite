#!/usr/bin/env python3
"""
Test script for the recursive directory copy function.
This demonstrates how to use the copy_directory_recursive function.
"""

from src.file_utils import copy_directory_recursive, copy_static_to_public
import os


def test_copy_function():
    """Test the copy function with different scenarios."""
    
    print("=== Testing Recursive Directory Copy Function ===\n")
    
    # Test 1: Copy static to public (the main use case)
    print("Test 1: Copying static directory to public directory")
    print("-" * 50)
    success = copy_static_to_public()
    print(f"Result: {'SUCCESS' if success else 'FAILED'}\n")
    
    # Test 2: Copy with custom logging
    print("Test 2: Copying with custom source and destination")
    print("-" * 50)
    success = copy_directory_recursive("static", "test_output", log_operations=True)
    print(f"Result: {'SUCCESS' if success else 'FAILED'}\n")
    
    # Test 3: Copy without logging
    print("Test 3: Copying without logging (silent mode)")
    print("-" * 50)
    success = copy_directory_recursive("static", "test_output_silent", log_operations=False)
    print(f"Result: {'SUCCESS' if success else 'FAILED'}\n")
    
    # Test 4: Error handling - non-existent source
    print("Test 4: Error handling - non-existent source directory")
    print("-" * 50)
    success = copy_directory_recursive("non_existent_dir", "test_output", log_operations=True)
    print(f"Result: {'SUCCESS' if success else 'FAILED'}\n")
    
    # Clean up test directories
    print("Cleaning up test directories...")
    import shutil
    for test_dir in ["test_output", "test_output_silent"]:
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
            print(f"Removed {test_dir}")
    
    print("\n=== Test completed ===")


if __name__ == "__main__":
    test_copy_function() 