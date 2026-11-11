---
title: A Technique to Model Product Information and User Reviews (MPIUR)
title_zh: MPIUR：融合商品多模态信息与用户评论的图推荐模型
authors:
- Emna Belguith
- Fajrian Yunus
- Talel Abdessalem
affiliations:
- Higher School of Communication of Tunis
- LTCI, Télécom Paris, IP Paris
arxiv_id: '2611.13361'
url: https://arxiv.org/abs/2611.13361
pdf_url: https://arxiv.org/pdf/2611.13361
published: '2026-11-09'
collected: '2026-11-11'
category: RecSys
direction: 多模态推荐 · 稀疏商品优化
tags:
- Multimodal Recommendation
- Graph Neural Network
- User Review
- Sparse Item
- Heterogeneous Graph
one_liner: 提出融合商品图文、用户评论的异构图推荐框架，显著提升稀疏商品推荐效果
practical_value: '- 可复用自适应加权的 collaborative-semantic 对齐损失，给交互少的商品更高权重锚定多模态语义信号，有效缓解长尾/稀疏商品推荐效果差的问题

  - 商品图文融合采用 per-item 注意力权重，可根据品类特性选择视觉编码器：乐器等非标品可尝试 VLM 生成图像描述，母婴等标品直接用 ResNet50
  特征效果更优

  - 可落地用户评论价值挖掘方案：用 LLM 提取评论的 (aspect, opinion, sentiment) 三元组作为异构图的边/节点特征，比直接用原始评论嵌入效果更好，同时可支持推荐结果可解释性

  - 多模态信号必须做对齐才能生效：可复用 InfoNCE 模态对齐损失 + 模态特征 BPR 损失的组合，避免新增模态反而引入噪声降效'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
电商推荐中协同过滤对交互稀疏的长尾商品效果极差，现有多模态推荐方法要么忽略用户评论，要么未将商品图文、用户评论三类原生模态纳入统一框架，且静态的协同-语义融合策略无法适配不同商品的交互密度，导致稀疏商品推荐效果难以提升。

### 方法关键点
- 模态预处理：用 Llama 3.1 从用户评论中提取 (aspect, opinion, sentiment) 结构化三元组；ResNet50、MiniLM 分别编码商品图像、文本描述，通过 per-item 自适应注意力融合图文表征，用 InfoNCE 损失对齐同商品的图文嵌入
- 双异构图架构：并行搭建两类异构图，协作图将评论嵌入作为用户-商品边特征做 GNN 消息传递，主题图关联三元组、属性维度、用户、商品节点建模细粒度用户偏好
- 自适应训练优化：以 BPR 为主排序损失，新增带商品交互度权重的模态间隙损失，给稀疏商品更高的多模态-协同表征对齐权重；同时加入模态表征直接参与排序的融合损失、三元组匹配的互信息损失

### 关键结果
在 Amazon Reviews 2023 乐器、母婴两个品类数据集上测试，对比 LightGCN、TGNN、BM3 三类基线：
- 全局 nDCG@10 分别达 0.2344、0.2194，均为最优
- 稀疏商品 nDCG@10 较 LightGCN 分别提升 105%、94%，较仅用评论的 TGNN 分别提升 2.5%、22.8%
- 仅在热门商品上效果略逊于仅用图文的 BM3

### 核心结论
多模态信号对推荐的增益核心不在模态数量多，而在于模态间、模态与协同信号的有效对齐，且语义信号对交互稀疏商品的增益远高于热门商品。
