---
title: 'LSF-SR: Latent Semantic Fusion for Sequential Recommendation via Flow-based
  Conditional Variational Autoencoders'
title_zh: LSF-SR：基于流条件变分自编码器的序列推荐隐语义融合方法
authors:
- Shih-Hong Chen
- Josh Jia-Ching Ying
- Vincent S. Tseng
affiliations:
- National Yang Ming Chiao Tung University
- National Chung Hsing University
arxiv_id: '2609.29815'
url: https://arxiv.org/abs/2609.29815
pdf_url: https://arxiv.org/pdf/2609.29815
published: '2026-09-24'
collected: '2026-09-27'
category: RecSys
direction: 序列推荐 · 协同与LLM语义融合
tags:
- Sequential Recommendation
- Normalizing Flows
- CVAE
- LLM
- Semantic Fusion
one_liner: 采用带归一化流的CVAE融合协同信号与LLM语义，提升序列推荐全场景效果
practical_value: '- 离线生成item级LLM语义描述并预计算语义embedding，完全避免推理阶段LLM调用开销，适配高吞吐电商推荐场景

  - 用带归一化流的CVAE做协同与语义信号的概率融合，相比传统拼接/门控确定性融合，在长尾/冷启动场景增益更显著

  - 训练时采用周期KL退火策略，可有效避免CVAE后验坍塌问题，平衡推荐精度与语义对齐效果

  - 长尾/冷启动占比高的业务可优先复用该方案，NDCG@20相对现有LLM增强推荐基线最高提升22.88%，投入产出比高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐方案存在两类核心问题：纯协同信号驱动的模型在数据稀疏、长尾/冷启动场景下表征质量差；引入LLM语义增强的方案普遍存在协同空间与语义空间分布不匹配问题，简单拼接/门控融合无法对齐异质信号，且用户级LLM推理会带来不可接受的延迟开销，难以落地到工业级高吞吐推荐场景。

### 方法关键点
1. 离线针对每个item用LLM生成结构化语义描述，通过预训练语义编码器得到语义embedding，仅需一次计算可重复调用，无推理侧开销
2. 设计带归一化流的CVAE融合模块，以LLM语义embedding为条件，将协同ID embedding映射到统一隐空间，自适应拟合非高斯联合分布，解决分布不匹配问题
3. 采用周期KL退火策略训练，动态调整语义正则权重，避免CVAE后验坍塌，端到端优化融合模块与Transformer序列推荐backbone

### 关键结果
在Amazon Beauty/Office/Sports/Toys、Yelp共5个公开基准数据集上，对比SASRec、SRA-CL等13个SOTA基线，Recall@20最高提升12.98%，NDCG@20最高提升14.13%；长尾item场景下NDCG@20相对最强LLM增强基线最高提升22.88%。

### 核心记忆点
异质信号融合不要局限于简单拼接，用概率建模方式对齐分布+离线预计算语义特征，可在不增加推理开销的前提下大幅提升稀疏/冷启动场景推荐效果。
