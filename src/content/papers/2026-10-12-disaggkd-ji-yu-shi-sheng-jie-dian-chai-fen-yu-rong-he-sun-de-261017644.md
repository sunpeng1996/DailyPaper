---
title: 'DisaggKD: Efficient Knowledge Distillation through Teacher-Student Disaggregation
  and a Fused Loss'
title_zh: DisaggKD：基于师生节点拆分与融合损失的高效知识蒸馏方法
authors:
- Ruixuan Tu
- Yuyang Dong
affiliations:
- The University of Tokyo
- RIKEN AIP
- SB Intuitions Corp.
arxiv_id: '2610.17644'
url: https://arxiv.org/abs/2610.17644
pdf_url: https://arxiv.org/pdf/2610.17644
published: '2026-10-12'
collected: '2026-10-20'
category: Training
direction: 大模型训练 · 知识蒸馏效率优化
tags:
- Knowledge_Distillation
- LLM_Training
- Fused_Kernel
- Distributed_Training
- Memory_Optimization
one_liner: 将知识蒸馏师生模型拆分部署到不同节点，结合融合损失降显存、提训练效率
practical_value: '- 电商/推荐域垂直小模型蒸馏时，若大尺寸教师模型与学生同卡部署显存不足，可复用师生节点拆分架构，教师单独跑前向仅传隐状态，无需在学生GPU放全量教师权重，大幅降低显存压力

  - 大词汇量（含推荐场景Semantic ID词表）的交叉熵/KD损失计算，可复用窗口化词表分片融合核，无需生成全词表logits，显存占用最高可降40x，精度无损失

  - 分布式训练前可参考论文的闭式显存与流量预估模型，提前计算不同并行度下的资源瓶颈，减少盲调OOM的试错成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有知识蒸馏（KD）框架默认将师生模型部署在相同GPU上，大模型场景下师生权重、梯度、优化器状态共同挤占显存，叠加全词表logits计算的额外开销，极易出现OOM，限制了可蒸馏的模型规模，也拖慢训练效率。

### 方法关键点
- 架构拆分：教师模型仅做前向推理，部署在独立节点集群，仅传输尺寸远小于logits的最后一层隐状态到学生节点，学生侧复用教师输出头计算logits，大幅降低跨节点传输量
- 融合损失：采用窗口化、词表分片的融合核计算KD损失，通过TP节点间MAX/SUM规约统计量替代全词表logits生成，数学上与全词表损失完全等价，无精度损失
- 资源管控：用预取环协调教师隐状态生产与学生训练的速度匹配，同时提供闭式显存与流量估算模型，可提前预判不同并行配置下的资源瓶颈

### 关键结果
在Qwen3.5-35B蒸馏到9B的任务上，3节点部署下传统同卡方案OOM，DisaggKD可正常训练，单GPU吞吐量达2352 tokens/s，比同条件下带融合损失的同卡方案快1.6%；4节点部署下比NVIDIA ModelOpt原生KD方案快34%，LM损失差异小于0.01，效果完全对齐。针对Nemotron 560B、Llama 405B等超大模型蒸馏任务，同卡方案均OOM，DisaggKD可正常训练。

### 核心结论
大模型知识蒸馏的显存瓶颈主要来自全词表logits生成与师生同卡部署，拆分部署+分片融合损失是性价比极高的优化方向。
