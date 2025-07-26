# Code Watermarking System for Aura Insurance Engine

## Overview

This document describes the invisible watermarking system implemented to prove authorship of the Aura Insurance Engine codebase.

## Method: Zero-Width Character Encoding

### How It Works

- Uses invisible Unicode characters (U+200B, U+200C, U+200D, U+2060)
- Encodes text into binary, then maps binary pairs to zero-width characters
- Inserts watermark after copyright headers in stable files

### Signature Format

```
AURA:Jose Reyes (@reyesjl):2025-07-26
```

### Files Watermarked

1. `aura_frontend/src/types/User.ts`
2. `aura_frontend/src/types/ApplicationSession.ts`
3. `aura_frontend/src/types/Question.ts`
4. `aura_frontend/src/components/FootBar.vue`
5. `aura_backend/core/models.py`
6. `README.md`

## Tools

### Adding Watermarks

```bash
python3 add_watermark.py
```

### Verifying Watermarks

```bash
python3 verify_watermark.py <filename>
```

### Example Verification

```bash
$ python3 verify_watermark.py aura_frontend/src/components/FootBar.vue
✓ Watermark found in aura_frontend/src/components/FootBar.vue
  Decoded text: AURA:Jose Reyes (@reyesjl):2025-07-26
  Character count: 148
```

## Characteristics

### Advantages

- **Completely Invisible**: No visual change to code
- **Copy-Resistant**: Survives copy/paste operations
- **Format-Agnostic**: Works with any text-based file
- **Undetectable**: Cannot be seen without specialized tools
- **Persistent**: Remains through most code transformations

### Technical Details

- Each character encoded as 8 bits
- Binary pairs mapped to specific zero-width characters
- 148 invisible characters encode the full signature
- Compatible with all modern text editors and systems

## Proof of Authorship

This watermarking system provides cryptographic proof that:

1. **Author**: Jose Reyes (@reyesjl)
2. **Project**: Aura Insurance Engine
3. **Date**: July 26, 2025
4. **Repository**: https://github.com/reyesjl/aura-insurance-engine

The watermarks are embedded in core, stable files that are unlikely to change frequently, ensuring long-term preservation of the authorship proof.

## Security Notes

- Watermarks survive most code copying and reformatting
- Even if someone discovers the watermarking system, the historical commits in Git provide additional proof
- The combination of copyright headers + invisible watermarks + Git history creates multiple layers of authorship proof
