---
title: 'Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits
  And Steering Robustness'
title_zh: 超越浅层对齐：训练后方法如何塑造LLM拒绝回路与调控鲁棒性
authors:
- Hoang Cuong Nguyen
- Mark Dras
- Usman Naseem
affiliations:
- Macquarie University
arxiv_id: '2609.03887'
url: https://arxiv.org/abs/2609.03887
pdf_url: https://arxiv.org/pdf/2609.03887
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: LLM安全对齐 · 机制可解释性
tags:
- Safety Alignment
- Post-training
- Mechanistic Interpretability
- Refusal Circuit
- Steering Robustness
one_liner: 对比三类LLM安全对齐训练后方法的内部机制差异，提出安全对齐三元悖论
practical_value: '- 业务Agent安全对齐选型优先选Ra-SFT：其拒绝回路分散在MLP，比SFT的注意力头集中式架构抗jailbreak能力更强，过拒绝率比ORPO低最多30%，平衡安全与用户体验

  - 做LLM行为调控（如控制Agent生成合规营销文案）时，优先在拒绝识别层而非执行层做激活干预，Ra-SFT架构下可降低18.8pp的违规生成率，对通用能力影响不到2pp

  - 高风险业务场景不要依赖单一对齐方法：当前无方法同时满足分散拒绝编码、安全-能力分离、细粒度可修正三个要求，需叠加规则校验、外部审核等多重安全层'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM安全对齐仅做行为层面评估，大量jailbreak攻击事件证明浅层对齐不可靠，但不同训练后方法如何从内部机制层面塑造拒绝行为、影响抗攻击能力缺乏系统性对比，无法支撑高安全要求场景的对齐方案选型。

### 方法关键点
- 控制变量对比三类训练后方法：SFT（无偏好无推理监督）、Ra-SFT（带安全决策推理链监督、无偏好）、ORPO（带偏好信号、无推理监督），固定训练数据、超参数，在Llama-3.1-8B、Gemma-2-9B、Qwen3-8B三个不同架构模型上测试
- 从三个维度分析：拒绝向量的几何特征、激活补丁做回路因果分析、激活调控测试鲁棒性

### 关键结果
用WildJailbreak（2000条对抗有害prompt）、StrongREJECT（420条跨7类攻击）、XSTest（250条测过拒绝）、MMLU子集测通用能力：ORPO在Gemma-2-9B上StrongREJECT攻击成功率（ASR）达0%，但过拒绝率达31.6%；Ra-SFT比SFT在StrongREJECT上ASR降27.6pp，过拒绝率低16.8pp；Ra-SFT在识别层做激活调控可降18.8pp的WildJailbreak ASR，对MMLU准确率影响不到2pp。

当前所有离线对齐方法都无法同时满足分散拒绝编码、安全与通用能力分离、细粒度可修正三个目标，不存在一劳永逸的安全对齐方案。
