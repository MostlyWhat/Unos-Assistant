Classes and Functions Overview
==========================================

**UNOS** is the main class that handles everything from booting to executing commands.

.. py:class:: UNOS
       
       .. py:method:: __init__(self)
       .. py:method:: UNOSinitialize(self)
       .. py:method:: Verify(self)
       .. py:method:: StartupText(self)
       .. py:method:: speak(self, audio: str)
       .. py:method:: MainWindow(self))
       .. py:method:: create_audio_tts(self, text)
       .. py:method:: RecognizeUNOS(self)
       .. py:method:: RecognizeAudio(self)
       .. py:method:: runningCommand(self)

**MicrophoneStream** is the main class that handles streaming audio input from microphone.

.. py:class:: MicrophoneStream

        .. py:method:: __init__(self, rate, chunk)
        .. py:method:: __enter__(self)
        .. py:method:: __exit__(self, type, value, traceback)
        .. py:method:: _fill_buffer(self, in_data, frame_count, time_info, status_flags)
        .. py:method:: generator(self)