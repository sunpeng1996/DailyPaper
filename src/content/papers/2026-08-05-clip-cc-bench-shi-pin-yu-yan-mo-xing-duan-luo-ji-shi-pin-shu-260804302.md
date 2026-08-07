---
title: 'CLIP-CC-Bench: Evaluating Paragraph-Level Video Descriptions in Video-Language
  Models'
title_zh: CLIP-CC-Bench：视频语言模型段落级视频描述能力评估
authors:
- Mukhtiar Ali
- Harsh Dubey
- Sugam Mishra
- Chulwoo Pack
affiliations:
- South Dakota State University
arxiv_id: '2608.04302'
url: https://arxiv.org/abs/2608.04302
pdf_url: https://arxiv.org/pdf/2608.04302
published: '2026-08-05'
collected: '2026-08-07'
category: Eval
direction: 多模态生成 · 长视频描述评测
tags:
- VLM
- Evaluation Benchmark
- Embedding Ensemble
- Long-form Video
- Multimodal Generation
one_liner: 推出面向长视频段落级描述的评测基准CLIP-CC-Bench，含专家标注集与多Embedding融合评估框架
practical_value: '- 多Embedding集成评估思路可复用，电商生成商品短视频文案、直播片段总结时，用多个嵌入模型ensemble降低单模型评估偏差

  - 粗细粒度结合的语义匹配方法可迁移到商品长描述、直播切片生成效果校验，兼顾整体语义一致性与细节准确率

  - Borda排序聚合方案适合多指标下的生成内容质量排序，可用于短视频带货文案的多维度评分融合，更贴合业务综合评估需求'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有视频语言模型评测多聚焦短片段、单句子指标，无法有效衡量模型的长视频段落级描述生成能力，缺乏可靠的长程多模态生成评估方案。
### 方法关键点
1. 构建覆盖5小时电影内容的评测数据集，切分为90s片段，每段配对专家撰写的段落级参考描述
2. 采用5个SOTA LLM embedding模型集成，缓解单模型评估偏差
3. 配套粗粒度+细粒度双层语义匹配逻辑，结合Borda聚合实现多模型综合排序
### 关键结果
完成17个SOTA视频语言模型的能力排名，评测协议通过人工标注一致性与bootstrap稳定性验证，全套评估脚本与工具已开源。
