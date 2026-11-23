---
title: 'Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation'
title_zh: Embodied-Harness：面向机器人操作的递归自改进双智能体框架
authors:
- Zhenxuan Fan
- Zhuoya Wang
- Yuqian Yuan
- Wenqiao Zhang
- Juncheng Li
- Jun Xiao
- Siliang Tang
- Yueting Zhuang
affiliations:
- Zhejiang University
- Huazhong University of Science and Technology
arxiv_id: '2611.27689'
url: https://arxiv.org/abs/2611.27689
pdf_url: https://arxiv.org/pdf/2611.27689
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: 具身智能 · 双Agent无参数自优化
tags:
- Embodied AI
- Dual-Agent
- Experience Reuse
- Self-Improvement
- VLM
one_liner: 提出Actor+Reflector双智能体架构，无需更新模型参数即可通过经验反思迭代优化机器人操作效果
practical_value: '- 双Agent（执行+复盘）分工架构可直接迁移到电商运营Agent、推荐策略迭代Agent场景，执行Agent跑AB实验/落地策略，复盘Agent自动归因失败原因生成优化规则，无需微调LLM参数即可迭代效果，大幅降低落地成本

  - 分层记忆（短期上下文+长期跨任务经验）架构可复用在搜索推荐的用户行为记忆模块、RAG系统的历史调用效果沉淀模块，区分临时会话信息和通用可复用经验，提升记忆检索准确率与效率

  - 基于实证的失败归因机制可迁移到推荐召回排序的bad case自动归因链路，无需人工标注，直接依托真实用户交互反馈生成优化规则，降低bad case运营成本'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
基于VLM的具身Agent在机器人操作场景存在记忆组织混乱、失败归因模糊、执行经验复用率低的痛点，主流优化方案依赖模型参数微调，落地成本高、泛化性有限。
### 方法关键点
1. 双Agent分工架构：Actor负责对接环境执行操作，Reflector负责将执行证据转化为可复用操作指导，全程无参数更新；
2. 分层记忆架构：分别存储短期执行上下文与长期跨任务经验，支撑执行决策与复盘归因；
3. 基于实证的递归自优化：依托真实交互证据做失败诊断，跨任务迭代优化操作指导规则。
### 关键结果
在RoboTwin 2.0、RoboSPA、RMBench三个公开基准上成功率分别达82.4%、76.7%、94.4%，真实场景三类操作任务平均成功率达96.7%，性能大幅领先现有基线方案
