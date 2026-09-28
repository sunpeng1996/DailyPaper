---
title: Improving Visual Sensitivity of LLMs on Multimodal Machine Translation with
  Metric-based Loss Weighting
title_zh: 基于度量损失加权提升多模态大模型机器翻译的视觉敏感度
authors:
- Paweł Mąka
- Piotr Andruszkiewicz
- Yusuf Can Semerci
- Jan Scholtes
- Gerasimos Spanakis
affiliations:
- Maastricht University
- Warsaw University of Technology
- IDEAS Research Institute
arxiv_id: '2609.31169'
url: https://arxiv.org/abs/2609.31169
pdf_url: https://arxiv.org/pdf/2609.31169
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: 多模态大模型 · 损失加权训练优化
tags:
- Multimodal LLM
- Loss Weighting
- Visual Grounding
- Fine-tuning
- Machine Translation
one_liner: 提出基于PCXMI与一致性PCXMI的度量损失加权训练法，提升多模态翻译视觉敏感度，精度最高涨7pp
practical_value: '- 多模态推荐/搜索场景可复用PCXMI度量识别对视觉信息敏感的token，针对性调整训练损失权重，提升图文商品特征利用率，优化多模态召回、文案生成效果

  - 训练多模态大模型时可复用双度量（基础PCXMI+一致性PCXMI）联合加权思路，避免模型忽略非文本模态输入，同时保障通用任务性能无劣化

  - 该方案仅调整损失计算逻辑无需修改模型架构，工程落地成本低，可快速迁移到商品图文理解、多模态query理解等业务场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
多模态机器翻译任务中，现有模型常忽略输入的图像信息，无法通过视觉信号解决文本歧义问题，提升模型视觉敏感度是核心痛点。

### 方法关键点
1. 提出度量驱动的损失加权训练方案，对可从图像中获益的token增大损失权重，强化视觉对齐
2. 基于逐点交叉互信息（PCXMI）对比有无视觉上下文时的模型输出概率，识别视觉敏感token
3. 新增一致性PCXMI度量，双度量组合使用效果最优，无需修改模型架构仅调整损失计算逻辑

### 关键结果
在CoMMuTE对比数据集上，相比标准微调精度最高提升7个百分点以上，同时通用翻译性能无明显下降
