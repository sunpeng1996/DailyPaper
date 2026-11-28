---
title: 'Make the Adversary Spend More: Stateful Deception as a Cost-Exchange Primitive
  for AI-Era Cyber Defense'
title_zh: 让攻击者付出更高成本：AI时代网络防御的有状态欺骗原语
authors:
- Alessandro Cantelli-Forti
- Isabella Marasco
- Hosam Alamleh
- Giada Boschi
- Michele Colajanni
affiliations:
- CNIT RaSS National Laboratory
- University of Bologna
- University of North Carolina Wilmington
- University of Parma
arxiv_id: '2611.34770'
url: https://arxiv.org/abs/2611.34770
pdf_url: https://arxiv.org/pdf/2611.34770
published: '2026-11-25'
collected: '2026-11-28'
category: Other
direction: AI网络防御 · 有状态欺骗成本优化
tags:
- LLM
- Cyber Defense
- Honeypot
- Cost Optimization
- Stateful System
one_liner: 提出攻击者专属持久状态的成本交换型网络欺骗方案，优化后防御成本降低63%
practical_value: '- 多会话交互场景可借鉴「状态与渲染分离」架构：会话状态独立存储，LLM仅承担输出渲染职责，避免LLM存会话状态带来的一致性问题和上下文开销，可复用在电商智能客服Agent、多轮对话式推荐等场景

  - LLM推理成本优化思路可直接复用：确定性层裁剪+prompt约束优化，可在类对话交互场景下降低约60%的单会话推理成本

  - 可借鉴DER指标设计思路，定义业务场景的投入产出比量化指标，比如推荐场景的算力消耗/GMV提升比、Agent场景的推理成本/转化提升比，指导系统迭代优先级'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
LLM普及大幅降低攻击者的入侵扫描、自适应攻击成本，传统蜜罐存在会话重置/多攻击者会话合并问题，防御端易陷入无限制算力投入的被动局面，现有网络欺骗的真实性、检出率等评估指标未对齐攻防成本交换的核心目标。
### 方法关键点
1. 核心原语采用攻击者专属持久状态：每个攻击者进入独立的、与其历史操作完全一致的虚拟环境，与其他攻击者完全隔离；2. 架构上做状态存储与LLM渲染分离，LLM仅作为受限的显式状态渲染器，不承担状态存储功能，降低大模型上下文开销；3. 量化定义欺骗交换率（DER）指标，衡量单位防御资源投入消耗的攻击者任务加权工作量；4. 基于Cowrie SSH蜜罐对接本地开源LLM实现原型，叠加确定性层优化、prompt优化降低推理成本。
### 关键结果
在5个开源权重模型上验证，相比纯LLM诱饵方案，优化后单会话防御成本降低约63%
