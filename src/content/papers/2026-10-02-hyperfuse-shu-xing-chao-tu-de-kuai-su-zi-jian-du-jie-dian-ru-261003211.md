---
title: 'HyperFuse: Fast Self-Supervised Node Embeddings for Attributed Hypergraphs'
title_zh: HyperFuse：属性超图的快速自监督节点嵌入方法
authors:
- Megha P
- Harshit Kumar
- Srajan Agarwal
- Anirban Banerjee
- Olaf Wolkenhauer
- Saptarshi Bej
affiliations:
- Indian Institute of Science Education and Research Thiruvananthapuram
- Indian Institute of Science Education and Research Kolkata
- University of Rostock
- Stellenbosch Institute for Advanced Study (STIAS)
arxiv_id: '2610.03211'
url: https://arxiv.org/abs/2610.03211
pdf_url: https://arxiv.org/pdf/2610.03211
published: '2026-10-02'
collected: '2026-10-05'
category: Other
direction: 超图表征学习 · 自监督节点嵌入
tags:
- Hypergraph
- Self-Supervised Learning
- Node Embedding
- Representation Learning
- Efficiency
one_liner: 提出无标注超图嵌入pipeline HyperFuse，效果不降前提下实现13-179倍基线提速
practical_value: '- 电商用户多跳交互/商品多属性关联的超图建模场景，可复用HyperFuse的线性复杂度结构坐标计算方法，大幅降低嵌入生成耗时

  - 动态演化超图（如实时用户行为网络）的嵌入更新场景，可借鉴其轻量编码器+少epoch训练范式，满足低延迟需求

  - 无监督多模态特征融合时，可参考其基于masking稳定性的超边权重分配策略，自动筛选有效关联边减少噪声干扰'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有自监督超图表征学习依赖深度编码器、需训练数百epoch，千级节点超图生成嵌入耗时可达数小时，无法适配多超图/动态演化超图的低延迟嵌入需求。

### 方法关键点
1. 采用无矩阵算子最大化超图模块化谱松弛度计算节点结构坐标，复杂度与节点-超边关联数线性相关
2. 基于特征/成员masking下的成员稳定性为超边分配有界效用权重，构建多尺度特征摘要
3. 采用不变性-去相关目标，训练轻量效用加权超图编码器仅100epoch

### 关键结果
在8个全方法跑通的公开数据集上，平均单数据集耗时仅8.7s，几何均值提速13-179倍；6个分类器中5个取得最高平均准确率，效果与SOTA无显著差异，较最快基线HypeBoy提速13倍的同时准确率提升2.1-4.1个百分点。
