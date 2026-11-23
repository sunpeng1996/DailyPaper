---
title: 'Functional Depth Is Learned: Isolating the Computation That Layers Produce
  Only Together'
title_zh: 功能深度是习得的：Transformer层间联合计算的隔离与分析
authors:
- JaeSeong Kim
- KyungTae Lim
affiliations:
- Semyung University
- Korea Advanced Institute of Science & Technology (KAIST)
arxiv_id: '2611.27911'
url: https://arxiv.org/abs/2611.27911
pdf_url: https://arxiv.org/pdf/2611.27911
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 大语言模型 · 层间依赖分析
tags:
- Transformer
- Cross-layer Dependency
- Model Pruning
- Pretraining Dynamics
- Mechanistic Interpretability
one_liner: 提出层间联合计算的容斥分解方法，证实Transformer功能深度由预训练逐步构建
practical_value: '- 做业务侧LLM剪枝时，可使用本文的层间协同度指标替代单纯的CKA相似度筛选可剪层，尤其是垂直域微调的电商导购/生成式推荐小模型，剪枝后效果损失更小

  - 预训练/微调业务LLM时，可监控层间协同度的变化趋势，当协同度进入平台期即可提前停止训练，降低训练成本

  - 做LLM推理优化时，高协同度的连续层区间可做联合KV cache优化，低协同度层可做激活复用，降低搜索推荐场景下Query改写、推荐理由生成等任务的推理时延'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Transformer深度是公认的可靠性能缩放轴，但过往分析工具仅能检测单层或层对的特性，无法捕捉必须多层同时存在才能产生的联合计算，也不清楚架构层面的标称深度如何转化为模型实际的计算能力，预训练对层间依赖的构建机制长期不明确。

### 方法关键点
- 提出基于容斥原理的层集合联合计算分量（Connected Component）精确分解方法，通过Identity ablation隔离仅当指定层集合共同作用时才会产生的计算，排除所有子集可解释的低阶贡献
- 定义归一化协同度指标`bUT`，将联合计算分量的模长与层集合最后一层的实际更新量做归一，消除不同训练阶段层更新尺度变化的干扰
- 定义协同度变化比率`Rk`，对比预训练前后同阶协同度的相对变化

### 关键结果
实验基于Pythia、OLMo、Amber三个系列共7个公开预训练检查点，在WikiText-103上测试得到核心结论：
1. 所有35组模型-阶次组合的`Rk`均>1，6阶协同度相对初始化最高提升64.4倍，层间协同在预训练到2.1B tokens后开始显著增强
2. 删除联合计算分量带来的困惑度上升是删除同范数随机方向的1.1~404.5倍，Pythia-6.9B的3阶联合计算删除后困惑度上升达809倍，证实联合计算是模型的核心负载部分
3. 层表示相似度（CKA）与协同度负相关（相关系数-0.66~-0.19），但相似度无法替代协同度作为剪枝依据，在Amber-7B上相似度的剪枝排序相关性接近0，而协同度仍保持正相关

### 核心结论
架构深度只是提供了串行计算的可能性，功能深度是预训练过程中逐步构建的层间依赖所赋予的。
