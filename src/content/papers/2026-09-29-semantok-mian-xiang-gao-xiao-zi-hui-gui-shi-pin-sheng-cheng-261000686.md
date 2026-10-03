---
title: 'SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation'
title_zh: SemanTok：面向高效自回归视频生成的可预测语义令牌
authors:
- Mikhail Dereviannykh
- Vikram Voleti
- Simon Donne
- Mallikarjun Byrasandra Ramalinga Reddy
- Shimon Vainer
- Mark Boss
affiliations:
- Stability AI
- Karlsruhe Institut für Technologie
arxiv_id: '2610.00686'
url: https://arxiv.org/abs/2610.00686
pdf_url: https://arxiv.org/pdf/2610.00686
published: '2026-09-29'
collected: '2026-10-03'
category: Multimodal
direction: 多模态生成 · 视频自回归分词器优化
tags:
- Tokenizer
- Autoregressive Generation
- Multimodal
- Video Generation
- Semantic Alignment
one_liner: 提出SemanTok灵活视频tokenizer，通过冻结DINO特征与轻量重建头实现小参数AR模型高语义对齐视频生成
practical_value: '- 电商短视频素材生成场景可复用SemanTok粗到细Token设计，用短前缀Token快速生成语义匹配的低分辨率初稿，大幅降低推理成本

  - 多模态推荐的跨域特征对齐场景可借鉴「冻结预训练大模型特征+各层前缀加轻量重建头」的训练方法，提升OOD场景语义一致性

  - 生成式推荐AR推理链路优化中，可参考优化Tokenizer而非盲目扩参的思路，用小参数模型匹配大模型效果降低部署成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有自回归视频生成框架的灵活分词器仅对解码器早期隐层加REPA对齐损失，解码器易从带噪输入凑出目标，导致语义对齐差、小参数模型生成质量低，OOD场景泛化性不足。
### 方法关键点
1. 编码器侧输入冻结DINO预训练语义特征，保证基础语义质量
2. 为每个保留的Token前缀加独立轻量重建头，强制各阶段前缀都能独立重建全局语义特征，实现粗Token承载全局语义、细Token补充像素细节的分层结构
### 关键结果数字
- 201M参数的SemanTok AR模型效果匹配甚至优于3.4倍参数规模的VideoFlexTok AR模型
- 各噪声级下解码器语义对齐度均优于基线，OOD类别场景下仍能保持高语义一致性
- 短Token前缀预测成本更低、生成保真度更高
