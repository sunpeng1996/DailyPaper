---
title: 'Mind What Matters for Reasoning: Aligning Cross-Modal Attention via Selective
  Probability Mass Concentration'
title_zh: 面向多模态推理优化：基于选择性概率质量集中的跨模态注意力对齐
authors:
- Jiaqi Deng
- Zonghan Wu
- Zhan Heng
- Xiaoshui Huang
- Huan Huo
- Guandong Xu
affiliations:
- University of Technology Sydney
- East China Normal University
- The University of New South Wales
- Shanghai Jiao Tong University
- The Education University of Hong Kong
arxiv_id: '2609.29940'
url: https://arxiv.org/abs/2609.29940
pdf_url: https://arxiv.org/pdf/2609.29940
published: '2026-09-24'
collected: '2026-09-25'
category: Training
direction: 多模态大模型 · 注意力优化
tags:
- MLLM
- Cross-Modal Attention
- Visual Grounding
- LoRA
- Hallucination Mitigation
one_liner: 提出sPMC训练框架，仅微调3%-15%注意力头即可提升多模态大模型推理性能并降低幻觉
practical_value: '- 多模态商品理解场景可复用自适应头选择策略，仅微调3%-15%跨模态注意力头即可降低MLLM微调成本，同时提升商品属性识别、图生文案准确率

  - 电商多模态检索/推荐的幻觉问题，可借鉴概率质量集中损失设计，用弱监督分割掩码引导注意力集中到商品核心区域，避免无关背景干扰，减少错误属性召回

  - Agent接入多模态能力时，可直接复用sPMC的LoRA微调范式，仅用少量标注数据即可提升视觉推理准确率，无需全量微调基座模型，适配业务快速迭代需求'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
当前多模态大模型（MLLM）在视觉推理任务中易出现幻觉、过度依赖语言先验，往往未充分利用任务相关的视觉证据就生成答案。现有方法要么在推理阶段调整注意力，无法从根本优化视觉信息利用效率；要么训练阶段全量正则化注意力头，易破坏模型原有能力，且优化效率低。
### 方法关键点
- 语义增强grounding掩码生成：用LLM从文本中提取带属性的可定位名词短语，结合SAM3生成弱监督分割掩码，过滤前景占比超过60%的过宽掩码，优先保证掩码召回率
- 自适应头选择：通过视觉参与度、空间对齐度两个指标，筛选出3%-15%对视觉grounding敏感的注意力头，仅对这部分头做正则化，保留其余头的原有功能
- sPMC损失设计：仅约束注意力在掩码区域的总概率质量，不要求逐token对齐，对掩码假阳性区域容忍度更高，最终总损失为LLM原生损失加λ权重的sPMC损失，配合LoRA实现高效微调
### 关键实验
基于Flickr30k、RLAIF-V 83k构造33.2万条图文掩码三元组训练，在6个多模态基准测试集上验证，相比基线模型平均零样本提升3%，最高提升11.3%，仅微调3%-15%的注意力头；2B参数的Qwen3-VL微调后在HallusionBench、MMVP基准上超过GPT-4V、Gemini 1.5 Pro等大模型。
### 核心结论
MLLM的视觉grounding能力仅由3%-15%的稀疏注意力头主导，针对性微调这部分头的效率和效果远优于全量注意力正则化。
