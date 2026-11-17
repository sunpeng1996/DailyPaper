---
title: 'CARE: Contrastive-Anchored Residual Encoding with Listwise Reconstruction
  for Retrieval-Oriented Semantic IDs'
title_zh: 面向生成式检索的语义ID构造：对比锚定残差编码与列表重建
authors:
- Yuan Xu
- Dawei Chen
- Xiaoguang Lin
- Xin Chen
- Yulong Ou
- Haijun Wu
affiliations:
- Tencent
arxiv_id: '2611.20721'
url: https://arxiv.org/abs/2611.20721
pdf_url: https://arxiv.org/pdf/2611.20721
published: '2026-11-16'
collected: '2026-11-17'
category: GenRec
direction: 生成式推荐 · Semantic ID 构造
tags:
- Semantic ID
- Generative Retrieval
- Contrastive Learning
- Knowledge Distillation
- Vector Quantization
one_liner: 提出两种面向检索的语义ID构造方法，工业视频搜索Recall@10较基线提升3.34个百分点
practical_value: '- Semantic ID构造可引入query-doc对比损失优化量化前的对齐空间，采用零初始化残差网络实现无缝对接原有量化基线，避免训练初期模型崩溃

  - 可复用列表式蒸馏思路：将原始embedding的query候选排序列表分布蒸馏到SID重建向量，无需修改SID顶层前缀，降低下游生成式检索模型的适配成本

  - SID效果可采用无GR模型的行预算召回协议快速评估，省掉反复训练生成模型的成本，大幅提升SID迭代效率

  - 业务落地优先优化上游检索预训练embedding质量，其对最终召回的影响远高于SID量化方案的选型，投入ROI更高'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Semantic ID构造方法（如残差k-means、RQ-VAE等）仅基于文档embedding优化几何失真、重建误差等指标，未考虑query-doc的检索相关性，量化损失可能落在检索依赖的特征方向上导致召回下降；且评估SID效果往往需要训练端到端生成式检索模型，迭代效率极低。

### 方法关键点
- **CARE-SID**：在量化前插入零初始化残差对齐网络，用query-doc对比损失优化对齐空间，同时加入锚定损失和原始embedding重建目标避免模型漂移，基于R3-VAE的评分残差量化分配SID码，保留纯文档编码接口
- **CARE-LR**：在CARE-SID基础上新增列表式蒸馏，将原始embedding输出的query候选列表相似度分布蒸馏到SID重建向量，采用函数保持的层解析重建头实现无缝初始化，固定一阶码本保证SID顶层前缀不变
- 提出无需GR模型的行预算召回评估协议，区分分桶质量和重建质量，可快速迭代SID tokenizer

### 关键实验
在腾讯工业视频搜索数据集上，对比基线RQ-KMeans，CARE-SID的重建视图Recall@10从62.75%提升到65.23%，CARE-LR进一步提升到66.09%，累计提升3.34个百分点；对比R3-VAE基线，CARE-LR的Recall@10提升0.94个百分点；对于未经过搜索数据训练的通用多模态embedding，CARE-SID的增益可达2.1个百分点。

### 核心结论
上游检索embedding的质量对Semantic ID召回效果的影响远高于量化方法的选型，优化上游embedding的投入ROI远高于调整SID构造方案。
