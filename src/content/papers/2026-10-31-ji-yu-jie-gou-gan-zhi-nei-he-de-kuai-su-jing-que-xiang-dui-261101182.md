---
title: Fast and Exact Relative-Position Attention via Structure-Aware Kernels
title_zh: 基于结构感知内核的快速精确相对位置注意力计算框架
authors:
- Delyan Boychev
- Ivo Petrov
- Dimitar I. Dimitrov
affiliations:
- INSAIT, Sofia University "St. Kliment Ohridski"
arxiv_id: '2611.01182'
url: https://arxiv.org/abs/2611.01182
pdf_url: https://arxiv.org/pdf/2611.01182
published: '2026-10-31'
collected: '2026-11-03'
category: Training
direction: 大模型训练推理 · 注意力内核优化
tags:
- FlashAttention
- Relative Position Attention
- Triton
- Kernel Optimization
- Long Context
- Transformer
one_liner: 将相对位置注意力集成到类FlashAttention分块计算，长序列下零精度损失提速并降低显存占用
practical_value: '- 业务中使用DeBERTa/T5等带相对位置编码的模型做商品长文理解、用户长行为序列建模时，可直接替换该内核，无需修改权重，即可获得2~6倍前向加速、2~128倍显存降低，适配长序列召回排序的离线训练与在线推理场景

  - 做Agent长会话记忆、多轮对话理解时，若用到自定义相对位置编码的编码器，可复用offset感知分块、无原子梯度累加的思路优化自研注意力内核性能

  - 涉及语音模态的业务（如商品语音评论理解、语音搜索），替换Conformer的注意力内核后，长音频转录速度提升1.8倍、显存降低2.4倍，可显著降低部署成本

  - 若需自定义非RoPE位置编码提升长序列泛化性，无需为性能妥协替换为RoPE并重训模型，该内核可直接支持自定义相对位置机制的高效计算'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RoPE可无缝集成到FlashAttention，但长序列外推效果弱于可学习相对位置编码；而传统相对位置注意力需实例化N×N偏置矩阵，与融合注意力内核不兼容，显存、带宽开销随序列长度平方增长，从业者往往被迫替换为RoPE重训，成本极高。
### 方法关键点
- 统一四种主流相对位置注意力（Shaw、Transformer-XL、DeBERTa、T5）的加法公式，暴露可优化的共享结构
- 前向采用偏移感知分块：仅计算每个查询组可达偏移范围的投影，常数偏移块复用投影结果，避免冗余计算与内存访问
- 反向采用基于偏移的梯度分片累加：每个查询块对应一个线程块，片上完成梯度累加，完全消除原子竞争，保证数值确定性
- 基于Triton实现，为各类相对位置注意力提供drop-in替换方案，无需修改模型权重，适配Hugging Face、NeMo等主流框架
### 关键结果
- 8K序列下，前向速度较最强基线提升1.8~6.4倍，反向速度提升2.0~21倍；峰值显存前向降低2.9~128倍，反向降低1.4~54倍
- 端到端长语音转录任务（Parakeet-TDT-0.6B-v3）速度提升1.8倍、显存降低2.4倍；DeBERTa长文档分类4K序列下训练速度提升2.39倍，显存仅为基线的1/4
- 所有优化均为数值精确，与原生实现精度完全一致，无精度损失

> 最值得记住：不需要为了性能放弃效果更好的相对位置编码，该内核可零成本替换现有实现，无精度损失下获得数倍长序列性能提升
