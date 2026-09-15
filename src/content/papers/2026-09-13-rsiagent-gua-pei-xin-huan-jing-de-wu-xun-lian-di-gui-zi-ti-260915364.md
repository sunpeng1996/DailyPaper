---
title: 'RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments'
title_zh: RSIAgent：适配新环境的无训练递归自提升多智能体框架
authors:
- Sibo Zhu
- Shicheng Fan
- Xinyue Wang
- Wenyi Wu
- Kun Zhou
- Biwei Huang
affiliations:
- Aether AI
- University of California San Diego
- University of Illinois Chicago
arxiv_id: '2609.15364'
url: https://arxiv.org/abs/2609.15364
pdf_url: https://arxiv.org/pdf/2609.15364
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: 多智能体协作 · 无训练递归自提升
tags:
- Multi-Agent
- Recursive Self-Improvement
- Autonomous Exploration
- Memory Reuse
- Training-free
one_liner: 提出无需训练的多智能体自提升框架，开源模型经自主探索后性能超越GPT-6等前沿闭源模型
practical_value: '- 可直接复用三角色（课程/执行/验证）多智能体分工架构，搭建新场景（如新电商活动页、商家后台）自动化Agent冷启动方案，无需标注训练数据，靠自主探索沉淀环境知识

  - 先广后深的探索策略可迁移到推荐系统新类目/新场景冷启动：先并行探索全域反馈覆盖通用规则，再聚焦高潜力case挖掘边界约束，缩短冷启动周期

  - 执行与验证模块信息隔离的设计可复用在电商文案生成、自动化投放类Agent中，降低错误经验沉淀到记忆库的概率，提升结果可靠性

  - 冻结记忆直接复用的训练-free模式适配高隐私要求业务，如商家私域运营Agent，无需对外传输业务数据，本地探索即可完成环境适配'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有数字Agent适配新环境时，大多需要收集额外交互数据做微调，成本高且无法适配私有、高频迭代的业务场景；仅靠记忆成功轨迹的适配方式无法沉淀稳定的动作-条件-结果因果关系，性能提升瓶颈明显。

### 方法关键点
- 三角色多智能体协作框架：课程Agent基于已有记忆和探索结果生成练习任务，规划探索方向；执行Agent以代码为动作空间交互环境，根据验证结果更新记忆；验证Agent独立基于环境反馈校验执行结果，避免关联错误传导
- 先广后深两阶段探索：Broad Recursive Self-exploration 阶段并行探索多方向任务，快速覆盖环境通用规则、常见失败模式；Deep Recursive Self-exploration 阶段聚焦难例、隐藏约束、边界条件，迭代细化记忆
- 完全训练-free：全程不更新模型参数，探索完成后冻结记忆，下游任务直接复用即可获得性能提升

### 关键结果
在OSWorld-v2（82个离线任务）、Agent's Last Exam（67个近景任务）基准上，基于开源Kimi-K3、GLM-5.3搭建的RSIAgent，OSWorld-v2 partial score达78.98%，超过GPT-6 Astra 6.38个百分点；Agent's Last Exam partial score达84.82%，超过GPT-6 Astra 2.56个百分点，同时优于Claude Opus 5等前沿闭源模型；ablation实验显示宽+深两阶段探索组合比单阶段探索平均得分高9~18个百分点。

无需更新模型参数，高效的自主探索+可复用因果记忆沉淀机制，可以抹平甚至逆转开源大模型与前沿闭源大模型的能力差距。
