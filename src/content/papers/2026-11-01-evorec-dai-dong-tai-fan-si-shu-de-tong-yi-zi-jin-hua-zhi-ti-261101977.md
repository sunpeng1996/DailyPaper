---
title: 'EvoRec: A Unified Self-Evolving Agentic Recommender with Dynamic Reflection
  Trees'
title_zh: EvoRec：带动态反思树的统一自进化智能体推荐系统
authors:
- Mengting Li
- Long Zhang
- Hao Jiang
- Sheng Yu
- Fei Pan
- Peng Jiang
affiliations:
- Kuaishou
arxiv_id: '2611.01977'
url: https://arxiv.org/abs/2611.01977
pdf_url: https://arxiv.org/pdf/2611.01977
published: '2026-11-01'
collected: '2026-11-03'
category: Agent
direction: 智能体推荐 · 动态反思树自进化
tags:
- Agentic Recommendation
- Dynamic Reflection Tree
- Self-Evolving
- LLM4Rec
- Industrial Deployment
one_liner: 提出端到端自进化Agent推荐框架，靠动态反思树闭环优化无需更新模型参数
practical_value: '- 部署层面可直接复用近线LLM推理+在线消费架构，将Agent决策、候选生成逻辑放在近线异步运行，完全不占用实时请求耗时，无需改造现有精排链路即可落地

  - 反馈闭环可直接借鉴动态反思树设计：将错误定位到需求识别、检索规划、历史修复策略三个维度，仅生成策略级（而非具体item级）修复规则，经replay验证后再存入记忆，避免过拟合单条反馈

  - 检索融合可直接落地双路径动态分配方案：将召回池拆分为历史行为匹配、需求匹配两个独立路径，由Agent按用户行为丰富度、需求明确度动态分配召回预算和排序融合权重，比固定权重配置相对提升10%+召回准确率'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统级联推荐管道固定、依赖离线参数更新，难以适配动态变化的用户需求；现有Agent推荐大多仅覆盖单阶段流程，缺乏端到端决策控制，也无法系统性定位推荐失败的根因，用户反馈仅能用于更新参数或存储原始交互记忆，无法转化为可复用的优化经验。

### 方法关键点
1. 三模块端到端Agent决策流：Need Agent从长短期记忆+工作记忆推理结构化用户需求；Planning Agent动态分配Behavior Continuation（历史行为匹配）与Need Satisfaction（需求匹配）的检索预算，选择召回工具、定排序融合权重；Acting Executor按计划执行检索、RRF融合、排序，留存全链路决策trace。
2. 动态反思树自进化闭环：收到用户反馈后，按trace定位错误到需求推理/规划/历史修复策略三类，分层匹配通用错误模式生成个性化修复策略，经replay验证后存入工作记忆，经验积累到阈值后抽象为跨用户通用策略，全程不更新Agent参数。
3. 工业级部署方案：采用近线生成+在线消费架构，LLM推理全放近线，预生成候选集与现有召回路并行汇入精排，不影响实时链路耗时。

### 关键实验
基于快手本地服务广告数据集，对比传统推荐、生成式推荐、Agent推荐三类共8种基线：离线Hit@50比最强基线InteRecAgent高15.7%，有修复经验的用户Hit@50提升13.1%；7天在线A/B测广告收入提升4.6%、CTCVR提升3.5%，高意向用户收入提升14.5%。

**最值得记住的结论**：Agent推荐系统无需频繁更新模型参数，基于可验证的策略级反思记忆即可实现持续效果迭代，且能完美兼容现有工业级级联推荐架构
