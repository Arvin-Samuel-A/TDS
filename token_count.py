import tiktoken

# Initialize the tokenizer for GPT-4o-mini
encoder = tiktoken.get_encoding("o200k_base")

# Define your prompt
prompt = """List only the valid English words from these: z5YM3dzTSJ, JZ, tflWQVlP, jMeIZ, suktb, wI4UUh, 6DRddNv0, sFip, rsXHik7u3, cQecxv, j5GA, VdHrzP, 89iQ4, FjphWXaTr, gBWKRS0Gvc, X3n8UtAL, dlUt54OOh, ngwwCNRd, eKE5dX, qF7qEx, UxEB, ZGY8VXBO, gFF6, CDexydmGrc, Kc3x, mgRZIb4tG, qoFDR63, K, tOZo, spU2Xn4Tg, wVQEDSwy, Z1, W, 2, H7a, XoPEI, 01m66unXm3, FUl, Dut, nt1, uBN12, 2VAcrwU8u1, I, 3KTUfZf, UinaHlU8a, RVkNxIS, uN, yQepe7F4m, 5VvsL, 4Khe6Pb9, LgQ, bULbG8c, t7moRMl, OcnFEKd, PjZVPY, 9U1m19, eIFr, eHni, zwKfNXGCq, Cq"""

# Tokenize the prompt
tokens = encoder.encode(prompt)

# Output the number of tokens
print(f"Number of tokens: {len(tokens)}")
