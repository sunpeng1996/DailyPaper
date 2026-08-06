---
title: 'A-SR: Self-Evolving Agentic LLMs for Symbolic Regression via Hierarchical
  Coordination'
title_zh: A-SR：基于分层协调的自进化智能体大模型符号回归框架
authors:
- Wenxiao Zhao
- Dong Liu
- Kaiyi Xu
- Feng Liu
- Zhen Zhao
- Fei Ben
- Shu Wang
- Wenhao Li
- Yingnian Wu
- Fenghua Ling
affiliations:
- Shanghai AI Laboratory
- University of California at Los Angeles
- Tongji University
arxiv_id: '2608.04872'
url: https://arxiv.org/abs/2608.04872
pdf_url: https://arxiv.org/pdf/2608.04872
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: 符号回归 · 多智能体分层协调
tags:
- Agentic-LLM
- Symbolic-Regression
- Hierarchical-Coordination
- LoRA
- Self-Evolution
- Memory-Routing
one_liner: 通过分层角色协调、在线自适应和记忆路由，大幅提升LLM符号回归的准确率与泛化性
practical_value: '- 多角色动态路由机制可直接迁移到生成式推荐/广告文案/搜索query改写场景：按当前生成状态（无效内容占比高/收敛停滞/内容冗余）动态调度生成、质检、简化优化角色，替代固定单prompt迭代，提升生成有效性和转化率

  - 在线角色效用更新机制可复用：基于业务侧可观测反馈（点击率、无效内容占比、转化效果）实时更新不同角色的调度优先级，无需更新LLM参数，推理端即可自进化适配动态业务流量

  - 轨迹蒸馏的降本方案可复用：将历史多智能体调度的优质执行轨迹通过LoRA蒸馏为小模型的角色条件先验，小参数模型即可获得接近大模型的效果，大幅降低推理成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM引导的符号回归方法依赖统一的提议-评估循环，将异构搜索失败（无效表达式、参数不稳定、冗余项、泛化性差等）压缩为单一标量奖励和单个prompt，无法匹配不同失败模式对应的修正策略，导致搜索效率低、准确率和泛化性差。
### 方法关键点
- 分层协调框架：设置Generator（生成新结构）、Analyst（诊断结构缺口）、Simplifier（压缩简化公式）、Reviewer（校验有效性和稳定性）4个角色，共享LLM骨干，按搜索状态动态调度
- 双时间尺度自进化：单轮搜索内通过协调协议选择、在线角色效用更新、状态路由记忆适配搜索过程，无需更新LLM参数；跨轮次可将优质轨迹通过LoRA蒸馏为角色条件提议先验，提升小模型效果
- 结构化反馈路由：将评估反馈拆分为有效性、改进量、失败类型、复杂度等多维度信号，不同搜索状态下给不同角色路由对应的记忆（优质候选、失败轨迹、结构基序）
### 关键实验
在LLM-SRBench的4个科学领域数据集上，对比DE等基线，基于Llama3.1-8B的A-SR将平均Acc@0.01从25.79%提升到48.30%；基于Qwen3-4B的A-SR-LoRA将对应Acc@0.01从24.58%提升到38.29%；在4个真实世界科学发现任务上，A-SR在8个ID/OOD NMSE指标中拿到7个最优。
### 核心结论
智能体控制的核心从「选择什么编辑操作」转向「给什么角色分配什么证据视图」，可在不更新LLM参数的前提下大幅提升复杂搜索任务的效果
