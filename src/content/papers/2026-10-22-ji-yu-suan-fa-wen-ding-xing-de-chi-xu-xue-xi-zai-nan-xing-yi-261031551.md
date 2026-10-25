---
title: Fine-Grained Analysis of Catastrophic Forgetting in Continual Learning via
  Algorithmic Stability
title_zh: 基于算法稳定性的持续学习灾难性遗忘细粒度分析
authors:
- Guodong Zheng
- Yan Sun
- Peng Wang
- Enneng Yang
- Jiafei Lyu
- Xiaochun Cao
- Dacheng Tao
- Li Shen
arxiv_id: '2610.31551'
url: https://arxiv.org/abs/2610.31551
pdf_url: https://arxiv.org/pdf/2610.31551
published: '2026-10-22'
collected: '2026-10-25'
category: Training
direction: 持续学习训练 · 灾难性遗忘分析
tags:
- Continual Learning
- Catastrophic Forgetting
- Algorithmic Stability
- SGD
- Learning Rate Scheduling
one_liner: 构建无预设模型架构的算法稳定性框架，拆解持续学习灾难性遗忘构成并推导上界
practical_value: '- 迭代更新推荐/Agent模型时，可参考论文拆解的遗忘构成，定位旧业务效果下滑的根因是泛化间隙还是经验遗忘

  - 多任务序列训练时，优先选择任务边界重启学习率衰减的调度策略，降低历史任务样本扰动的传播，缓解遗忘

  - 训练持续学习类推荐增量模型时，可根据推导的遗忘上界参数（训练集大小、单任务更新步数等）反向调优训练配置'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有灾难性遗忘的理论分析依赖特定模型/任务结构，无法解释SGD迭代优化过程对遗忘的影响，缺乏通用分析框架。

### 方法关键点
1. 构建无预设模型架构的算法稳定性分析框架，将预期群体遗忘拆解为任务内泛化间隙、跨任务泛化间隙、经验遗忘三部分
2. 跟踪单样本扰动在单任务内的更新影响及跨后续任务的传播路径，推导固定、任务内衰减、连续衰减三类学习率调度下的泛化间隙上界
3. 基于优化轨迹的累积梯度对齐度推导经验遗忘上界，无需凸性假设

### 关键结果
推导的遗忘上界可覆盖训练集大小、单任务更新步数、总任务数、学习率调度、累积梯度对齐度的影响，在Split CIFAR-100、Split MiniImageNet数据集上验证了理论结论有效性
