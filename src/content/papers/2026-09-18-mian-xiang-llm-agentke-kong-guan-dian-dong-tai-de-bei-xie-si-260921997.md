---
title: Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents
title_zh: 面向LLM Agent可控观点动态的贝叶斯信念层
authors:
- Hafsa Akbar
- Daniel Platnick
- Marjan Alirezaie
- Hossein Rahnama
affiliations:
- MIT Media Lab
- Flybits Labs
- Toronto Metropolitan University
arxiv_id: '2609.21997'
url: https://arxiv.org/abs/2609.21997
pdf_url: https://arxiv.org/pdf/2609.21997
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: LLM Agent 可控信念与群体观点动态
tags:
- LLM Agent
- Opinion Dynamics
- Bayesian Update
- Controllable Agent
- Multi-agent Simulation
one_liner: 为LLM Agent添加单参数可控的贝叶斯信念层，实现可解释可审计的群体观点演化
practical_value: '- 电商社交场景的多Agent仿真（如用户种草、舆情传播模拟）可复用该贝叶斯信念层架构，用单参数κ控制用户固执程度，避免仿真结果偏向LLM固有bias，更贴合真实用户行为

  - Agent信念与表达解耦的思路可迁移到导购Agent设计：将用户真实偏好存储在外部结构化状态，LLM仅负责自然语言生成/理解，避免LLM自带偏好偏移影响对话推荐准确性

  - 做Agent仿真审计时，可借鉴本文的generate-appraise双LLM链路校准方法，对每个LLM单独做温度缩放校准，降低自然语言转量化证据的误差'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent群体观点仿真的观点更新完全依赖LLM上下文隐式完成，存在两大核心痛点：一是群体容易收敛到LLM固有偏见，出现共识坍塌，仿真结果与真实社会偏差大；二是Agent观点更新不符合贝叶斯准则，校准性差，且无法手动控制个体对说服的接受度，无解释性与审计能力。

### 方法关键点
- BCA架构完全解耦Agent真实信念与语言表达：信念以Beta分布概率值存储在LLM外部，仅通过贝叶斯规则更新，LLM仅承担发言生成、输入发言量化两个功能
- 单参数κ控制个体固执程度，对应经典Friedkin-Johnsen（FJ）观点动态模型的先验强度，搭配固定0.7的遗忘因子，无额外复杂调参
- 双LLM链路设计：generator（温度0.9）根据当前信念生成自然语言发言；appraiser（温度0，提前做温度缩放校准）将其他Agent的发言转为[0,1]区间的量化证据，输入信念层完成更新

### 关键结果数字
实验基于20个Agent的全连接社群，覆盖gpt-5.4、Llama-4-Scout、claude-sonnet-4等4个主流LLM，仅需100条标注数据完成appraiser校准：
1. 预设κ参数经过完整自然语言往返后，秩恢复度Spearman系数达1.0，量级衰减不超过30%
2. 仅调整κ即可复现三类经典观点动态：共识（κ→0）、持续分歧（有限κ）、少数派影响（κ→∞），其中持续分歧的最终信念与FJ理论固定点R²达0.93~0.99
3. 信念层可直接审计到不同LLM的语言信道bias：如Llama-4会系统性偏向反面立场，GPT模型则会放大观点极端性

### 核心结论
将Agent的核心状态（信念、偏好）放在LLM外部用透明规则更新，LLM仅负责自然语言输入输出转换，是实现可控、可审计LLM Agent系统的低成本有效路径。
