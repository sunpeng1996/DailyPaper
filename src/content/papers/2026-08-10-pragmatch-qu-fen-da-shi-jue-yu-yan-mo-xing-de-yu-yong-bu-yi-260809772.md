---
title: 'PragMatch: Separating Pragmatic Incongruity from Cross-Modal Mismatch in Large
  Vision-Language Models'
title_zh: PragMatch：区分大视觉语言模型的语用不一致与跨模态不匹配
authors:
- Zhanna Mukhametsharip
- Vera Demberg
- Varsha Suresh
affiliations:
- Saarland University, Germany
- Max Planck Institute for Informatics, Germany
arxiv_id: '2608.09772'
url: https://arxiv.org/abs/2608.09772
pdf_url: https://arxiv.org/pdf/2608.09772
published: '2026-08-10'
collected: '2026-08-11'
category: Eval
direction: 多模态大模型评估 · 语用推理
tags:
- LVLM
- Multimodal Evaluation
- Pragmatic Reasoning
- Shortcut Learning
- Sarcasm Detection
one_liner: 提出含3000组图文对的PragMatch基准，揭示LVLM多模态语用推理依赖表层捷径的缺陷
practical_value: '- 做电商多模态内容审核（商品图文匹配、反讽类违规内容识别）时，需额外增加语用特征校验，避免模型被表层词汇/OCR线索误导

  - 评估商品AI文案、短视频配文等多模态生成内容质量时，可参考文中对照样本构建方法，加入字面匹配但语用矛盾的难负例提升评估鲁棒性

  - 微调多模态模型做广告/商品图文合规校验任务时，可针对性加入表层线索对抗训练，降低捷径学习带来的bad case'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LVLM在多模态任务上常依赖表层关联（捷径学习），现有评估框架无法区分模型是识别了带交际意图的语用不一致，还是单纯判断图文不匹配，尤其制约多模态反讽检测等高阶任务的性能可靠性。

### 方法关键点
1. 构建PragMatch受控基准，基于MMSD2.0生成3000组对照图文对，包含原始反讽样本、字面匹配样本、难负例样本；
2. 通过系统掩码定位影响模型判断的捷径线索，再通过定向注入实验量化各类线索的影响程度。

### 关键结果数字
LVLM预测对词汇、OCR、风格类表层线索高度敏感，注入表层信号后即使底层图文关系不变，模型预测也会出现大幅偏移，验证了现有LVLM语用推理能力的核心缺陷。
