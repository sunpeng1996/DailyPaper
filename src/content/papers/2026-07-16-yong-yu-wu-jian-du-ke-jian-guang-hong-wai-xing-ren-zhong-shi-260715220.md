---
title: Structural-Semantic Reciprocal Learning for Unsupervised Visible-Infrared Person
  Re-Identification
title_zh: 用于无监督可见光-红外行人重识别的结构语义互学习方法
authors:
- Moyao Tian
- Shijia Liu
- Yan Yang
- Xin Yuan
- Minshi Chen
- Wei Wang
- Xiao Wang
affiliations:
- 武汉科技大学计算机科学与技术学院
- 武汉科技大学湖北省智能信息处理与实时工业系统重点实验室
- 中国科学院沈阳自动化研究所机器人学与智能系统国家重点实验室
- 中国科学院大学
arxiv_id: '2607.15220'
url: https://arxiv.org/abs/2607.15220
pdf_url: https://arxiv.org/pdf/2607.15220
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 无监督跨模态行人重识别优化
tags:
- Cross-Modal Learning
- Unsupervised Learning
- Pseudo Label Calibration
- Person ReID
- Closed-loop Training
one_liner: 推出结构语义互学习框架，解决无监督可见光-红外行人重识别的模态鸿沟与伪标签噪声传播问题
practical_value: '- 无标注训练场景下，可复用闭环伪标签校准机制，每轮训练后重构语义原型过滤噪声，缓解伪标签错误传播问题

  - 跨模态匹配任务（如电商图文匹配、多模态召回）可借鉴细粒度结构解耦思路，提取局部特征作为空间锚点，补足全局表征的歧义性

  - 多任务学习场景可参考结构-语义互学习范式，让两个分支的学习结果互相约束，提升表征鲁棒性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
无监督可见光-红外行人重识别存在模态鸿沟大、缺少跨模态ID标注的问题，现有渐进式关联范式依赖歧义全局表征，且开环训练会导致伪标签噪声无限制传播。

### 方法关键点
1. 结构语义互学习(SSRL)框架将开环关联改造为自校正闭环系统
2. 配套细粒度结构解耦(FSD)模块，提取有判别性的身体局部基元作为空间锚点，补充全局轮廓缺失的空间一致结构细节
3. 闭环语义校准(CSC)机制每轮epoch重构共享语义原型反馈到训练循环，在下一轮聚类前过滤伪标签噪声
4. 结构和语义学习双向交互，提升跨模态表征鲁棒性

### 关键结果
在SYSU-MM01、RegDB数据集上性能优于现有SOTA无监督方法，在RegDB上超过部分有监督方法
