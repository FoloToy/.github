# Organization profile design

The public organization profile is `profile/README.md`. It uses GitHub-supported Markdown, a two-column HTML table, and local PNG assets; no CSS, scripts, external fonts, or image-host services are required.

## Assets

- `profile/assets/ai-passport.png`: https://ai-passport.folotoy.cn/assets/ai-passport-product-showcase-transparent.png
- `profile/assets/wordmark.png`: https://github.com/FoloToy/ai-passport/blob/main/assets/images/logo-wordmark.png
- `profile/assets/magicbox.png`: https://github.com/FoloToy/MagicBox/blob/main/docs/images/magicbox-overview.png
- `hero.png`, `ai-passport-card.png`, `magicbox-card.png`: composed from the above FoloToy assets by `build_assets.py`. Product imagery retains its proportions.

Run `python3 design/build_assets.py` with Pillow and the macOS fonts referenced in the script to regenerate the layout. The checked-in PNGs require no runtime dependencies.

Structure follows the reference https://github.com/makecindy: brand hero → useful links → bilingual introduction → project navigation. The visual design uses FoloToy's own logo and product photography.

Optional organization settings: description “AI companions, open hardware, and things you make your own. · 让 AI 走进真实世界。”; website https://ai-passport.folotoy.cn; pinned public repositories `ai-passport`, `MagicBox`, `ai-passport-arduino`, `ai-passport-micropython`, `folotoy-server-self-hosting`, `folotoy-doc`. These settings are recommendations, not applied by this change.
