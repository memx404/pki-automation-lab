import subprocess
import os
import sys
def test_pki_output():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    tool_path = os.path.join(current_dir, "pki_tool.py")
    result = subprocess.run(
        [sys.executable, tool_path],
        capture_output=True,
        text=True
    )
    output = result.stdout

    print("----- Capturing Tool Output -----")
    assert "Public Key:" in output, "Missing public key"
    assert "Private Key:" in output, "Missing private key"
    print("PKI tool test passed!")
if __name__ == "__main__":
    test_pki_output()
