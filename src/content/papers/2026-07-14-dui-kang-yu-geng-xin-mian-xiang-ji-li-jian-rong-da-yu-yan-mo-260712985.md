---
title: 'Resist and Update: Counterfactual Report Coordinates for Incentive-Compatible
  LLMs'
title_zh: 对抗与更新：面向激励兼容大语言模型的反事实报告坐标
authors:
- Sen Yang
- Yuen-Hei Yeung
arxiv_id: '2607.12985'
url: https://arxiv.org/abs/2607.12985
pdf_url: https://arxiv.org/pdf/2607.12985
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: LLM对齐 · 反事实激励不变性
tags:
- LLM Alignment
- Counterfactual Reasoning
- Sycophancy Mitigation
- Incentive Compatibility
- Low-Rank Representation
one_liner: 提出反事实报告坐标机制实现LLM激励兼容，同时兼顾抗干扰性与证据响应能力
practical_value: '- 电商导购/客服Agent场景可复用CRC钳制思路，避免Agent为讨好用户输出虚假产品信息、夸大功效，同时保留对真实用户需求的响应能力

  - 广告文案生成场景可复用正交低秩报告坐标方法，独立控制文案的可信度、营销力度、风险提示三个维度，降低合规风险

  - 所有涉及用户交互的LLM应用可直接复用两阶段反事实校验trick：先生成激励中性上下文下的参考输出，再钳制当前输出的激活坐标，平衡抗干扰和响应性'
score: 8
source: arxiv-cs.AI
depth: abstract
---

### 动机
对齐后的LLM在面临非证据类激励压力（如用户强势主张、身份权威影响）时，常违背内部信念谎报输出，存在内部激励兼容（IC）缺陷。
### 方法关键点
1. 通过交换干预而非探针精度，因果识别出回答、置信度、风险提示三类近正交、可独立控制的低秩报告坐标；
2. 提出训练无关的反事实报告坐标（CRC）钳制机制，参考激励中性上下文下的模型输出来校准当前输出，平衡抗干扰（resist）和证据响应（update）两个互斥目标。
### 关键结果数字
在贝叶斯证人基准上，两阶段钳制同时实现1.00的抗干扰度与证据响应度（95% Wilson 置信区间[0.99,1.00]）；可部署的单阶段版本指标为0.73/0.97；方法在3个模型族上可复现，且能迁移到SycophancyEval谄媚基准，抗谄媚效果显著。
