---
title: Your Transformer Is Secretly Elastic
title_zh: 无需重训的Transformer弹性化方法：支持推理时动态适配计算预算
authors:
- Walter Simoncini
- Dheeraj Varghese
- Gertjan J. Burghouts
- Cees G. M. Snoek
affiliations:
- University of Amsterdam
- TNO, Intelligent Imaging
arxiv_id: '2610.20588'
url: https://arxiv.org/abs/2610.20588
pdf_url: https://arxiv.org/pdf/2610.20588
published: '2026-10-14'
collected: '2026-10-15'
category: LLM
direction: Transformer推理优化 · 无重训结构化剪枝
tags:
- structured_pruning
- elastic_inference
- transformer_optimization
- post_training
- inference_acceleration
one_liner: 提出无需重训的可微软剪枝方法，将预训练Transformer转为支持任意推理预算的弹性模型
practical_value: '- 电商搜索/推荐的召回侧文本/多模态编码器可直接复用该方法做弹性化，流量高峰时剪枝到60%稀疏度仅损失个位数精度，无需重建向量索引，大幅降低峰值算力成本

  - 业务上有动态流量波动的LLM服务（如商品文案生成、Agent客服）可复用该可微软剪枝方案，无需重训即可生成多档位弹性模型，切换成本仅0.46ms，A100上单卡最高获得1.8×吞吐量提升

  - 可复用「跨多稀疏度目标联合优化单元重要性排序」的思路，替代现有单目标剪枝方案，无需为每个算力档位单独存储模型，综合精度比单目标优化最高高3.6%'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
预训练Transformer通常仅提供S/M/L等固定尺寸，部署时面对波动业务流量，要么高峰算力不足延迟上涨，要么低峰算力浪费；现有剪枝方法只能生成固定稀疏度模型，多档位需要存储多份模型，且大多需要重训/微调，成本极高，难以落地到百亿级参数模型。

### 方法关键点
- 初始化：用经验Fisher对角近似计算每个MLP神经元、注意力头的初始重要性得分，对数转换后按类型做中位数中心化，统一不同单元的得分基准
- 可微软剪枝：对14个稀疏度目标（5%~70%步长5%）分别生成sigmoid软掩码，用多目标平均损失优化每个单元的重要性得分，全程冻结预训练权重，仅更新得分参数
- 推理：优化后的全局重要性排序可直接硬剪枝到任意稀疏度，无需额外调整权重，支持推理时动态切换算力档位

### 关键结果
覆盖27个22M~8B参数量的视觉/文本Transformer，60%稀疏度下精度显著优于所有one-shot剪枝基线；DINOv3 ViT-H+/16 50%稀疏度下仅损失0.8%ImageNet线性探测精度，减少427M参数；AugReg ViT-B/16 60%稀疏度在A100上获得1.8×吞吐量、1.26×单query延迟降低，档位切换开销仅0.46ms；剪枝后的查询编码器和全量模型生成的向量索引兼容，无需重建索引。

最值得记住的结论：预训练Transformer本身的冗余度远高于过往认知，无需重训仅优化单元重要性排序即可实现高稀疏度下的精度保留，支持弹性推理降本
