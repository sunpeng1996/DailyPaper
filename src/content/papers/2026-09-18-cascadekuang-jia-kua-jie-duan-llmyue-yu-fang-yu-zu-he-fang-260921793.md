---
title: 'CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense
  Evaluation'
title_zh: CASCADE框架：跨阶段LLM越狱防御组合方案及标准化评估
authors:
- Jiale Luo
- Eric Han
affiliations:
- School of Computing, National University of Singapore
arxiv_id: '2609.21793'
url: https://arxiv.org/abs/2609.21793
pdf_url: https://arxiv.org/pdf/2609.21793
published: '2026-09-18'
collected: '2026-09-21'
category: LLM
direction: LLM安全 · 越狱防御体系设计
tags:
- LLM Safety
- Jailbreak Defense
- Defense Pipeline
- Evaluation Framework
- Black-box Attack
one_liner: 提出首个统一评估框架下的LLM跨阶段越狱防御组合方案，给出分层防御落地指导
practical_value: '- 电商LLM导购、Agent客服等场景可直接复用分层防御架构，采用输入预处理+输出校验的跨阶段组合方案，降低单点防御被绕过的风险

  - 内部防御效果评测可复用其标准化攻击成功率定义+受控query预算的评估范式，统一指标避免不同方案对比的碎片化问题

  - 优先测试跨阶段防御组合而非单一最优防御，可在满足合规要求的前提下，最小化对正常用户交互体验的负面影响'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM越狱防御分散在输入修改、输出守卫等不同pipeline阶段，缺乏跨阶段组合方案的系统评估逻辑；过往研究因攻击成功率（ASR）定义、实验设置不统一，评估结果碎片化，无法指导工业级防御体系落地。
### 方法关键点
1. 构建统一的直接黑盒单轮攻击威胁模型，标准化ASR计算规则，加入受控query预算、公平性评估约束，解决评估不一致问题；
2. 系统测试19种攻击、15种防御的单点防御与跨/同阶段组合效果，输出防御组合选择框架。
### 关键结果
无任何单一防御可覆盖所有攻击场景，最优跨阶段防御组合可实现安全性大幅提升，同时效用下降控制在可接受范围，可直接支撑分层防御落地。
