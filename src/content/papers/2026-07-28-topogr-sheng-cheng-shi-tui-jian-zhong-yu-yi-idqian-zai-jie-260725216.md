---
title: 'TopoGR: Revealing and Preserving Latent Structure of Semantic ID in Generative
  Recommendation'
title_zh: TopoGR：生成式推荐中语义ID潜在结构的揭示与保留
authors:
- Ziyu Zheng
- Zhengshun Du
- Yaming Yang
- Bin Tong
- Guan Wang
- Meng Yan
- Ziyu Guan
- Wei Zhao
affiliations:
- Xidian University
- Alibaba
- University of Science and Technology of China
arxiv_id: '2607.25216'
url: https://arxiv.org/abs/2607.25216
pdf_url: https://arxiv.org/pdf/2607.25216
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 语义ID拓扑结构保留
tags:
- GenRec
- Semantic ID
- Hamming Distance
- Vector Quantization
- Sequential Recommendation
one_liner: 提出拓扑感知生成式推荐框架，通过二进制语义ID保留空间结构，提升全场景推荐效果
practical_value: '- 语义ID量化阶段可复用BDQ设计，用二进制编码替换纯整数ID，既兼容现有生成式推荐流程，又能暴露Hamming拓扑，无需重构整体架构，落地成本低

  - 训练阶段可引入Hamming软目标替代硬交叉熵，对接近目标的语义ID给予更小惩罚，几乎无额外计算量即可提升语义相似物品的召回率，尤其适配长尾/冷启动场景

  - 推理阶段可在现有Top-P候选池上叠加Hamming一致性重排序，仅需预存每个item的二进制SID，计算与预测原型的相似度做加权，对线上 latency
  影响极小，可直接嵌入现有推荐链路的重排层

  - 冷启动/稀疏场景下，二进制SID的Hamming相似度可补充传统ID重叠匹配信号，解决语义相似但无共享ID的物品匹配问题，提升小众物品推荐效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐将ID视为独立离散符号，忽略量化阶段学到的ID空间拓扑结构，存在明显结构 mismatch：tokenizer学到的语义邻接关系在生成阶段被丢弃，仅靠精确ID重叠匹配无法识别语义相似但无共享ID的物品，严重限制推荐效果，尤其在长尾、冷启动场景下短板显著。

### 方法关键点
- 设计Bit-Decomposable Quantizer（BDQ），生成可双向转换的二进制语义ID（Binary SID）：每个整数SID对应固定r位二进制编码，自带可解释的Hamming几何属性，同时完全兼容现有生成式推荐的整数ID流程
- 输入层直接使用Binary SID扁平特征替代传统ID嵌入查表，天然保留不同ID间的Hamming邻近关系，无需额外学习语义关联
- 训练阶段引入Hamming软目标：基于二进制编码的Hamming距离给非目标ID分配梯度权重，距离目标越近惩罚越小，引导模型学习ID空间拓扑
- 推理阶段先并行预测得到Top-P候选池，再构建预测的二进制原型对候选做Hamming一致性重排序，修正仅靠精确ID匹配的打分偏差

### 关键结果
在Amazon 4个公开数据集（Beauty、Sports、Toys、CDs）上对比10+SOTA基线，相比并行生成式推荐SOTA RPG，Toys数据集N@5提升24%，Sports数据集N@5提升19%；冷启动场景下低频次物品推荐效果提升更显著；即使在整数ID完全无重叠的样本上，Hamming邻近的物品推荐NDCG是Hamming远离的3倍以上。

**核心记忆点**：语义ID的价值不止于离散索引，其量化过程中隐含的拓扑结构是生成式推荐可以低成本挖掘的重要增量信号。
