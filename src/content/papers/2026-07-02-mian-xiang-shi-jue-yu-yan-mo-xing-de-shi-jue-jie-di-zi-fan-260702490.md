---
title: Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement
  Learning
title_zh: 面向视觉语言模型的视觉接地自反思强化学习训练框架
authors:
- Liyan Tang
- Fangcong Yin
- Greg Durrett
affiliations:
- The University of Texas at Austin
- New York University
arxiv_id: '2607.02490'
url: https://arxiv.org/abs/2607.02490
pdf_url: https://arxiv.org/pdf/2607.02490
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: 多模态大模型 · 自反思训练优化
tags:
- LVLM
- Reinforcement Learning
- Self-Reflection
- Visual Grounding
- Distribution Shift
one_liner: 提出VRRL强化学习训练框架，提升LVLM分布偏移场景下视觉接地自反思纠错能力
practical_value: '- 多模态商品理解Agent可复用VRRL训练思路，优化商品图属性识别、图表类商品参数解读的纠错能力，提升小众品类、用户实拍非标图等分布外场景的准确率

  - 训练多模态搜索/推荐模型时，可引入随机mask中间推理轨迹+经验回放失败态的trick，降低模型对标注推理路径的依赖，提升泛化性

  - 电商客服多模态Agent处理用户实拍图咨询场景，可嵌入该自反思机制，减少视觉对齐偏差导致的错误回复，无需额外大量标注'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LVLM执行CoT多模态推理时，自反思阶段常忽略视觉输入，分布偏移场景下无法基于视觉证据修正错误，推理准确率下降显著。

### 方法关键点
核心框架VRRL为强化学习范式，包含两个核心设计：1）训练时随机mask推理轨迹前缀，强制模型学习从错误中间预测中恢复，而非仅关注生成正确初始推理；2）引入经验回放缓存的失败态roll-in，让模型暴露于多样错误场景，学习针对性纠错。

### 关键结果
在表格/图表视觉接地、空间导航基准任务上，分布外平均准确率相较标准RL、面向自反思的微调基线实现大幅提升，而通用预训练、常规微调模型在分布偏移场景下性能显著衰减。
