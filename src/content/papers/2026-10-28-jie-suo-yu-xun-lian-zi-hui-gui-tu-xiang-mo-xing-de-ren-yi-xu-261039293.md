---
title: Unlocking Any-Order Generation in Pretrained Autoregressive Image Models
title_zh: 解锁预训练自回归图像模型的任意顺序生成能力
authors:
- Rishav Pramanik
- Marco Pedersoli
- Zhaozheng Yin
affiliations:
- Stony Brook University
- International Laboratory on Learning Systems
- LIVIA, ÉTS Montréal
arxiv_id: '2610.39293'
url: https://arxiv.org/abs/2610.39293
pdf_url: https://arxiv.org/pdf/2610.39293
published: '2026-10-28'
collected: '2026-10-31'
category: Training
direction: AR模型微调 · 任意顺序生成能力解锁
tags:
- Autoregressive Model
- Positional Embedding
- Curriculum Learning
- Efficient Fine-tuning
- Image Generation
one_liner: 以极低额外计算成本将预训练固定顺序AR图像模型适配为任意顺序生成，兼容现有AR推理栈
practical_value: '- 电商图文生成场景可复用该微调方案改造现有预训练AR生成模型，仅需少量额外计算即可获得图像局部补绘/外延/编辑能力，无需从零训练

  - 生成式推荐等场景的固定顺序预训练序列模型（如Semantic ID序列生成模型），可借鉴future-aware positional embedding、ordering
  curriculum思路，低成本适配任意位置条件生成需求，满足推荐序列插品/补品等场景

  - 适配过程不破坏原有推理栈，可完全兼容KV cache、vLLM等现有推理优化方案，工程落地成本极低'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
固定栅格扫描顺序预训练的自回归（AR）图像生成模型无法支持推理阶段的图像补绘、外延、编辑操作，现有方案需从零混合顺序训练，计算成本达标准训练的3倍，且不兼容KV cache、vLLM等成熟AR推理生态。
### 方法关键点
仅对预训练AR模型做少量适配，核心含两个组件：1. future-aware positional embedding，以可忽略 overhead 解决目标位置可识别性问题；2. ordering curriculum，提供从预训练权重到任意顺序生成最优解的稳定优化路径，完全保留原有AR推理栈。
### 关键结果
在LlamaGen-L/XL、RAR-L/XL共4种不同架构/规模的基线模型上验证：ImageNet补绘任务FID达6.21，优于MaskGIT的10.44；外延任务性能与MAR-L相当；仅需在预训练基础上增加13-33%额外计算量，类条件生成FID仅上升1.2-1.9即可获得任意顺序生成灵活性。
