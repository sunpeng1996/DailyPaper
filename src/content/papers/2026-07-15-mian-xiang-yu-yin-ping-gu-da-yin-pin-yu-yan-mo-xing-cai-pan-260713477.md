---
title: Auditing Protocol-Level Shortcuts in Large Audio Language Model Judges for
  Speech Evaluation
title_zh: 面向语音评估大音频语言模型裁判的协议级捷径审计
authors:
- Joonyong Park
- David M. Chan
- Yuki Saito
- Hiroshi Saruwatari
affiliations:
- Graduate School of Information Science and Technology, The University of Tokyo
- Berkeley AI Research (BAIR), University of California, Berkeley
arxiv_id: '2607.13477'
url: https://arxiv.org/abs/2607.13477
pdf_url: https://arxiv.org/pdf/2607.13477
published: '2026-07-15'
collected: '2026-07-17'
category: Eval
direction: 大模型自动裁判 评估有效性验证
tags:
- LALM
- LLM-as-judge
- Evaluation Protocol
- Shortcut Probe
- Speech Evaluation
one_liner: 发现语音评估LALM裁判依赖协议级捷径，提出需为模型-协议对搭配专属捷径探针验证有效性
practical_value: '- 用LLM-as-judge做电商/推荐/广告生成内容A/B评估时，不能仅看与人工标注的整体一致性，需额外设计捷径探针验证模型真的关注评估对象而非协议自带辅助信息

  - 做pairwise A/B评估时，增加顺序反转测试，排查模型是否存在固定选前/选后的位置偏见，避免评估结果失真

  - 用结构化特征描述替代原始内容做评估时，需先验证特征标注正确性，错误标注会导致大模型裁判准确率骤降'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前大音频语言模型（LALM）被广泛用作语音评估自动裁判，但仅统计与人工评分的整体一致性，无法保证其判决真的基于音频内容，可能利用评估协议自带的标签、参考数据等走捷径。
### 方法关键点
针对3种主流LALM裁判部署协议：特征蓝图评估（用结构化声学特征文本替代音频）、参考条件评估、成对A/B比较，设计配套捷径审计方法，在6个LALM裁判、4种评估属性上开展测试。
### 关键结果数字
特征蓝图评估场景下，错误的专家标签会让5个裁判的情感识别准确率降至0.10及以下；拼接式A/B比较场景下，Qwen3-Omni-Thinking存在固定位置偏好，交换待评估对象顺序仍会选择同一位置；整体一致性指标会高估LALM裁判的有效性，必须对每个模型-协议对做配套的捷径探针验证。
