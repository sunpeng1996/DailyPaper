---
title: 'Adaptive FastOPD: Progress-Aware Rollout Horizon Expansion for Efficient On-Policy
  Distillation'
title_zh: 自适应FastOPD：进度感知的滚动窗口扩展实现高效在线策略蒸馏
authors:
- Qian Tan
- Huaifei Liang
- Xuanyu Zhu
- Lei Jiang
- Yuqiang Li
affiliations:
- University of Science and Technology of China
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
arxiv_id: '2607.29494'
url: https://arxiv.org/abs/2607.29494
pdf_url: https://arxiv.org/pdf/2607.29494
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: 大模型训练 · 在线策略蒸馏效率优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- Training Efficiency
- Large Language Model
- Adaptive Scheduling
one_liner: 通过进度感知的滚动窗口自适应扩展机制，在提升OPD效果的同时将训练时间降低49.1%-71.2%
practical_value: '- 做生成式推荐/Agent小模型蒸馏时，可复用本文进度感知扩展策略替代固定步长训练调度，无需调参即可同时降低训练时间、避免效果下降

  - 多信号相对基线评估的方法可迁移到所有自适应超参调整场景，比如微调LLM导购/文案生成模型时自动调整训练步长，无需手动设置全局固定阈值

  - 窗口利用率门控的设计可复用到批量生成场景（如商品文案、推荐话术批量生成），避免少量长序列拖慢整个batch生成速度，提升推理吞吐'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
在线策略蒸馏（OPD）是将大模型推理/决策能力迁移到小模型的主流后训练方法，但滚动生成的在线训练环节计算成本极高，少量长尾长序列会拖慢整个batch的训练进度。现有方案多采用固定窗口长度、固定步长扩展的调度策略，无法适配不同模型、不同训练阶段的学习进度，要么需要大量调参抵消适配成本，要么会损失最终模型效果。

### 方法关键点
- 从短滚动窗口启动训练，仅满足两个条件时才扩展窗口：当前边界区域的师生对齐进度已停滞、当前窗口被足够多的样本充分利用，避免无效计算。
- 设计4种互补的师生对齐信号（top-k重叠度、共享概率质量、共享候选惩罚、非共享候选惩罚），基于每个窗口阶段的初始基线做归一化，取最大值聚合后用EMA平滑检测训练停滞，无需人工设置全局绝对阈值。
- 新增窗口命中率、边界到达率两个利用率指标做扩展门控，避免仅少量长尾长序列触发窗口扩展、拖慢整体训练效率。

### 关键结果
在数学推理基准上测试两组师生模型对，对比原生OPD（7K/15K窗口）、固定步长FastOPD基线：
1. 效果均为最优：DeepSeek模型对平均得分56.1，Qwen3模型对平均得分20.1，均高于所有基线。
2. 效率大幅提升：相比OPD15K，训练时间降低49.1%（DeepSeek）到71.2%（Qwen3）；相比固定步长FastOPD，训练时间降低13.4%到47.3%。
3. 超参鲁棒性强：调整核心超参时效果波动远小于固定调度方案。

最值得记住的结论：基于训练实际进度的自适应调度，比人工预设的固定规则能拿到更优的训练效率-效果trade-off，且跨场景适配性更强。
