---
title: 'VFAD: Variational Semantic Prompting Meets Frequency-Adaptive Representation
  Learning for Zero-Shot Anomaly Detection'
title_zh: VFAD：结合变分语义提示与频率自适应表征的零样本异常检测
authors:
- Peng Chen
- Kaige Li
- Wei Wang
- Mingbo Yang
- Wenqiang Wang
- Li Shen
- Fangjun Huang
- Chao Huang
affiliations:
- School of Cyber Science and Technology, Sun Yat-sen University Shenzhen Campus
arxiv_id: '2607.29370'
url: https://arxiv.org/abs/2607.29370
pdf_url: https://arxiv.org/pdf/2607.29370
published: '2026-07-31'
collected: '2026-08-04'
category: Other
direction: 零样本异常检测 · 跨模态表征优化
tags:
- Zero-Shot Anomaly Detection
- CLIP
- Variational Prompting
- Frequency Decomposition
- Cross-Modal Alignment
one_liner: 提出融合变分语义提示与频率自适应表征的VFAD框架，提升零样本异常检测泛化性与细粒度定位能力
practical_value: '- 电商商品瑕疵检测、新类目违规内容零样本识别可直接复用VSPE模块，通过变分信息瓶颈过滤噪声、聚合细粒度异常语义，大幅降低新类目标注成本

  - 图像类商品推荐、内容审核场景可引入FARA的小波频率分解+分频率专家聚合方案，强化局部细微特征（如商品划痕、虚假宣传图细节）的判别能力

  - 跨模态检索/匹配任务可借鉴变分提示优化思路，替代传统固定prompt方案，提升跨模态对齐的精度与泛化性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有CLIP基零样本异常检测（ZSAD）依赖视觉-语言对齐实现泛化，但存在异常语义捕捉不全、局部细微变异识别不足的问题，无法适配无目标类目训练数据的工业、医疗等检测场景需求。

### 方法关键点
1. 设计Variational Semantic Prompt Extractor（VSPE），从密集patch token中自适应聚合异常相关局部语义，通过变分信息瓶颈正则化，融入细粒度视觉特征实现更精准的跨模态对齐；
2. 提出Frequency-Adaptive Representation Aggregation（FARA）模块，基于小波频率分解和分频率专家聚合，增强异常判别性视觉表征；
3. 联合优化语义引导与视觉表征学习，同时提升异常判别和细粒度定位能力。

### 关键结果
在13个工业、医疗基准数据集上，VFAD在各类异常场景下均优于现有SOTA ZSAD方法，代码将开源。
