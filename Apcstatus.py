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

def update_apcstatus_html(voltage):
  """
  Updates the content of a paragraph in /var/www/HTML/apcstatus.html.
  Args:
      status: The new content to be placed between the <p> tags.
  """
  try:
    # Open the file in read mode
    with open("/var/www/HTML/apcstatus.html", "r") as file:
      html_content = file.read()

    # Replace the paragraph content with the status variable
    new_content = html_content.replace("<p> Test </p>", f"<p> {voltage} </p>")

    # Open the file again in write mode (overwrites existing content)
    with open("/var/www/HTML/apcstatus.html", "w") as file:
      file.write(new_content)
    print(f"Successfully updated apcstatus.html with status: {voltage}")
  except FileNotFoundError:
    print("Error: File not found at /var/www/HTML/apcstatus.html")
  except Exception as e:
    print(f"Error updating file: {e}")

# Get the voltage or None if there's an error
voltage = get_apc_voltage()
update_apcstatus_html(voltage)


if voltage:
  if voltage > 207:
    print(f"Voltage: {voltage} Volts")
    
  elif voltage > 0:
    print(f"Blackout\nVoltage: {voltage}  Volts")
    
else:
  print("Error: Could not extract voltage")
