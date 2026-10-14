---
title: Visual Grounding Safety in Vision-Language Models
title_zh: 多模态视觉语言模型的视觉定位输出安全性研究
authors:
- Erfan Shayegani
- Kundan Krishna
- Yue Dong
- Nael Abu-Ghazaleh
- Leon Gatys
- Shruti Palaskar
affiliations:
- University of California, Riverside
- Apple
arxiv_id: '2610.05637'
url: https://arxiv.org/abs/2610.05637
pdf_url: https://arxiv.org/pdf/2610.05637
published: '2026-10-04'
collected: '2026-10-14'
category: Multimodal
direction: 多模态大模型 · 安全对齐优化
tags:
- VLM
- Visual Grounding
- Safety Alignment
- Fine-tuning
- Multimodal Model
one_liner: 揭示VLM视觉定位输出的安全漏洞，提出兼顾能力与安全的结构化输出对齐微调方案
practical_value: '- 多模态Agent（如电商导购Agent、GUI操作Agent）对接VLM输出时，需单独校验视觉定位（bounding box/点坐标）输出的合规性，不可直接复用文本输出的安全校验逻辑

  - 多模态模型结构化输出的安全对齐，可复用「结构化拒绝样本+能力保留数据+自蒸馏良性数据」三混合微调策略，避免对齐后原生能力下降

  - 电商场景违规商品识别的多模态模型对齐，可参考该方案平衡违规拦截率与正常请求误拒率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM输出的视觉定位结果（点、bounding box）可直接被下游Agent、机器人、GUI系统调用执行，但这类结构化输出的安全对齐未被系统研究，存在直接触发有害动作的风险。
### 方法关键点
1. 重构3类安全基准（直接伤害VLSU、社会偏见BBQ-V、场景安全Asimov-2.0）生成15401组配对有害请求，仅输出要求不同：自由文本VQA/视觉定位
2. 采用三混合微调策略：结合定位格式拒绝样本、能力保留定位数据、自蒸馏良性数据，同时规避过度拒绝问题
### 关键结果
- 5款主流VLM的定位输出拒绝率比文本VQA拒绝率低31~59个百分点，常规系统提示无法弥补该差距
- 微调后Qwen3-VL-8B、VisionReasoner-7B的定位拒绝率在VLSU/BBQ-V上提升77~95个百分点，在域外Asimov-2.0上提升64~85个百分点，同时保留原生定位能力、过度拒绝率可控
