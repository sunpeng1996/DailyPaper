---
title: AI translation of literary texts is "fine", but readers still prefer human
  translations
title_zh: 文学文本AI翻译效果尚可，但读者仍更偏好人工翻译
authors:
- Yves Ferstler
- Adam Podoxin
- Ty Brassington
- Roman Grundkiewicz
- Maite Taboada
- Marzena Karpinska
affiliations:
- Simon Fraser University
- Université du Québec à Montréal
- Microsoft
arxiv_id: '2606.26040'
url: https://arxiv.org/abs/2606.26040
pdf_url: https://arxiv.org/pdf/2606.26040
published: '2026-06-23'
collected: '2026-07-05'
category: Eval
direction: 大模型翻译评测 · 读者偏好对齐
tags:
- LLM
- Translation
- Evaluation
- Human Preference
- Dataset
one_liner: 通过读者实验对比文学领域AI与人工翻译偏好，发布面向读者的文学翻译评测数据集LAIT
practical_value: '- 做文案/商品标题/营销内容AI生成效果评测时，不可仅依赖自动指标或LLM-as-judge，需补充真实用户的沉浸式体验打分，适配沉浸感、吸引力等主观指标场景

  - 用户存在「认知锚定效应」：相信内容为人工创作时会给出更高偏好评分，做内容类A/B测试时需做好双盲设计避免结果偏差

  - 长文本生成/翻译的质量波动是核心体验短板，做长文案、商品描述批量生成时可增加分段质量校验逻辑降低内容波动'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有机器翻译的自动指标、面向流利度/准确度的人工评测，无法捕捉文学翻译的沉浸感、文学效果等读者主观体验维度，AI文学翻译的实际用户感知尚不明确。
### 方法关键点
招募15名深度读者，对比15本法、波兰、日语小说的人工翻译（HT）与基于Agent LLM流水线的机器翻译（MT）效果，设置整段沉浸式阅读、对齐片段精读两种评测场景，控制呈现顺序做交叉验证。
### 关键结果数字
读者认为MT效果尚可，但63%的整段对比、67.6%的片段对比中更偏好HT，核心优势为易读、清晰、沉浸感强；读者仅56.7%的概率可正确区分HT与MT，且倾向偏好自己判定为人工的版本；包括LLM-as-judge在内的自动指标均无法复现读者偏好，反而更倾向MT；发布含1K读者评论、2K偏好打分、7.2K片段标注的LAIT评测数据集。
