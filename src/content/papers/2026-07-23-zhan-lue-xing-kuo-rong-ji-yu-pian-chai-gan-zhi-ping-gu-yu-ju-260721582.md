---
title: 'Scale Up Strategically: Learning Compositional Generalization via Bias-Aware
  Evaluation and Data Collection for Robotic Manipulation'
title_zh: 《战略性扩容：基于偏差感知评估与数据采集的机器人操纵组合泛化学习》
authors:
- Yu Qi
- Zhang Ye
- Xinyi Xu
- Yuxuan Lu
- Amitoj Sandhu
- Boce Hu
- Haojie Huang
- Jonathan Tremblay
- Lawson L. S. Wong
affiliations:
- Northeastern University
- NVIDIA
arxiv_id: '2607.21582'
url: https://arxiv.org/abs/2607.21582
pdf_url: https://arxiv.org/pdf/2607.21582
published: '2026-07-23'
collected: '2026-07-27'
category: Other
direction: 机器人操纵 · 组合泛化优化
tags:
- Compositional Generalization
- Bias Evaluation
- Data Collection
- Robotic Manipulation
- Sample Efficiency
one_liner: 提出指令因子偏差量化框架与偏差感知数据采集策略，提升机器人操纵模型泛化性与样本效率
practical_value: '- 可借鉴FDR/FDH偏差量化思路，针对推荐/LLM4Rec模型对用户特征、item属性的shortcut依赖做诊断，定位过拟合的特征维度

  - 可复用偏差感知数据分配策略，在训练样本预算有限时，向模型欠拟合的特征维度倾斜标注/采样资源，提升样本效率和OOD泛化性

  - 针对多语义因子的生成式推荐任务，可参考指令因子拆分方法，将生成目标拆解为可量化的独立语义组件，降低组合泛化难度'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
机器人操纵模型需具备组合泛化能力以适配多样指令，但预训练策略易走捷径过度依赖显著特征，未真正落地语义理解，现有方法无法定位具体失效的语义因子。
### 方法关键点
1. 将指令拆解为颜色、动词、物体、尺寸、空间属性等独立可复用的语义因子，定义指令因子偏差为微调策略过度依赖主导因子的倾向
2. 提出两个量化指标：**Factor Dominance Rate (FDR)** 刻画因子间两两偏差，**Factor Dominance Hierarchy (FDH)** 输出因子主导性全局排序
3. 基于诊断结果设计偏差感知数据采集策略，将固定数据预算向欠落地的因子倾斜
### 关键结果
- 6个基础策略上验证得到一致的因子主导排序：颜色≥物体≥空间≥动词≥尺寸，颜色占绝对主导，动词、尺寸落地程度最低
- 偏差感知数据采集策略仅用一半标注样本，在仿真和真实机器人环境下效果均优于基线，样本效率和泛化性显著提升
