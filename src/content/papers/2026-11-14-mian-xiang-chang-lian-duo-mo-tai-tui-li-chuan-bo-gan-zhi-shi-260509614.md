---
title: Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal
  Reasoning
title_zh: 面向长链多模态推理传播感知视觉留存的反射锚方法
authors:
- Xuan Gong
- Hanbo Huang
- Hao Zheng
- Yiran Zhang
- Wenbin Dai
- Weishu Zhao
- Shiyu Liang
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
arxiv_id: '2605.09614'
url: https://arxiv.org/abs/2605.09614
pdf_url: https://arxiv.org/pdf/2605.09614
published: '2026-11-14'
collected: '2026-11-17'
category: Reasoning
direction: 长链多模态推理 · 视觉信息留存优化
tags:
- Multimodal-Reasoning
- Chain-of-Thought
- LVLM
- Policy-Optimization
- Visual-Grounding
one_liner: 从信息论推导视觉干预增益下界，提出RAPO方法缓解LVLM长链推理的视觉遗忘问题
practical_value: '- 多模态商品导购Agent的长推理场景，可复用高熵token选点逻辑，在视觉敏感决策节点主动重注视觉特征，降低视觉遗忘导致的导购错误

  - 可借鉴信息论增益下界的评估思路，替代启发式规则选干预点，降低推理链路无效计算开销，适配高并发多模态推荐/搜索场景

  - RAPO的链掩码有限窗口KL代理目标可直接迁移到LVLM多模态推理微调阶段，无需全链路重训即可提升长序列推理的视觉依赖度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
长CoT提升LVLM推理能力的同时，存在生成过程中视觉信息消退的问题，现有视觉重注方法依赖启发式规则选择干预点，无理论支撑且视觉影响传播路径不明确。
### 方法关键点
从信息论视角推导单步干预的下游视觉增益下界，明确两个核心影响因子：本地分支空间（token熵）、下游视觉传播潜力（与移除视觉的参考序列的后缀散度）；基于GRPO提出RAPO方法，选择高熵反射锚点，优化链掩码有限窗口KL代理目标强化下游视觉依赖。
### 关键结果
在多个推理密集/通用域基准上，跨多个LVLM backbone均大幅优于强基线；机制分析显示反射锚点集中在视觉敏感决策点，RAPO可显著提升生成路径上的对比视觉依赖信号。
