def build_prompt(abstract, style):

    return f"""
You are a senior academic editor specializing in medical imaging and AI research.

Improve the following abstract:
- Strengthen novelty
- Improve clarity
- Maintain scientific tone
- Improve logical flow
- Keep under 300 words
- Use {style} writing style

Abstract:
{abstract}
"""
