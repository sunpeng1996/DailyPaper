---
title: Test-Time Training for Modality Order Consistency in Vision-Language Models
title_zh: 面向视觉语言模型模态顺序一致性的测试时训练方法
authors:
- Aditi Gupta
- Yossi Gandelsman
affiliations:
- University of Chicago
- Reve
arxiv_id: '2607.20351'
url: https://arxiv.org/abs/2607.20351
pdf_url: https://arxiv.org/pdf/2607.20351
published: '2026-07-22'
collected: '2026-07-23'
category: Multimodal
direction: 多模态VLM 测试时鲁棒性优化
tags:
- VLM
- Test-Time Training
- Modality Consistency
- Multimodal
- Prompt Robustness
one_liner: 发现VLM模态输入顺序敏感缺陷，提出测试时训练方法消弭性能差并提升基准表现
practical_value: '- 部署多模态商品导购、商品理解类VLM时，优先采用「图片先于用户query」的prompt构造格式，无需改动模型即可获得6~26pp的准确率提升

  - 线上多模态模型遇到语义无关输入扰动导致的性能波动时，可复用本文的非对称测试时训练策略做自适应优化，无需全量重训即可修复问题

  - 多模态Agent的prompt鲁棒性优化可参考激活补丁定位故障层的思路，仅调整小范围中间层参数即可快速修复表征对齐问题，改造成本极低'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前主流VLM存在模态输入顺序敏感问题：相同任务下，仅交换prompt中图片与query的顺序（语义完全不变），就会出现显著性能差异，图片优先的prompt准确率比query优先高6~26pp，严重影响部署鲁棒性。
### 方法关键点
1. 提出非对称顺序一致性测试时训练方法，对齐不同模态顺序下的模型表征；
2. 通过激活补丁技术定位到模态顺序故障集中在网络中间窄范围层，针对性修复层间表征错位。
### 关键结果
1. 所有评测设置下基本消除模态顺序带来的性能差距；
2. 原效果更优的图片优先分支性能较基线进一步提升，实现双向对齐同时获得整体效果增益
