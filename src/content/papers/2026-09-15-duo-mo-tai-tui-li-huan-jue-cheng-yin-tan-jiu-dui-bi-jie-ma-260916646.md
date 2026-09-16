---
title: What Do Hallucinations Reveal About Multimodal Reasoning? Diagnosing Visual
  Grounding Failures via Contrastive Decoding Probes
title_zh: 多模态推理幻觉成因探究：对比解码探针诊断视觉对齐失败
authors:
- Zhipeng Zhao
- Wenxu Wang
- Peishun Liu
- Ruichun Tang
affiliations:
- Ocean University of China
arxiv_id: '2609.16646'
url: https://arxiv.org/abs/2609.16646
pdf_url: https://arxiv.org/pdf/2609.16646
published: '2026-09-15'
collected: '2026-09-16'
category: Multimodal
direction: 多模态推理 · 幻觉检测与抑制
tags:
- LVLM
- Hallucination Detection
- Contrastive Decoding
- Visual Grounding
- Multimodal Reasoning
one_liner: 提出无训练的SAFE对比解码框架，检测LVLM视觉幻觉并在解码阶段抑制幻觉生成
practical_value: '- 电商多模态场景（如商品图生成详情文案、直播内容质检）可直接复用SAFE无训练对比解码思路，无需微调即可检测生成内容与视觉输入的对齐度，降低幻觉率

  - 生成式推荐场景输出商品介绍、搜索结果文案时，可借鉴token级对比对齐得分作为解码惩罚项，在不损失生成流畅度的前提下减少不符合商品实际特征的错误描述

  - 多模态Agent处理拍图搜、商品图咨询等用户Query时，可参考「幻觉呈时间簇分布、早期干预效果好」的结论，在生成前3个token阶段就加入对齐校验，避免后续连锁幻觉'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：当前LVLM评估多聚焦基准跑分，缺乏对视觉幻觉等错误行为的可解释诊断手段，现有幻觉优化方案多需微调，落地成本高。
**方法关键点**：提出无训练的SAFE解码框架，对比视觉输入完整与视觉输入屏蔽的两条生成路径，计算token级对比对齐得分，识别模型依赖语言先验而非视觉证据的生成片段；该得分可同时作为无监督幻觉检测指标、解码阶段的惩罚项。
**关键结果**：实证得到3个核心结论：LVLM生成过程中对视觉输入的依赖度随生成步长逐步衰减、幻觉呈时间簇分布、生成早期干预可减少幻觉簇且不显著降低流畅度；在MMHalBench基准上，SAFE幻觉检测效果显著优于所有对比基线。
