---
title: Closing the Modality Gap via Simplex-Constrained Representations
title_zh: 通过单纯形约束表征消除多模态模型的模态鸿沟
authors:
- Shubham Gupta
- Siva Reddy
- Perouz Taslakian
- Valentina Zantedeschi
- Cem Subakan
affiliations:
- Mila – Québec AI Institute
- ServiceNow Research
- McGill University
- Université Laval
arxiv_id: '2610.32890'
url: https://arxiv.org/abs/2610.32890
pdf_url: https://arxiv.org/pdf/2610.32890
published: '2026-10-23'
collected: '2026-10-26'
category: Multimodal
direction: 多模态表征对齐 · 模态鸿沟消除
tags:
- Multimodal Alignment
- Modality Gap
- Contrastive Learning
- Embedding Calibration
- Simplex Representation
one_liner: 将多模态嵌入域从单位球面改为概率单纯形，缩减97%-99%模态质心L2 gap且检索性能持平甚至更优
practical_value: '- 多模态召回场景可复用本方案的轻量softmax adapter改造现有CLIP类模型，无需重训主干即可大幅降低模态gap，提升跨模态检索精度

  - 可将概率单纯形嵌入、Total Variation相似度替代传统余弦相似度，用于商品图文检索、直播内容多模态匹配等业务场景的相似度计算优化

  - 跨模态语义对齐需求的场景（如AI导购多轮对话的图文匹配），可优先采用单纯形约束作为结构先验，避免盲目调整对比损失带来的性能下降'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
CLIP、CLAP等多模态对比模型虽能学习共享表征，但嵌入存在稳定模态鸿沟，既可能导致跨模态相似度校准偏差、降低检索性能，又无法直接消除以免扰动单模态内部几何结构、损害下游效果，现有方案多需修改损失或模型主干，落地成本较高。
### 方法关键点
1. 纯几何改造：将嵌入域从传统单位球面切换至概率单纯形，利用其非负、单位质量约束作为结构先验，强制不同模态在同一坐标系下校准对齐
2. 工程改动极小：仅在原有模型后接入轻量softmax适配器，相似度计算替换为Total Variation相似度，无需修改主干模型与对比损失
### 关键结果数字
- 5个多模态检索基准上，模态质心L2 gap降低97%~99%
- 跨模态检索性能匹配甚至优于原生无约束模型，无性能损失
