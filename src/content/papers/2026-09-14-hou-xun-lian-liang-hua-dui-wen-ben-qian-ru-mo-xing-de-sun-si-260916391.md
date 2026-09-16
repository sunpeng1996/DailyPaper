---
title: 'Where Post-Training Quantization Breaks Text Embedders: A Measured Map Across
  Four Embedder Families'
title_zh: 后训练量化对文本嵌入模型的损伤边界：四大架构家族的实测分析
authors:
- Hyojung Han
affiliations:
- ThakiCloud
arxiv_id: '2609.16391'
url: https://arxiv.org/abs/2609.16391
pdf_url: https://arxiv.org/pdf/2609.16391
published: '2026-09-14'
collected: '2026-09-16'
category: LLM
direction: LLM量化 · 文本嵌入模型压缩
tags:
- PTQ
- Text-Embedding
- Model-Compression
- Retrieval
- Quantization
one_liner: 实测四大嵌入架构的PTQ损伤边界，推翻传统混合精度量化的通用经验规则
practical_value: '- 电商/Agent的RAG向量检索场景可直接对通用嵌入模型做INT4/g16量化，NDCG损失小于1%，核心相关结果召回几乎不受影响，可大幅降低推理与存储成本

  - 混合精度量化的经验规则无法跨嵌入架构复用，INT3及更低位量化前必须针对目标嵌入模型做单模块敏感度实测，无需默认优先保护embedding table

  - 固定业务场景下，小模型蒸馏+温和量化的性价比远高于大模型极端低比特量化，相同精度下模型体积可缩小17倍，泛化性下降风险需结合业务范围评估

  - 量化效果评估不能仅依赖NDCG指标，需额外校验TopK相关文档的召回重叠率，避免出现NDCG无变化但核心相关结果被非相关结果替换的业务问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统生成式LLM的后训练量化（PTQ）经验（优先保护embedding table、按模块敏感度分配比特、用权重重建误差做敏感度代理）被直接套用在检索嵌入模型上，但嵌入模型的优化目标是TopK排序准确性而非生成困惑度，现有经验是否适用从未被系统验证，直接套用可能导致不必要的精度损失或资源浪费。
### 方法关键点
- 选取4大架构家族的5个公开嵌入checkpoint（Qwen3-Embedding-0.6B、其任务微调版本、EmbeddingGemma-300M、BGE-M3、E5-base-v2），覆盖编码器、解码器架构
- 网格遍历INT2/3/4/8、group size 16/32/128的权重量化配置，做单模块隔离量化测试敏感度，以对称量化为对照
- 在3个检索数据集（SciFact、NFCorpus、SkillRet）上评估，保留每查询粒度的得分，用NDCG@10、TopK召回重叠率等多维度衡量效果
### 关键结果
- INT4/g16量化对所有模型几乎无损，平均NDCG保留率98.7%~100.4%，仅13%~22%的Top10非相关结果被替换，相关文档重叠率达94.4%~97%
- INT3下模块敏感度出现明显架构依赖：Qwen系列FFN量化损失最高，BGE-M3、E5的注意力模块损失最高，模块损失不再可加
- INT2下架构差异被放大，相近权重重建误差下，NDCG保留率从1.3%到65.9%不等，embedding table量化对精度影响始终<3%，从未成为瓶颈
- 权重重建误差仅对整模型均匀量化有强预测性（r=0.8~0.92），对单模块敏感度的预测性极弱（INT4下r=-0.04），无法支撑混合精度比特分配

> 最值得记住的结论：针对检索嵌入模型的量化没有通用跨架构最优策略，优先保护embedding table的传统经验完全不成立，INT4/g16是当前几乎无业务损伤的通用最优量化配置。
