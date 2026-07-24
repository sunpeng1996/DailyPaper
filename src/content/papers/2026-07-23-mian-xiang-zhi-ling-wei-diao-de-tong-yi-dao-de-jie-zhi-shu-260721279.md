---
title: A Unified Moral-Value Dataset for Instruction Tuning
title_zh: 面向指令微调的统一道德价值数据集
authors:
- Zhaohui Zeng
- Florian Mai
affiliations:
- RWTH Aachen
- University of Bonn
- Lamarr Institute for Machine Learning and Artificial Intelligence
arxiv_id: '2607.21279'
url: https://arxiv.org/abs/2607.21279
pdf_url: https://arxiv.org/pdf/2607.21279
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: LLM价值对齐 · 指令微调数据集构建
tags:
- Value Alignment
- Instruction Tuning
- Dataset Construction
- SFT
- Moral Value
one_liner: 整合三类公开道德数据集构建统一指令微调数据集，验证10%混合占比下价值对齐效果最优且通用能力无损失
practical_value: '- 做Agent/导购LLM价值观对齐时，可复用「少量垂直领域SFT数据混合大量通用指令数据」的配比策略，10%左右的垂直数据占比即可兼顾垂直能力和通用任务效果

  - 构建领域指令微调数据集时，可采用LLM自动生成指令-响应模板的自提示方法，大幅降低人工标注成本

  - 对齐评估环节可复用Value-Action Gap评估框架，结合vLLM结构化输出约束+批量推理，提升评估效率和准确性

  - 多源异构数据集融合时，可采用训练小模型补全缺失字段的方案，解决不同数据源标注体系不一致问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM价值对齐缺乏专用的指令微调数据集，现有通用指令微调数据集未覆盖道德价值场景，直接进行价值对齐训练容易导致通用任务能力下降，同时不同道德价值数据集标注体系不统一，难以直接用于SFT训练。

### 方法关键点
- 整合ETHICS、UNIMORAL、SOCIAL-CHEM-101三类公开道德价值数据集，训练ModernBERT作为数据生成器补全不同价值框架下的缺失标注，统一为{场景、价值框架、标签}格式
- 采用自提示方法调用LLM自动生成多样化指令-响应模板，转换为可直接用于SFT的指令微调数据集
- 训练时将价值数据集与通用Tulu-3 SFT数据集按不同比例混合，基于Value-Action Gap框架评估价值对齐效果，同时采用OLMES基准评估通用任务能力

### 关键结果数字
- NE（规范伦理）数据生成器整体F1达0.9093，MF（道德基础）数据生成器最优加权F1达0.5334，可有效补全缺失标注
- 混合10%价值数据集时，价值对齐F1达峰值0.8521，较纯通用数据提升0.36个千分点，通用任务平均得分维持在70.8-71.2区间，与纯通用数据训练无显著差异
- 价值数据占比超过10%后，价值对齐效果逐步下降，占比100%时模型无法输出符合要求的格式化结果

### 核心结论
小模型做领域对齐时，少量垂直数据混合大量通用指令数据即可在不损失通用能力的前提下提升垂直任务效果，过高的垂直数据占比反而会损害模型的指令遵循能力
