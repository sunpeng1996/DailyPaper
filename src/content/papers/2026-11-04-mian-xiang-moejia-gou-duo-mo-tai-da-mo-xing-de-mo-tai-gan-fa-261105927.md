---
title: Modality-Aware Expert Pruning for MoE-Based Multimodal Large Language Models
title_zh: 面向MoE架构多模态大模型的模态感知专家剪枝方法
authors:
- Donggeun Kim
affiliations:
- Nota Inc.
arxiv_id: '2611.05927'
url: https://arxiv.org/abs/2611.05927
pdf_url: https://arxiv.org/pdf/2611.05927
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM压缩 · MoE多模态大模型剪枝
tags:
- MoE
- Multimodal LLM
- Model Pruning
- Model Compression
- Inference Optimization
one_liner: 提出训练无需微调的模态感知专家剪枝框架MAEP，大幅降低MoE多模态大模型内存占用
practical_value: '- 业务中部署多模态LLM做商品理解、图文生成、直播内容审核时，可直接复用MAEP的免训练剪枝流程，50%剪枝率下可将原58GB的30B级MoE
  MLLM压缩至31GB，适配单张40G消费级GPU，大幅降低部署成本

  - MoE推荐系统的专家剪枝可复用模态拆分思路：将用户特征、物品特征对应为不同「模态」，分别计算专家对两类特征的重要性，非对称加权后全局排序剪枝，避免统一统计导致的核心信号损失

  - 多模态召回/商品内容理解场景可复用低注意力视觉token的筛选逻辑：过滤商品图中无意义的背景冗余信号，提升特征提取/模型压缩的跨数据集稳定性，仅需百级样本即可完成校准，落地成本极低

  - 针对垂直品类（如3C、服装）的定制化MLLM，可在通用校准集中加入30%左右的领域样本，无需微调即可提升领域任务性能10%+，无明显跨域负迁移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
MoE架构是当前多模态大模型（MLLM）扩容的主流方案，但专家参数占总模型规模的90%以上：30B级MoE MLLM的BF16权重达~58GB，其中54GB为专家参数，即使单token仅激活8/128个专家，所有专家仍需常驻内存，无法在单张40G GPU部署。现有专家剪枝方法统一统计所有token的重要性，忽略视觉与文本token对专家的需求差异，直接应用到MLLM会导致多模态性能骤降。

### 方法关键点
- 提出∆H（Delta-H Output）指标：计算移除单个专家、路由权重重分配后MoE层输出的L2变化，量化专家冗余度，仅需一次前向传播即可完成所有专家的重要性计算，无需梯度或微调
- 非对称模态信号设计：文本侧∆H作为保留信号（值越高专家越重要），视觉侧仅用文本到视觉注意力最低的2%视觉token计算∆H作为剪枝信号（值越高越可剪），后者跨数据集重要性排序稳定性达0.54，远高于全量视觉token的接近0
- 全局跨层剪枝：对每层∆H做log变换和z-score归一化后，按模态相关性加权合并双模态信号，所有层专家统一排序剪枝，避免固定每层剪枝比例的不合理性

### 关键结果
在InternVL3.5、Qwen3-VL、Gemma4三个主流MoE MLLM上测试，对比HC-SMoE、REAP基线：25%剪枝率下平均保留97%以上的多模态与文本性能；50%剪枝率下多模态性能比基线高2-6个百分点，BF16模型内存从~58GB降至~31GB，可直接塞入单张40G GPU。仅需100个校准样本即可达到接近1K样本的效果，加入30%领域校准样本可提升对应领域任务性能13.9个点。

**最值得记住的一句话**：多模态MoE剪枝不能采用统一的重要性规则，拆分模态的非对称剪枝信号能在大幅降低内存的同时最小化性能损失
