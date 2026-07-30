---
title: 'Sharpness-Aware Minimization and Muon: Robustness under the Spectral Norm'
title_zh: 光谱范数约束下结合SAM与Muon的鲁棒优化算法
authors:
- Wenzhi Zhong
- Edward Milsom
- Michael Murray
affiliations:
- University of Bath, Department of Mathematical Sciences
- University of Bath, Department of Computer Science
arxiv_id: '2607.26001'
url: https://arxiv.org/abs/2607.26001
pdf_url: https://arxiv.org/pdf/2607.26001
published: '2026-07-28'
collected: '2026-07-30'
category: Training
direction: 大模型训练 · 优化器泛化改进
tags:
- SAM
- Muon
- Spectral Norm
- Optimization
- Generalization
- Model Training
one_liner: 提出基于分层光谱内扰动的SAM优化变体，搭配Muon外更新提升模型泛化性能
practical_value: '- 推荐/广告排序、召回模型训练时，可将原有SAM的欧氏内扰动替换为分层光谱范数扰动，适配MLP/Transformer的矩阵参数结构，降低离线到在线的效果diff

  - 训练Transformer类的排序/多模态推荐模型时，可尝试光谱内扰动+Muon外更新的组合，替代原有AdamW+普通SAM的训练策略，提升分布外样本预测准确率

  - 做Agent相关的LLM微调任务时，可引入该优化策略，提升模型在未见过的用户Query、业务场景下的决策鲁棒性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有SAM优化的扰动几何多基于欧氏范数，未适配神经网络隐层权重的矩阵结构，最优扰动几何选择缺乏明确实践指引，而已有研究验证矩阵感知优化器Muon可显著提升模型训练效果。
### 方法关键点
1. SAM内扰动阶段，针对矩阵形式的隐层参数引入分层光谱内扰动，贴合权重的矩阵结构特性
2. SAM外更新阶段支持搭配AdamW/SGDW或Muon优化器，其中光谱内步+Muon外步的组合性能最优
### 关键结果
在ImageNet-1K数据集上测试ViT-Small/16、ResNet-50两类模型，该组合在所有参评方法中取得最高验证精度，泛化性能显著优于传统SAM+SGD/AdamW的配置。
