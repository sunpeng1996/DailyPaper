---
title: 'Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation'
title_zh: 自适应推理：大模型测试阶段计算资源动态分配方法
authors:
- Gijs Kassenaar
- Zhao Yang
- Vincent François-Lavet
affiliations:
- Vrije Universiteit Amsterdam
arxiv_id: '2608.20256'
url: https://arxiv.org/abs/2608.20256
pdf_url: https://arxiv.org/pdf/2608.20256
published: '2026-08-20'
collected: '2026-08-21'
category: Reasoning
direction: 大模型自适应推理 · 算力效率优化
tags:
- LLM
- GRPO
- Adaptive Reasoning
- Compute Efficiency
- Reinforcement Learning
one_liner: 无需额外路由网络，GRPO端到端训练让LLM自主选3种推理模式，大幅降低推理token消耗
practical_value: '- 电商/客服场景用LLM生成回复、商品文案时，可复用该多模式自适应路由思路，对简单query（如查物流、问运费）走短回复模式，复杂query（如售后纠纷、定制化需求）走长推理模式，可降低40%+推理成本同时不影响用户体验

  - 用GRPO做LLM对齐训练时，防模式坍塌的3个trick可直接复用：分模式设置硬token上限+优势计算加入负载均衡项+强制warmup阶段引导路由学习，避免策略向单一模式收敛

  - Agent系统做任务调度时，可借鉴该思路设置多档推理深度：对简单任务直接返回结果，中等任务走少量步骤推理，复杂任务调用工具/多轮思考，可大幅降低Agent平均响应延迟

  - 生成式推荐场景中用LLM生成个性化推荐理由时，可对不同优先级请求匹配不同推理深度：高价值用户/高转化商品走详细生成模式，低优先级请求走简洁模式，平衡生成质量和算力成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前基于RL训练的推理大模型普遍采用固定token预算，易在简单问题上过度计算、复杂问题上算力不足，全局长度惩罚的优化方式非自适应，无法匹配不同问题的推理深度需求，还易出现路由模式坍塌问题。
### 方法关键点
- 无独立路由模块：让模型输出的首个token选择NoThink/Short/Long三种推理模式，路由决策融入主策略端到端GRPO训练
- 分模式约束设计：三种模式分别设置1024/3000/无上限的硬token上限，搭配差异化奖励：短模式正确基础奖励更高但随长度衰减，长模式奖励无衰减，避免路由标签与实际推理行为解耦
- 训练稳定性优化：改进GRPO优势计算，移除标准差归一化避免小奖励被异常放大，加入优势负载均衡项防止模式坍塌，搭配强制路由warmup阶段引导模型学习路由逻辑
### 关键结果
在1.5B DeepSeek-R1蒸馏模型上用MATH数据集训练：
- 分布内MATH500测试集：精度接近基线（0.782 vs 0.796），平均响应token数从4796降至2811，减少41%
- 零样本迁移到GSM8K：token减少76%，精度高于同长度固定模式基线
- 零样本迁移到高难度AIME数据集：模型自动选择长推理模式，仅减少13%token，精度几乎无损失
### 核心洞察
自适应推理是比全局固定预算更优的算力分配方式，核心是让模型自主匹配问题难度与推理深度，而非用统一规则约束所有请求。
