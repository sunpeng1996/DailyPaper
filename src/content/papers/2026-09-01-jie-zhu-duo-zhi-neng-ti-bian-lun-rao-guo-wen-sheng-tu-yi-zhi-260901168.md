---
title: 'Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous
  Safety Filters via Multi-Agent Debate'
title_zh: 借助多智能体辩论绕过文生图异质安全过滤器的越狱方法
authors:
- Kaiyan Wen
- Shijie Zhang
- Lu Yu
- Guangdong Bai
arxiv_id: '2609.01168'
url: https://arxiv.org/abs/2609.01168
pdf_url: https://arxiv.org/pdf/2609.01168
published: '2026-09-01'
collected: '2026-09-07'
category: Agent
direction: 多智能体攻防 · 文生图安全防护
tags:
- Multi-Agent Debate
- Jailbreak
- Text-to-Image
- Safety Filter
- Generative AI Safety
one_liner: 提出多智能体辩论框架CRACK，可高效突破文生图多层复合安全防护，攻击成功率最高达99.63%
practical_value: '- 三角色（攻击/防御/裁判）多智能体分工迭代的框架可复用在多约束寻优场景，比如推荐多目标优化、电商合规内容生成的prompt自动调优

  - 异质多层过滤器的分层反馈调试思路，可迁移到电商商品图/营销文案的多层合规校验场景，大幅降低合规迭代的查询成本

  - 保留核心意图的奖励引导突变搜索方法，可用于广告创意迭代，在不改变营销核心信息的前提下快速生成过审且高转化的创意变体'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有文生图越狱方法要么针对单个安全过滤器优化，要么仅获取全链路聚合反馈，无法适配多层异质安全栈的跨层约束冲突，难以高效定位激活的拦截规则，迭代成本高。
### 方法关键点
1. 提出Detection Surface统一几何框架，建模多层异质安全过滤器的决策边界，明确跨层冲突下的越狱可行域为稀疏非凸区域，突变绕过某层过滤器可能触发其他层拦截
2. 设计CRACK多智能体辩论框架，拆分任务为探索、诊断、仲裁三个环节：Attack Agent生成prompt突变，Defense Agent输出分层拦截诊断反馈，Judge Agent基于奖励优化突变策略，迭代全程保留原始意图
### 关键结果
在多文生图模型、多安全配置下，复合防护场景攻击成功率（ASR）最高达99.63%，相比现有基线方法查询量更少，且prompt语义保真度更高
