---
title: 'Not All Confusion Is Equal: A Source-Aware Uncertainty Diagnosis for Fine-Grained
  Aircraft Detection'
title_zh: 并非所有混淆等价：面向细粒度飞机检测的来源感知不确定性诊断
authors:
- Hai Huang
- Helmut Mayer
affiliations:
- Chair of Visual Computing, Universität der Bundeswehr München, Germany
arxiv_id: '2609.29959'
url: https://arxiv.org/abs/2609.29959
pdf_url: https://arxiv.org/pdf/2609.29959
published: '2026-09-24'
collected: '2026-09-27'
category: Other
direction: 细粒度目标检测 · 不确定性归因诊断
tags:
- Uncertainty Quantification
- Confusion Analysis
- Object Detection
- Aleatoric Uncertainty
- Epistemic Uncertainty
one_liner: 提出A²E²诊断工具，2×2维度拆解细粒度检测混淆来源，输出可落地的针对性优化方案
practical_value: '- 推荐/广告badcase分析可复用2×2混淆拆分思路，将预测错误按「固有不可控/模型可优化」×「类内/类间」维度拆解，避免盲目堆训练数据

  - 错误归因可参考输入特征相似度、输出预测分歧、参数偏差三个量化维度，替代纯人工经验判断，提升归因效率

  - 定位到错误来源后做定向干预：类内异构问题优先优化标注而非加数据，类别边界问题优先优化训练策略，提升优化投入ROI'
score: 5
source: arxiv-cs.CV
depth: abstract
---

### 动机
细粒度检测常用的混淆矩阵仅能呈现模型混淆的类别，无法定位混淆原因与可优化性，无法提供可落地的优化指导。
### 方法关键点
1. 沿「偶然不确定性/认知不确定性」×「类内/类间」两个轴构建2×2混淆来源分类体系
2. 从输入几何特征、输出空间分歧、偏置参数后验三个位置分别量化四个象限的混淆值，拆分逻辑基于构造而非经验相关性
3. 四类混淆分别对应：不可优化的类间相似、需重标注的类内异构、可优化的分类边界训练不足、需补数据的样本匮乏
### 关键结果
针对可优化混淆来源做定向干预，可精准降低对应问题的混淆占比，且不会改变不可优化的固有混淆
