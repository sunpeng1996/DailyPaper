---
title: 'Puro-2B: Poor Lab''s Qwen2-1.5B Trained on RTX 5090 within $5090'
title_zh: Puro-2B：基于RTX 5090的低成本2B参数大模型预训练方案，成本低于$5090
authors:
- Kairong Luo
- Jiarui Cui
- Yaorui Yin
- Shengqi Chen
- Yiming Yang
- Linxiang Gao
- Yanmohan Wang
- Mingzhe Zhang
- Kaiyue Wen
- Kaifeng Lyu
affiliations:
- Tsinghua University
- Pengcheng Laboratory
arxiv_id: '2608.27370'
url: https://arxiv.org/abs/2608.27370
pdf_url: https://arxiv.org/pdf/2608.27370
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: 大模型预训练 · 低成本训练方案
tags:
- Low-Cost LLM Training
- FP8 Mixed Precision
- RTX 5090
- MuonH Optimizer
- Curriculum Learning
one_liner: 开源低成本2B参数大模型预训练全流程，用消费级GPU实现接近Qwen2.5-1.5B的性能
practical_value: '- 训练电商/推荐域垂直小模型（如商品理解、Agent决策模型）时，可复用这套消费级GPU训练优化trick（驱动改P2P/GDR、通信感知并行策略），大幅降低训练成本

  - 预训练优化上可复用Blockwise FP8训练+MuonH超球优化组合，在精度损失可忽略的前提下提升训练吞吐量1.34倍，适配中小算力场景

  - 小算力团队训域内模型时可参考Curriculum Model Averaging策略，仅通过数据排序+ checkpoint平均就能提升1.65倍成本效率，无需额外加算力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型预训练成本居高不下，3B级小模型复现成本普遍超过70万美元，中小团队、学术机构难以负担；现有开源模型大多仅开放权重，完整可复现的预训练pipeline、全栈成本优化方案缺失，低成本预训练的落地路径存在明显空白。

### 方法关键点
- 硬件层：选用消费级RTX 5090 GPU，通过修改驱动开启PCIe P2P与GPUDirect RDMA，通信效率提升2.8倍，单位算力成本为H200的2.7倍
- 精度优化：采用Blockwise FP8混合精度训练，仅Transformer线性层用FP8计算，训练状态保留BF16/FP32，吞吐量提升1.36倍，精度损失可忽略
- 优化器：采用MuonH超球优化器约束参数范数，显式控制有效学习率，收敛效果优于普通Muon优化器
- 训练策略：两阶段预训练+课程模型平均（CMA），按数据源内质量分排序喂入数据，最后阶段固定学习率并平均6个checkpoint提升效果

### 关键结果
- 在15个数学、代码、推理基准上，$4.4K成本训出的Puro-2B平均得分55.14，超过Qwen2-1.5B；$6.9K版本得分接近Qwen2.5-1.5B，成本仅为同类开源模型的1/6以下
- 整套方案相比基线累计提升成本效率2.77倍，拟合的Puro成本缩放定律可直接预测不同预算下的模型性能

> 最值得记住的一句话：小团队可通过软硬件全栈协同优化，用消费级硬件以极低的成本训出媲美工业级的中小尺寸大模型，无需百万级算力预算。
