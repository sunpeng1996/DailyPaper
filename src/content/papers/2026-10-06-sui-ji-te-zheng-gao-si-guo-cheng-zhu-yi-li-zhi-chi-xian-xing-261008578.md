---
title: 'Random Feature Gaussian Process Attention: Linear-Time Probabilistic Attention
  with Calibrated Uncertainty'
title_zh: 随机特征高斯过程注意力：支持线性时间可校准不确定性的概率注意力模块
authors:
- Amir Mohammad Mahfoozi
- Zi Yang
- Ying Li
- Michael Minyi Zhang
affiliations:
- Sharif University of Technology
- The University of Hong Kong
arxiv_id: '2610.08578'
url: https://arxiv.org/abs/2610.08578
pdf_url: https://arxiv.org/pdf/2610.08578
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: LLM 概率注意力优化
tags:
- Gaussian Process
- Attention
- Uncertainty Quantification
- Random Fourier Features
- Transformer
- Long Sequence
one_liner: 提出即插即用的RFF-GPA概率注意力模块，实现线性时间、可校准不确定性的Transformer推理
practical_value: '- 可将RFF-GPA作为即插即用模块替换现有推荐/搜索场景Transformer的标准注意力，在长用户行为序列建模时实现线性复杂度，同时输出序列级不确定性用于低置信度召回结果兜底

  - 面向生成式推荐、RAG场景可复用RFF-GPA的token级不确定性输出，识别不可靠的生成token或检索片段，提升召回/生成结果可控性

  - 分布偏移场景（如大促用户行为变化、冷启动item）下，可复用RFF-GPA的校准优势，比MCD、温度缩放等方案获得更可靠的不确定性估计且不损失精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Transformer注意力无原理性的不确定性校准能力，预测容易过拟合，在高风险场景可靠性不足；基于高斯过程（GP）的概率注意力虽然能输出校准后的不确定性，但传统方案存在O(L³)的立方复杂度，即使改进的稀疏GP方案也只能降到O(L²)，无法适配长序列的搜索推荐、LLM推理场景，同时还存在精度下降的问题。

### 方法关键点
- 用随机傅里叶特征（RFF）近似GP注意力的平稳核，将核矩阵低秩分解为特征空间的乘积，通过Woodbury矩阵恒等式避免O(L³)的核矩阵求逆，将复杂度降到O(LM²)（M为固定的随机特征维度，和序列长度L无关），实现线性时间的后验均值和方差计算
- 提出RFF-CGP变种，通过共享潜层GP结构建模query和key的非对称交互，解决平稳核带来的query/key对称性约束问题，提升文本等非对称序列场景的表达能力
- 采用变分推断训练框架，仅需优化随机特征的谱分布参数和原Transformer参数，无需改动整体架构，可即插即用替换标准注意力

### 关键结果
在3个图像、3个文本分类数据集，以及CIFAR-10-C分布偏移数据集上对比MLE、MCD、SNGP、SGPA等基线：精度上RFF-GPA在CIFAR-10数据集上取得0.759的top-1精度，比SGPA基线提升9.4个百分点；校准性上ECE比标准MLE注意力平均降低20%~57%，在SVHN数据集上ECE仅为0.013；效率上序列长度L>500时，吞吐量比SGPA高10倍以上，随L增长保持线性扩展。

**最值得记住的一句话**：基于随机傅里叶特征的低秩核近似，可在几乎不损失精度的前提下，为Transformer提供兼具校准性和长序列扩展性的概率注意力能力。
