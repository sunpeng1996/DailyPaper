---
title: 'REGER: Modeling inter-item Relations with Semantic IDs for Generative Recommendation'
title_zh: REGER：基于语义ID建模商品间关联的生成式推荐框架
authors:
- Yuxi Huang
- Silin Zhou
- Chenhao Wang
- Zihan Li
- Gangming Guo
- Pei Ke
- Shen Gao
- Shuo Shang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2610.37584'
url: https://arxiv.org/abs/2610.37584
pdf_url: https://arxiv.org/pdf/2610.37584
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 商品间关联建模
tags:
- Generative Recommendation
- Semantic ID
- Knowledge Distillation
- Attention Mechanism
- Pre-training
one_liner: 通过语义预训练、结构化注意力、分层偏好蒸馏显式建模商品间关联，提升生成式推荐性能
practical_value: '- 预训练阶段可复用Generative Semantic Retrieval (GSR)任务，用商品语义embedding的TopK邻居构造预训练对，无需用户交互即可让模型提前学习商品间语义关联，缓解冷启动问题

  - 历史编码模块可直接复用Item Transition Structure Attention (ITSA)，仅修改注意力掩码无需新增参数，通过全局token注意力+按Semantic
  ID边界对齐的局部商品级注意力，同时捕获全局长期偏好和相邻交互的转移关系

  - 训练阶段可接入Hierarchical Collaborative Preference Distillation (HCPD)，把传统判别式推荐模型的偏好分布按Semantic
  ID前缀树分解蒸馏，仅在目标商品的真实前缀路径上计算KL损失，训练开销低，推理无额外成本，可稳定提升生成式推荐精度'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐（GR）通过自回归生成商品Semantic ID实现端到端推荐，但现有方案存在三大痛点：随机初始化的SID token embedding和从零训练的GR模型无法继承原生商品语义关联；交互历史打平为token序列后，注意力未显式对齐SID边界，无法捕获相邻商品的定向转移关系；仅用正样本交叉熵损失训练，未显式引入商品间协同偏好排序约束，效果上限低。

### 方法关键点
- 设计Generative Semantic Retrieval（GSR）预训练任务：输入单个商品的SID，要求模型生成其语义空间TopK邻居的SID，为后续推荐训练提供优质初始化
- 提出Item Transition Structure Attention（ITSA）：编码器每层混合两类注意力头，全局头对全历史token做双向注意力捕获长期偏好，局部头仅允许当前商品SID的token和前一个商品的SID token互注意力，无额外参数开销
- 提出Hierarchical Collaborative Preference Distillation（HCPD）：基于SID前缀树理论证明商品偏好分布可精确分解为各前缀下的条件分布，将判别式教师模型的全量偏好分布按真实目标SID的前缀路径分层蒸馏，与交叉熵联合优化

### 关键实验
在Amazon 2014的Beauty、Sports、Toys三个公开数据集上对比16个基线（含判别式、生成式、混合三类），REGER在所有生成式/混合基线上取得一致提升，在Beauty数据集Recall@5达0.0594，超过SOTA生成式基线ActionPiece 17.2%，超过强判别式基线DuoRec 2.4%；仅加入HCPD的TIGER基准模型Recall@5相对提升23%，训练仅增加10%左右耗时，推理无额外开销。

### 核心结论
生成式推荐的效果瓶颈不仅来自SID的编码质量，更来自模型是否能显式将商品间语义、协同关联融入预训练、编码、生成全流程。
