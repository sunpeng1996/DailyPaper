---
title: 'PolyFlow: Continuous Topology Embedding Flow Matching for Artist-style Mesh
  Generation'
title_zh: PolyFlow：面向艺术家风格网格生成的连续拓扑嵌入流匹配方法
authors:
- Chunshi Wang
- Haohan Weng
- Junliang Ye
- Biwen Lei
- Yang Li
- Zibo Zhao
- Zeqiang Lai
- Kaiyi Zhang
- Yunhan Yang
- Zhuo Chen
affiliations:
- ZJU
- Tencent
- THU
- CUHK
- HKUST
arxiv_id: '2606.30673'
url: https://arxiv.org/abs/2606.30673
pdf_url: https://arxiv.org/pdf/2606.30673
published: '2026-06-24'
collected: '2026-07-01'
category: Other
direction: 3D网格生成 · 连续流匹配
tags:
- Flow Matching
- Mesh Generation
- Transformer
- 3D Generation
- Continuous Embedding
one_liner: 提出离散拓扑连续嵌入的PolyFlow框架，实现并行高效的高质量艺术家风格3D网格生成
practical_value: '- 离散结构连续化嵌入的思路可迁移到商品SKU/多模态内容的连续表示学习，解决离散属性难以适配连续生成模型的问题

  - 并行流匹配生成替代自回归解码的架构设计，可参考用于生成式推荐的提速优化，降低大模型推理延迟

  - 显式控制输出维度（顶点数）的实现思路，可复用在推荐内容生成的可控性优化场景，比如按需调整推荐结果粒度'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
自回归Transformer生成高质量网格的延迟过高，而连续扩散/流匹配方法无法直接适配离散的网格连接结构，两类方案均存在明显缺陷。
## 方法关键点
1. 预训练轻量化拓扑嵌入器，将离散的网格顶点位置、法线、邻接信息映射为连续的逐顶点嵌入，可通过时空距离阈值还原原始离散拓扑
2. 冻结嵌入器后，构建基于Transformer的流匹配框架PolyFlow，基于点云特征实现全并行的顶点状态去噪
3. 推理阶段通过ODE求解器快速生成，支持直接指定顶点数精准控制输出网格分辨率
## 关键结果
在Toys4K基准上，Chamfer Distance、Hausdorff Distance两项指标均超过SOTA自回归基线，生成速度较自回归方案实现数量级提升。
