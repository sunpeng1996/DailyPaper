---
title: 'BadWAM: When World-Action Models Dream Right but Act Wrong'
title_zh: BadWAM：世界动作模型想象正确但执行错误的漏洞研究
authors:
- Qi Li
- Xingyi Yang
- Xinchao Wang
affiliations:
- National University of Singapore
- The Hong Kong Polytechnic University
arxiv_id: '2607.15207'
url: https://arxiv.org/abs/2607.15207
pdf_url: https://arxiv.org/pdf/2607.15207
published: '2026-07-15'
collected: '2026-07-18'
category: Agent
direction: 具身Agent · 世界动作模型鲁棒性优化
tags:
- Adversarial Attack
- World-Action Model
- Embodied Agent
- Robustness
- Action-Imagination Alignment
one_liner: 提出BadWAM攻击框架，验证世界动作模型想象与执行对齐假设的脆弱性
practical_value: '- 搭建基于WAM的电商AR导购、实景选品等具身Agent时，不能仅校验想象未来的合理性，需额外增加动作与想象结果的对齐校验逻辑，避免被对抗样本误导

  - 涉及多模态输入的Agent决策系统，可参考本文攻击强度+隐蔽性的双维度划分，设计分层检测规则：先校验动作合理性，再匹配动作与想象结果的一致性

  - 线上部署WAM类架构前，可复用本文的两类攻击范式做鲁棒性测试，补充小幅度视觉扰动的训练数据，提升对抗防御能力'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
WAM作为具身控制的主流架构，业界普遍认为动作生成与未来世界预测的耦合特性可提升鲁棒性、可解释性，该假设的可靠性此前未被充分验证。

### 方法关键点
BadWAM统一框架定义世界动作漂移攻击，按攻击强度、隐蔽性两个维度划分两类攻击：1）仅动作攻击：直接诱导模型生成任务失败的动作；2）保留想象的攻击：诱导执行有害动作的同时，让模型预测的未来与无扰动场景的想象结果一致，实现隐蔽攻击。

### 关键结果数字
在多类WAM上的闭环执行测试显示，仅动作攻击可将任务成功率从96.5%降至43.1%；适度的未来保留正则化可在维持强攻击效果的同时，将想象漂移控制在较低水平，暴露WAM的独特漏洞。
