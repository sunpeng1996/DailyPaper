---
title: 'MentalThink: Shaping Thoughts in Mental SVG World'
title_zh: MentalThink：基于SVG的多模态大模型心智可视化推理范式
authors:
- Kangheng Lin
- Jisheng Yin
- Dingming Li
- En Yu
- Yana Wei
- Han Zhou
- Liang Zhao
- Hongyu Zhou
- Hongbo Peng
- Jianjian Sun
affiliations:
- 北京邮电大学网络与交换技术国家重点实验室
- 中国科学院大学
- StepFun
arxiv_id: '2607.03530'
url: https://arxiv.org/abs/2607.03530
pdf_url: https://arxiv.org/pdf/2607.03530
published: '2026-07-02'
collected: '2026-07-08'
category: Reasoning
direction: 多模态空间推理 · 心智可视化
tags:
- Multimodal LLM
- SVG Reasoning
- Mental Imagery
- SFT
- Reinforcement Learning
one_liner: 提出SVG驱动的视觉符号推理框架，让多模态大模型具备可校验的心智空间推理能力
practical_value: '- 电商3D场景导购Agent可借鉴「可执行中间表示+渲染校验」范式，用SVG/矢量图作为空间推理中间态，降低3D空间选品、布局推荐的幻觉

  - 多模态生成类任务可复用两阶段训练策略：先SFT对齐中间表示语法，再多轮RL强化迭代修正逻辑，提升输出稳定性

  - 推理链路的中间结果可验证设计思路，可迁移到广告创意生成、商品3D建模等需确定性输出的场景，降低审核成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态大模型的空间推理依赖隐式内部表征，缺乏可解释可校验的中间过程，难以复刻人类借助心智图像解决空间问题的能力，推理幻觉率高。

### 方法关键点
1. 核心为think-with-SVG pipeline，将可执行SVG代码作为多轮推理的中间视觉表示，通过「生成SVG-渲染校验-解释迭代」的闭环，外化空间假设，在约束几何空间内完成推理；
2. 采用两阶段训练框架：先通过SFT对齐SVG语法规范，再用多轮RL强化模型对中间视觉假设的迭代检验、修正与优化能力。

### 关键结果
在空间理解与推理基准上性能显著领先，VSIBench准确率达55.1%，MindCube准确率达76.0%，验证了可执行矢量图作为动态视角转换、视觉反思、组合场景构建的可校验视觉工作空间的有效性。
