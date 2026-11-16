---
title: 'G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving
  Demands'
title_zh: G-CAST：面向需求演进场景的电商Agent受管控持续自训练系统
authors:
- Yuechun Yu
- Wenzheng Kong
- Xiaofeng Mao
- Jin Zhang
affiliations:
- Alibaba Group
arxiv_id: '2611.17814'
url: https://arxiv.org/abs/2611.17814
pdf_url: https://arxiv.org/pdf/2611.17814
published: '2026-11-12'
collected: '2026-11-16'
category: Agent
direction: 电商Agent · 持续自训练 · 能力演进适配
tags:
- E-commerce Agent
- Continual Learning
- Self-Training
- Reward Modeling
- LLM Agent
one_liner: 提出受管控持续自训练框架，解决电商Agent需求漂移与能力演进时的适配与旧能力遗忘问题
practical_value: '- 数据编排可复用 reward 路由 + 熵优先级策略：全失败带标注 query 进 SFT 池，混合结果进 RL 池，全成功进回归监控池，再按
  token 级熵排序优先选高不确定性样本，大幅提升训练样本利用率

  - 持续迭代场景必须做受管控 checkpoint 切换：每次模型更新必须同时过新任务评测 + 全历史能力回归评测，避免旧能力遗忘，上线前验证门槛可直接拦截坏版本

  - Reward 无需一次性做完美，可随能力契约迭代更新：每次新增工具/流程后先审计当前 reward 错判 case，更新后过目标case验证、历史回归、重打分、轨迹回放四道门槛再上线，人力成本远低于全量
  reward 一次性开发

  - 大流量Agent场景可复用多rollout生成策略：每个query生成8个rollout，既可判断模型不确定性，也能快速发现reward错判问题'
score: 10
source: huggingface-daily
depth: full_pdf
---

### 动机
电商 LLM Agent 上线后持续面临需求漂移（新品类、新采购场景）和执行框架演进（新工具、新流程、新技能）双重挑战，一次性训练的模型很快性能衰退，定期人工重训延迟高、人力成本高；现有自进化方法仅解决单点问题，无法同时处理模型、数据、奖励三者的不匹配，也无法保证旧能力不遗忘。

### 方法关键点
- 双循环架构：主自进化循环处理日常训练，奖励进化循环处理能力契约变更后的奖励更新
- 奖励路由+熵优先数据编排：每个query生成8个rollout，全失败带验证目标的进SFT池，混合成败的进RL池，全成功的进回归监控池；池内按token级熵的90分位值排序，优先训练高不确定性样本
- 受管控奖励进化：检测到奖励不可靠时，先标注审计case，更新奖励规则后过目标验证、历史回归、重打分、轨迹回放四道门槛，验证通过后再投入使用
- 受管控checkpoint切换：候选模型必须同时通过新需求评测和所有历史能力回归评测，才能替换线上模型

### 关键实验
在阿里1688 B2B采购Agent Yuancai的4个演进阶段真实数据集上测试，对比基线AutoTrainess：第4阶段新需求Reward提升0.183（基线提升0.200），同时历史保留Reward提升0.012（基线下降0.017），累计Reward达0.8078（基线0.7911）；skill选择准确率达0.7625（基线0.6875），skill adherence达0.4503（基线0.4219）；上线后人工奖励审计成本从2人天/轮降到30分钟/轮，需求到上线周期从1周降到2天。

### 核心结论
持续迭代的电商Agent场景中，受管控的checkpoint和奖励切换，比单纯优化固定目标下的训练效果更重要。
