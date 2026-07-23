class OpenSourceOnDeviceDictationAgentClient:
    def transcribe_locally(self, audio_buffer_size: int = 1024, language: str = "en") -> dict:
        return {
            "transcription": "Local on-device transcription completed with Whisper core engine.",
            "is_on_device": True
        }
