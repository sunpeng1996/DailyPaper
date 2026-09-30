---
title: 'SCOPD: Sparse-Context On-Policy Self-Distillation for Efficient Vision-Language
  Models'
title_zh: SCOPD：面向高效视觉语言模型的稀疏上下文在策略自蒸馏
authors:
- Ahmadreza Jeddi
- Enming Zhang
- Jasper Gerigk
- Hakki Karaimer
- Mozhgan Nasr Azadani
- Jiayun Luo
- Minh Ngoc Le
- Gholamali Aminian
- Hugo Buurmeijer
- Yongchao Chen
affiliations:
- University of Toronto
- Stanford University
- Vector Institute
- Tsinghua University
- NVIDIA
arxiv_id: '2609.34044'
url: https://arxiv.org/abs/2609.34044
pdf_url: https://arxiv.org/pdf/2609.34044
published: '2026-09-27'
collected: '2026-09-30'
category: Multimodal
direction: 多模态大模型 · 推理效率优化
tags:
- VLM
- Knowledge Distillation
- Token Pruning
- On-Policy Training
- Inference Efficiency
one_liner: 提出稀疏上下文在策略自蒸馏框架，大幅提升强视觉token剪枝下多模态大模型推理性能
practical_value: '- 多模态搜广推场景VLM提速方案：采用「视觉token剪枝+SCOPD轻量LoRA微调」，仅保留10%视觉token即可恢复92%+原模型性能，推理无额外开销，可直接落地到商品图文理解、搜图、直播内容理解等场景

  - 剪枝性能下降优化思路：无需只迭代剪枝策略，通过自蒸馏让模型适配稀疏表征、解决「表征-利用gap」，成本远低于重新训练大模型

  - 蒸馏效率优化trick：通过视觉敏感性筛选Top10%响应位置做蒸馏，计算量仅为全量蒸馏的1/10，效果反而更优，适合业务侧低成本快速微调

  - 跨模态迁移复用：图像上训练的稀疏表征适配能力可直接迁移到视频理解场景，无需额外视频数据微调，适配短视频推荐、直播内容审核等需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
推理型VLM处理图像/视频时会生成数百上千个视觉token，prefill阶段推理成本极高。现有无训练token剪枝方法在强压缩（如仅保留10%token）下性能暴跌，过往普遍归因于关键视觉信息丢失，但固定稀疏表征下的Pass@K实验显示，Pass@64远高于Pass@1，说明性能下降本质不是信息丢失，而是模型未学会可靠利用剩余稀疏表征，存在「表征-利用gap」。

### 方法关键点
- SCOPD框架：学生模型基于剪枝后的稀疏视觉表征生成推理轨迹，特权教师模型用全量视觉表征监督相同的在策略前缀，无需标注数据、修改模型架构或增加推理开销
- SCOPD+优化：通过增加1%视觉token的扰动计算JSD，筛选对视觉信息最敏感的前10%响应位置做蒸馏，仅对这部分位置反传梯度，进一步降低训练成本、提升效果

### 关键实验
在13个多模态图像基准上测试，基于Qwen2.5-VL-7B、VisionZip剪枝保留10%视觉token时，原生模型仅保留86.37%的未剪枝性能，SCOPD提升至90.49%，SCOPD+进一步提升至92.43%；方案兼容所有剪枝算子，跨Qwen2.5/3-VL架构均生效，图像训练的模型无需额外微调直接适配视频任务，10%token下视频基准性能恢复至未剪枝模型的96.6%。

### 核心结论
高效推理VLM的性能不仅取决于剪枝后保留了哪些视觉信息，更取决于模型能否可靠地学会利用剩余的稀疏表征。
