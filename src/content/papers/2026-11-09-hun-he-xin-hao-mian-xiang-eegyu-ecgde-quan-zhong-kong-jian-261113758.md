---
title: 'Mixed Signals: Weight-Space Programming for EEG and ECG'
title_zh: 混合信号：面向EEG与ECG的权重空间编程方法
authors:
- Dara Varam
- Taraneh Aminosharieh Najafi
- David Atienza
affiliations:
- École Polytechnique Fédérale de Lausanne (EPFL), Switzerland
arxiv_id: '2611.13758'
url: https://arxiv.org/abs/2611.13758
pdf_url: https://arxiv.org/pdf/2611.13758
published: '2026-11-09'
collected: '2026-11-14'
category: LLM
direction: LLM权重空间编程 小模型少样本优化
tags:
- Weight-Space-Programming
- LLM
- EEG
- ECG
- Edge-Deployment
- Few-Shot
one_liner: 验证权重空间编程适配EEG/ECG模型，少样本即可生成媲美梯度训练的小网络
practical_value: '- 边缘端小推荐/广告触发模型可借鉴WSP思路，用LLM直接生成权重，降低梯度训练的样本需求，适配低资源端侧场景

  - 线上小模型故障修复可尝试用LLM读权重定位问题，无需全量重训即可快速迭代bad case

  - 少样本场景的小模型快速验证可用WSP替代部分训练流程，缩短小模型从需求到上线的周期'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
传统神经网络依赖梯度下降训练，需大量标注样本；权重空间编程（WSP）此前仅在游戏、LLM、扩散模型场景验证效果，未覆盖小模型跨领域落地场景，亟需验证其通用性。
### 方法关键点
采用Claude Opus 5.5等前沿LLM，仅输入模型架构、任务定义、极少量训练受试者数据，无需梯度下降步骤，直接调试故障模型或从零生成生物信号分类模型的全量权重。
### 关键结果
- 仅用梯度训练1/6的样本量，LLM生成的模型效果即可与梯度训练模型持平
- 基于5个样本生成的EEG分类模型，效果优于传统手工特征pipeline（alpha波段功率、CSP+LDA）
- 局限性：无法优化已训练成熟的分类模型，无法仅通过权重反推任务，仅适配小网络场景
