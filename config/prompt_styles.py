# /Users/sango/Documents/nook2/nook/config/prompt_styles.py
from dataclasses import dataclass
import json
from pathlib import Path

@dataclass
class PromptStyle:
    translation_persona: str
    translation_style: str
    summary_persona: str
    summary_style: str

PROMPT_STYLES = {
    "normal": PromptStyle(
        translation_persona="プロの翻訳者",
        translation_style="自然な日本語に翻訳してください。",
        summary_persona="プロの要約者",
        summary_style="簡潔でわかりやすい要約を作成してください。"
    ),
    "kawaii": PromptStyle(
        translation_persona="かわいい翻訳者",
        translation_style="かわいい日本語に翻訳してください。",
        summary_persona="かわいい要約者",
        summary_style="かわいくて簡潔な要約を作成してください。"
    ),
    "cyber": PromptStyle(
        translation_persona="サイバーパンク翻訳者",
        translation_style="サイバーパンク風の日本語に翻訳してください。",
        summary_persona="サイバーパンク要約者",
        summary_style="サイバーパンク風で簡潔な要約を作成してください。"
    )
}

def save_prompt_styles(styles):
    styles_dict = {
        name: {
            "translation_persona": style.translation_persona,
            "translation_style": style.translation_style,
            "summary_persona": style.summary_persona,
            "summary_style": style.summary_style
        }
        for name, style in styles.items()
    }
    
    with open(Path(__file__).parent / "prompt_styles.json", "w", encoding="utf-8") as f:
        json.dump(styles_dict, f, indent=2, ensure_ascii=False)