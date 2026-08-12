---
title: 'TimeRoute: Time-Aware Modality Routing and Diffusion for Multi-Modal Recommendation'
title_zh: TimeRoute：面向多模态推荐的时间感知模态路由与扩散方法
authors:
- Pengyu Zhang
- Yangqin Jiang
- Klim Zaporojets
- Congfeng Cao
- Paul Groth
affiliations:
- University of Amsterdam
- University of Hong Kong
- Aarhus University
arxiv_id: '2608.10983'
url: https://arxiv.org/abs/2608.10983
pdf_url: https://arxiv.org/pdf/2608.10983
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: 多模态推荐 · 时序感知模态融合
tags:
- Multi-modal Recommendation
- Temporal Recommendation
- Diffusion Model
- Modality Fusion
- GNN
one_liner: 提出时序感知模态路由与时间条件扩散框架 解决多模态推荐的模态时效漂移问题
practical_value: '- 电商节日大促场景可复用时序模态路由逻辑：从用户近期交互的时间特征（活跃度、场景周期等）生成个性化多模态权重，替代全局固定融合比例，适配大促期间用户从看参数转向看包装/氛围感的决策变化

  - 可直接落地的轻量化trick：给多模态融合加0.05的权重下限，同时加「单用户熵低+批次平均熵高」的多样性正则，避免模态坍缩同时保证路由个性化，几乎无额外算力开销

  - 多模态召回/排序的过时信号抑制方案：复用FiLM调制的长短流双去噪头设计，给扩散/图重建模块加时间权重，优先拟合近期交互的分布，降低过时模态边的噪声传播，尤其适配内容/商品模态时效性强的短视频、服饰、礼品类赛道'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
多模态推荐普遍采用全局固定的模态融合权重，但不同模态的效用随时间漂移速率存在显著差异（例如日常购买巧克力用户关注成分文本，情人节则转向包装视觉、氛围音频），引发两个核心痛点：一是同一用户在不同时序场景下需要的模态比例不同，全局权重无法适配个性化时序需求；二是时效失效的模态会引入过时噪声，在图传播过程中被放大拖累推荐效果。

### 方法关键点
- 时序感知模态路由器：从用户交互时间戳提取16维时序特征（覆盖长短周期、活跃度、交互间隙等），通过2层MLP输出用户个性化模态融合权重，设置0.05权重下限避免模态坍缩，新增「单用户熵低+批次平均熵高」的多样性正则保证路由的用户级差异
- 时间条件扩散图重建器：通过FiLM调制对用户上下文做长短流双分支处理，分别拟合长期偏好和短期行为，新增时间重加权损失优先拟合近期交互，重建各模态用户-物品图时自动抑制过时边
- 三阶段训练流程：先训练扩散去噪器，再重建模态图，最后训练GCN排序模块，隔离对比损失对路由模块的梯度干扰，避免路由坍缩为全局固定权重

### 关键实验
在TikTok、Amazon-Baby、Amazon-Sports三个数据集上对比DiffMM等18个强基线，随机拆分下P@20最高提升9.8%，NDCG@20最高提升9.73%；按时间拆分的更贴近业务的场景下NDCG@20最高提升16.11%；不均衡模态噪声实验中性能优势进一步扩大。

**最值得记住的一句话**：多模态融合的权重不应该是全局固定的，用户的时序行为特征本身就是模态重要性的强信号，适配不同模态的时效漂移能带来稳定的推荐效果提升
