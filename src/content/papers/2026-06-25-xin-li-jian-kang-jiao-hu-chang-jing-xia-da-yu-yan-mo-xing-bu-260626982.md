---
title: Auditing Framing-Sensitive Behavioral Instability in Large Language Models
  for Mental Health Interactions
title_zh: 心理健康交互场景下大语言模型框架敏感行为不稳定性审计
authors:
- Abla Bedoui
- Ashley L. Greene
- Mohammed Cherkaoui
affiliations:
- School of Computer Science, Digital Engineering and AI, Long Island University
- Department of Psychology, Long Island University
arxiv_id: '2606.26982'
url: https://arxiv.org/abs/2606.26982
pdf_url: https://arxiv.org/pdf/2606.26982
published: '2026-06-25'
collected: '2026-06-27'
category: Eval
direction: LLM可信评估 · 高敏感场景行为稳定性
tags:
- LLM
- Trustworthy AI
- Behavioral Stability
- Probing Analysis
- Activation Steering
one_liner: 通过层探测与激活引导实验揭示心理健康场景下LLM框架敏感行为的内部机制
practical_value: '- 高敏感场景（如电商客诉、售后对话Agent）可复用本研究的匹配prompt控制变量法，审计话术框架对LLM回复稳定性的影响

  - 层探测分析方法可直接迁移到业务LLM的内部表征排查，快速定位引发输出波动的Transformer层，针对性做对齐优化

  - 激活引导技术可用于业务场景的输出稳定性控制，通过干预框架相关表征方向减少回复偏差，提升用户信任度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM已广泛应用于心理健康等高敏感对话场景，语义相似但表述框架不同的输入易引发输出不稳定，损害交互可信性；过往研究多聚焦行为层面差异，缺乏对内部表征机制的解释。
### 方法关键点
构造多上下文框架条件的匹配控制prompt集，在多类指令微调LLM家族上开展实验，结合层-wise探测、跨框架泛化探测、激活引导三类方法分析框架敏感的内在规律。
### 关键结果数字
不同架构LLM均存在框架效应，会系统性改变回复倾向；行为相关信息在Transformer全层均可被解码，解码强度随架构差异变化；未知框架探测准确率始终高于随机水平，不受强词汇基线干扰；干预框架相关表征方向可部分调控下游输出行为。
