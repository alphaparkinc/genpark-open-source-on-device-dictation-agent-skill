from client import OpenSourceOnDeviceDictationAgentClient

def main():
    client = OpenSourceOnDeviceDictationAgentClient()
    res = client.transcribe_locally(1024, "en")
    print(f"On-Device Verified: {res['is_on_device']}")
    print(f"Transcription: {res['transcription']}")

if __name__ == "__main__":
    main()
