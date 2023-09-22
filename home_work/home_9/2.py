import sys
print("Current sys.path:")
for path in sys.path:
    print(path)
custom_dir = '/path/to/your/custom/directory'
sys.path.append(custom_dir)

# Display the updated sys.path
print("\nUpdated sys.path:")
for path in sys.path:
    print(path)