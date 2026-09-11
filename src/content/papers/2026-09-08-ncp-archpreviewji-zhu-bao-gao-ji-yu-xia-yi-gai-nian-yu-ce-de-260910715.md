---
title: 'NCP-ArchPreview Technical Report: Moving towards Latent Space Language Models
  through Next Concept Prediction'
title_zh: NCP-ArchPreview技术报告：基于下一概念预测的隐空间语言模型
authors:
- NCP Team
- Jiaqi Cao
- Chiyu Chen
- Shuang Cheng
- Xu Cheng
- Beiya Dai
- Yufan Feng
- Kewen Ge
- Ruijun Ge
- Jiayi Huang
affiliations:
- Shanghai AI Lab
- LUMIA Lab, Shanghai Jiao Tong University
arxiv_id: '2609.10715'
url: https://arxiv.org/abs/2609.10715
pdf_url: https://arxiv.org/pdf/2609.10715
published: '2026-09-08'
collected: '2026-09-11'
category: Training
direction: 大模型预训练 · 隐空间概念预测
tags:
- Latent Space LLM
- Next Concept Prediction
- Vector Quantization
- Pretraining Efficiency
- Speculative Decoding
one_liner: 结合NTP与NCP双目标训练隐空间大模型，训练效率、下游效果均优于同规模基线
practical_value: '- 做LLM4Rec/垂域大模型预训练可复用NTP+NCP双目标设计，仅用51.3%训练token即可达到同参数基线效果，大幅降低预训练成本；

  - 电商垂域适配可优先尝试仅更新VQ模块的方案，相比同参数量LoRA吞吐量提升50%、内存占用降低34%，同时显著减少领域适配的灾难性遗忘；

  - 推荐/Agent场景的大模型推理加速，可将预训练学到的概念表示注入speculative drafter，在几乎无开销的前提下提升4.17%的平均接受长度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统大模型仅基于Next Token Prediction（NTP）预训练，高层语义概念仅作为训练间接副产品习得，训练效率低；隐空间建模在CV领域已验证可大幅提升效率，但在大语言模型领域缺乏大规模落地的可行性验证。
### 方法关键点
- 架构拆分为3个模块：16层Token Encoder、8层Concept Module、16层Token Decoder，新增层级残差连接（IRC+CRC）实现跨模块、跨层级信息高效流通；
- 采用乘积量化VQ从Encoder隐状态自动构造离散概念词表，每4个连续token压缩为1个概念表征，大幅降低概念级建模的序列长度；
- 端到端联合优化3个损失：token级NTP损失、概念级Next Concept Prediction（NCP）损失、VQ码本拟合损失，兼顾标准token生成能力和概念级语义建模能力。
### 关键结果
在5.73T Dolma-3数据集上训练8.9B参数NCP模型，对比OLMo-3-7B基线：
- 仅消耗51.3%的训练token即达到基线最终预训练损失，收敛速度提升1.95倍，整体计算效率提升1.74倍；
- 下游任务宏观平均分高2.45，其中推理类任务GSM8K提升5.99分；
- 轻量适配仅需更新17M参数的VQ模块，相比同参数量LoRA吞吐量高50%、内存占用低34%；将概念表征注入DFlash2 speculative drafter，平均接受长度提升4.17%，额外参数开销仅0.04M。
### 核心结论
联合token级和概念级双目标预训练，是兼顾训练效率、下游效果、推理加速、轻量适配的下一代大模型可行架构方向
