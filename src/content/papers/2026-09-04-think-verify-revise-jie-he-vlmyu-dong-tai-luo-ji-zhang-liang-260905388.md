---
title: 'Think-Verify-Revise: Neuro-Symbolic Visual Reasoning with Vision-Language
  Models and Dynamic Logic Tensor Networks'
title_zh: Think-Verify-Revise：结合VLM与动态逻辑张量网络的神经符号视觉推理框架
authors:
- Homayoun Afshari
- Pietro Basci
- Alessandro Russo
- Lia Morra
affiliations:
- Politecnico di Torino, Department of Control and Computer Engineering
arxiv_id: '2609.05388'
url: https://arxiv.org/abs/2609.05388
pdf_url: https://arxiv.org/pdf/2609.05388
published: '2026-09-04'
collected: '2026-09-08'
category: Reasoning
direction: 神经符号视觉推理 · 少样本规则自动归纳
tags:
- Neuro-Symbolic
- Visual Reasoning
- VLM
- Logic Induction
- Few-shot Learning
- D-LTN
one_liner: 提出思考-验证-修正闭环神经符号框架，融合VLM规则归纳与D-LTN可微验证，实现少样本高性能视觉推理
practical_value: '- 「思考-验证-修正」闭环架构可直接迁移到电商多模态内容审核Agent，用VLM生成审核规则+可微模块校验，大幅降低人工写规则成本，减少大模型幻觉

  - 少样本规则归纳范式可复用在推荐/广告合规校验模块，仅需少量违规样本即可快速生成适配不同地区/场景的管控规则，缩短新规则上线周期

  - 可微逻辑张量网络校验+反馈迭代的设计，可用于提升多模态推荐系统的语义一致性校验能力，比如直播间商品和讲解内容的匹配度校验'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
视觉推理任务需要同时完成视觉内容感知与形式化关系约束应用，纯神经方法难以处理逻辑约束，纯符号方法感知能力弱，现有VLM在少样本下的规则归纳准确性不足，无法满足推理需求。
### 方法关键点
1. 设计三阶段闭环神经符号框架：Think阶段VLM输入少量标注视觉样本，输出符合语法规范的一阶逻辑（FOL）候选规则；
2. Verify阶段运行时基于生成的规则自动构建D-LTN，基于CNN输出的视觉embedding完成可微规则校验；
3. Revise阶段将校验失败的结果作为反馈输入VLM，指导下一轮规则迭代优化。
### 关键结果
在ViSudo-PC基准的4个视觉域（MNIST、EMNIST等）测试，仅需3个训练样本作为上下文即可归纳有效数独约束规则，AUC指标持平或超越NeuPSL、LTN等现有方法。
