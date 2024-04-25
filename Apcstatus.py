import subprocess
import re

def get_apc_voltage():
  """
  Executes the apcacces command and extracts the voltage value.

  Returns:
      The extracted voltage as a float or None if there's an error.
  """
  try:
    # Execute the command with PIPE to capture standard output
    process = subprocess.Popen(["apcaccess", "-p", "LINEV"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Get the output and error (if any)
    output, error = process.communicate()
    # Decode the output (may need adjustments based on your encoding)
    output_decoded = output.decode("utf-8").strip()
    
    # Use regular expression to extract voltage value (assuming format with digits and '.')
    match = re.search(r"(\d+\.\d+) Volts", output_decoded)
    if match:
      voltage_str = match.group(1)
      return float(voltage_str)
    else:
      return None
  except subprocess.CalledProcessError:
    print("Error running apcacces command")
    return None
  except UnicodeDecodeError:
    print("Error decoding output, check encoding")
    return None

# Get the voltage or None if there's an error
voltage = get_apc_voltage()

if voltage:
  if 
  print(f"Voltage: {voltage} Volts")
else:
  print("Error: Could not extract voltage")
