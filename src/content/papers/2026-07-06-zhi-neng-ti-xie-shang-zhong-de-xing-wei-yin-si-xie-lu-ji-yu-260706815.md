---
title: 'Behavioral Privacy Leakage in Agentic Negotiation: Formalizing and Mitigating
  Inference Attacks via Randomized Policies'
title_zh: 智能体协商中的行为隐私泄露：基于随机策略的推理攻击防御
authors:
- Barkha Rani
affiliations:
- Apple Inc.
arxiv_id: '2607.06815'
url: https://arxiv.org/abs/2607.06815
pdf_url: https://arxiv.org/pdf/2607.06815
published: '2026-07-06'
collected: '2026-07-21'
category: Agent
direction: 智能体协商 · 隐私防御
tags:
- Differential Privacy
- Negotiation Agent
- Privacy Leakage
- Inference Attack
- Stochastic Policy
one_liner: 提出带(ε, δ)差分隐私的自适应随机协商策略，降低对手推理准确率同时保障协商效用
practical_value: '- 电商议价类Agent（如大宗商品采购、二手交易协商Agent）可直接复用该差分隐私随机策略，避免用户底价/预算通过协商行为泄露

  - 对外交互类业务Agent（如广告投放议价、客服协商）可参考「行为侧信道隐私」思路，排查动态交互行为是否泄露用户或平台敏感信息

  - 可复用差分隐私+业务收敛性联合优化的框架，在增加隐私保护能力的同时避免核心业务指标受损'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有高风险场景（保险、采购等）协商Agent仅通过密码技术保护显式披露的约束值，无法防御对手从可观测协商动态（让步轨迹、响应时长、收敛模式等）推断用户隐私约束的行为侧信道攻击。
### 方法关键点
针对多轮协商协议设计自适应随机协商策略，同时满足三项约束：(ε, δ)差分隐私保障、报价序列几乎必然收敛（对手保留价允许时可达成一致）、高协商效用。
### 关键结果
在3000组合成双边协商测试中，该机制将对手推理准确率降低43%-50%，同时协商成功率与效用保持在90%以上，强隐私保障下无显著性能损失。
