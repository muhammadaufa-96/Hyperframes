#!/bin/bash
# Prepares a Claude Code cloud session for editing videos in this HyperFrames project:
# CLI + render browser, Malay-capable whisper model, face-blur model and Python helpers.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

HF_VERSION=0.8.164
WHISPER_DIR="$HOME/.cache/hyperframes/whisper/models"
WHISPER_MODEL="$WHISPER_DIR/ggml-large-v3-turbo.bin"
YUNET="$HOME/models/yunet.onnx"

# HyperFrames CLI (pinned to the version in package.json)
if [ "$(hyperframes --version 2>/dev/null || true)" != "$HF_VERSION" ]; then
  npm install -g "hyperframes@$HF_VERSION" >/dev/null 2>&1
fi

# Chrome headless shell used for rendering
hyperframes browser ensure >/dev/null 2>&1 || echo "warn: browser ensure failed" >&2

# Python helpers: Drive download, face blur, HEIC photos
pip install -q gdown==6.4.2 opencv-python-headless==5.0.0.93 pillow-heif==1.8.1 2>&1 | grep -v -i warning || true

# Multilingual whisper model (Bahasa Melayu captions); needs huggingface.co in the network allowlist
mkdir -p "$WHISPER_DIR"
if [ ! -s "$WHISPER_MODEL" ]; then
  curl -sSfL -o "$WHISPER_MODEL.part" \
    "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo.bin" \
    && mv "$WHISPER_MODEL.part" "$WHISPER_MODEL" \
    || echo "warn: whisper model download failed (is huggingface.co allowed?)" >&2
fi

# Face detector for blurring bystanders
mkdir -p "$(dirname "$YUNET")"
if [ ! -s "$YUNET" ]; then
  curl -sSfL -o "$YUNET" \
    "https://huggingface.co/opencv/face_detection_yunet/resolve/main/face_detection_yunet_2023mar.onnx" \
    || echo "warn: face model download failed" >&2
fi

# Build the whisper.cpp runtime once by transcribing one second of silence
if [ -s "$WHISPER_MODEL" ] && [ ! -d "$HOME/.cache/hyperframes/whisper/whisper.cpp" ]; then
  tmp=$(mktemp -d)
  ffmpeg -v error -f lavfi -i anullsrc=r=16000:cl=mono -t 1 "$tmp/s.wav"
  hyperframes transcribe "$tmp/s.wav" -d "$tmp" -m large-v3-turbo -l ms --json >/dev/null 2>&1 \
    || echo "warn: whisper runtime build failed" >&2
  rm -rf "$tmp"
fi
