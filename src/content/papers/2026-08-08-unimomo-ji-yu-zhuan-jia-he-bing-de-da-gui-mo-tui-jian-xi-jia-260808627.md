---
title: 'UniMoMo: Expert Merging-Based MoE Acceleration for Large Recommendation Models'
title_zh: UniMoMo：基于专家合并的大规模推荐系统MoE模型加速框架
authors:
- Lei Xin
- Bin Gu
- Peize Li
- Zitong Wang
- Jianbo Zhao
- Changjiang Jiang
- Yanyue Xie
- Chao Huang
- Xuyang Zhao
- Zunhai Su
affiliations:
- Kuaishou Technology
- Hohai University
- Wuhan University
- ByteDance
- Alibaba Ant Group
arxiv_id: '2608.08627'
url: https://arxiv.org/abs/2608.08627
pdf_url: https://arxiv.org/pdf/2608.08627
published: '2026-08-08'
collected: '2026-08-12'
category: RecSys
direction: 推荐系统 · MoE训练后压缩加速
tags:
- MoE
- Model Compression
- Recommender System
- Expert Merging
- Inference Acceleration
one_liner: 通过功能相似性聚类+流量感知保护实现MoE推荐模型训练后压缩，无额外在线模块
practical_value: '- 部署阶段可直接复用该压缩框架，仅需少量无标注校准交互数据即可完成MoE压缩，不引入额外在线模块，完全兼容现有推理管线

  - 专家合并优先参考功能相似性（而非参数距离）的思路可复用，通过无标注数据计算专家输出分布的KL divergence衡量相似度，避免参数相似但功能差异大的错误合并

  - 高流量专家保护机制可直接迁移，通过路由熵计算流量集中度，动态设置保护专家比例，大幅降低合并带来的效果损失

  - SwiGLU专家合并时的最小二乘激活校正trick可复用，解决非线性层参数平均带来的激活偏移问题，仅需离线计算无推理开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工业级推荐系统广泛采用MoE结构扩容模型容量，但训练完成的MoE checkpoint仍保留全量专家库，路由、存储、推理开销高；现有MoE加速方案要么优化路由/执行逻辑不减少专家量，要么基于参数距离合并易造成效果下滑，无法在给定部署预算下无额外在线模块地压缩已有训练好的MoE推荐模型。

### 方法关键点
- 离线压缩阶段用无标注校准数据同时计算两类信息：一是所有专家在相同输入下的输出分布KL divergence，构建功能相似性亲和图；二是各专家的路由流量占比，计算层级路由熵动态确定高流量保护专家比例
- 采用带约束的图粗化算法合并专家：仅允许高流量专家最多合并1个低流量专家，优先合并功能相似度最高的合法专家对
- 合并后专家参数采用流量加权平均，针对SwiGLU非线性层加入最小二乘激活校正，将校正量直接融入权重无额外推理开销；压缩后模型仅需少量微调即可上线

### 关键实验
在Amazon Beauty、KuaiRec、TenRec三个公开推荐数据集，对比Origin MoE、MergeMoE等基线：8专家压缩为4专家时，NDCG@10保留原模型的99.92%~102.30%，A100上推理提速1.28×~1.63×；激进压缩为2专家+top1路由时，NDCG@10保留原模型的98.36%~104.24%，推理提速最高达2.21×。

### 核心结论
MoE推荐模型压缩的核心是识别功能冗余而非参数冗余，结合流量优先级的合并策略可以在几乎无损效果的前提下大幅降低部署成本。
