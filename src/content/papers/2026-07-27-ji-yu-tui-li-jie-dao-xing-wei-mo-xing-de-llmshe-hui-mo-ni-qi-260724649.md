---
title: Reason-Mediated Behavioral Models for Auditing LLM Social Simulators
title_zh: 基于推理介导行为模型的LLM社会模拟器审计方法
authors:
- Atharva Pandey
- Gautam Jajoo
affiliations:
- Kairosity
arxiv_id: '2607.24649'
url: https://arxiv.org/abs/2607.24649
pdf_url: https://arxiv.org/pdf/2607.24649
published: '2026-07-27'
collected: '2026-07-29'
category: Eval
direction: LLM 社会模拟器可解释性评估
tags:
- LLM
- Evaluation
- Social Simulation
- Reason Alignment
- Audit
one_liner: 提出基于决策理由对齐的LLM社会模拟器审计框架，弥补仅结果匹配评估的不足
practical_value: '- 做新品概念测试、广告创意预调研等用户仿真任务时，不能仅校验LLM输出的最终偏好结果，需加决策理由与人类真实理由的对齐校验，避免逻辑错配导致业务判断失误

  - 可复用「带正负向标签的理由状态Z」设计，将用户开放评论/评价理由结构化后加入购意预测模型，可显著提升离线预测准度

  - 做Agent模拟用户行为的任务时，可引入理由对齐的审计逻辑，避免Agent生成看似合理但不符合真实用户决策路径的伪造行为'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前LLM作为社会模拟器（如合成调研受访者）的评估仅校验最终结果与人类的匹配度，无法识别「结果正确但决策理由完全错配」的问题，评估标准过松。

### 方法关键点
1. 基于94人防晒产品概念测试数据集，将用户开放决策理由映射为带正负向的理由状态Z（正向支持购买、负向阻碍购买）；
2. 提出审计范式：固定用户特征D、品类上下文K、产品概念X，分别校验人类理由对行为Y的预测增益，以及LLM在无人类理由/结果输入时生成的理由状态与真实Z的匹配度。

### 关键结果
- 人类推导的结构化理由可大幅提升购意预测的holdout效果；
- LLM模拟的理由脆性极强，多数案例仅复述产品概念信息，无法复现用户真实的接受/拒绝决策路径。
