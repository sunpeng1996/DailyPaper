---
title: 'Recurrent Neural Networks Beyond Time: Learning from Multiple Ordered Projections'
title_zh: 超越时序场景的循环神经网络：多有序投影学习方法
authors:
- Vagan Terziyan
- Artur Terziian
- Oleksandra Vitko
affiliations:
- University of Jyväskylä
- Prague University of Economics and Business
- Kharkiv National University of Radio Electronics
arxiv_id: '2608.09690'
url: https://arxiv.org/abs/2608.09690
pdf_url: https://arxiv.org/pdf/2608.09690
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 序列模型 · 非时序结构化学习
tags:
- RNN
- Sequence Learning
- Multi-view Learning
- Representation Learning
- Structural Learning
one_liner: 提出基于多有序投影的SE-RNN框架，可挖掘非时序结构化数据中单序列无法捕捉的隐式依赖
practical_value: '- 电商用户行为、商品属性等非纯时序结构化数据，可构造多组合理排序投影（如用户行为除时间序外，还可按商品品类、客单价排序），通过多专家序列模型分别编码后融合，挖掘单排序遗漏的用户兴趣关联

  - 可直接复用「独立结构专家+后融合」的架构，不需要修改底层RNN/Transformer等序列模型的现有实现，可快速在召回、排序模块开展AB实验

  - 针对用户长期兴趣建模、隐式反馈挖掘等推荐场景，可将静态用户/商品结构化特征构造为多组有序序列输入，提升表征的丰富度和召回精度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
RNN被广泛用于序列学习但长期被绑定时序场景，而循环计算本质是处理任意有序序列，单一排序规则无法挖掘结构化数据中全部隐式依赖。

### 方法关键点
1. 提出有序结构依赖假设(OSDH)：同一观测集合的多种合法排序可暴露单种排序无法捕捉的互补结构依赖；
2. 提出独立结构专家原则(ISEP)：每种排序投影对应独立训练的序列模型，学到的表征再通过专用融合层整合；
3. 落地为SE-RNN架构，底层直接复用原生RNN作为投影专家，不修改原有循环计算逻辑，也可拓展到Transformer等其他序列模型。

### 关键结果
在3种不同结构复杂度的合成数据集上验证，存在隐式结构依赖时，SE-RNN性能稳定优于单排序基线，在简单数据集上也保持和基线相当的竞争力。
