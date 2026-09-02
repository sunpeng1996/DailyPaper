---
title: 'EvoSCM: Scientific Belief Revision Through Causal Model Evolution and Experimentation'
title_zh: EvoSCM：基于因果模型演化与实验的科学信念修正框架
authors:
- Qing Zhao
- Haowei Li
- Weijian Deng
- Pengxu Wei
- Liang Lin
affiliations:
- Sun Yat-sen University
- Tsinghua Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2609.01526'
url: https://arxiv.org/abs/2609.01526
pdf_url: https://arxiv.org/pdf/2609.01526
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent认知进化 · 因果模型迭代
tags:
- Causal Inference
- SCM
- Agent Evolution
- Belief Revision
- Scientific Discovery
one_liner: 将结构因果模型SCM作为智能体显式认知状态，通过闭环迭代实现可迁移的科学信念修正
practical_value: '- 可将SCM作为推荐/广告系统的显式因果认知状态，替代隐式黑盒用户行为假设，基于新的用户交互数据迭代修正用户决策因果结构，提升跨品类/冷启动场景的泛化性

  - 可借鉴「假设种群+干预实验+差异修正+一致性校验」的闭环框架，用于业务策略迭代：维护多套候选策略，通过AB实验选择最大化区分度的流量分配，基于实验结果修正策略参数/结构，降低试错成本

  - 训练得到的因果模型可跨底座迁移，小模型可直接复用大模型产出的因果结构，降低业务场景的推理部署成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent的科学假设多为自由文本，信念隐式难以测试与修正，仅能优化推理流程，无法系统更新对外部世界的认知，导致出现预测与观测冲突时无法溯源错误、高效迭代认知，在需要因果推理的决策场景表现受限。

### 方法关键点
- 以SCM（结构因果模型）作为Agent的显式持久化认知状态，维护多套竞争SCM假设种群，避免过早收敛到错误解释
- 设计闭环演化流程：先基于现有证据反演隐变量状态，选择能最大化区分不同假设的干预实验，各假设生成可证伪预测后执行实验
- 基于预测与观测的差异提炼修正规则，支持增删因果边/隐变量、更新机制/参数四类编辑操作，再通过历史证据校验与结构一致性校验筛选有效假设进入下一轮迭代

### 关键实验结果
在DiscoverPhysics科学发现基准测试，对比不同底座原生推理基线：
- GPT-5.4底座下pass@1从1.86%提升至38.08%，收敛所需实验轮次减少29.7%；GPT-5.5底座下，机制解释得分从0.516提升至0.751，预测MSE降低2个数量级
- 演化得到的SCM可跨模型迁移，原本pass@k全为0的Qwen3.6，注入GPT-5.6-Sol演化的SCM后，pass@5达到63.64%，解释得分提升至0.74，媲美前沿大模型原生能力

### 核心结论
将显式因果结构作为智能体的可进化认知载体，比仅优化推理流程能带来更强的泛化性与跨底座迁移能力
