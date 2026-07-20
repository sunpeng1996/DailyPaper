---
title: 'DSWorld: A Data Science World Model for Efficient Autonomous Agents'
title_zh: DSWorld：面向高效自主Agent的数据科学世界模型
authors:
- Zherui Yang
- Fan Liu
- Hao Liu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2607.15901'
url: https://arxiv.org/abs/2607.15901
pdf_url: https://arxiv.org/pdf/2607.15901
published: '2026-07-16'
collected: '2026-07-20'
category: Agent
direction: Agent 世界模型 训练推理效率优化
tags:
- World Model
- LLM Agent
- RL Optimization
- Simulation
- Efficiency
one_liner: 提出数据科学世界模型框架，无需执行高成本操作即可预测状态转移，大幅提升Agent训练与推理效率
practical_value: '- 可复用cost-aware路由设计：电商/推荐Agent调用工具时，轻量操作（简单特征统计、规则校验）直接执行，高成本操作（大模型训练、海量召回打分）走模拟预测，平衡精度与速度

  - 反射式RL优化可直接迁移：做Agent工具调用结果预测时，先SFT初始化再用GRPO做误差感知的迭代优化，比纯SFT预测精度更高，适配动作结果有明确ground
  truth的场景

  - 训练数据合成方案可落地：缺乏Agent交互轨迹时，先构造基础状态/动作库，用LLM生成多样动作，真实执行后过滤有效样本，补充CoT解释，低成本扩量训练数据

  - 世界模型加速Agent范式可复用：推荐系统RL排序/多轮召回Agent训练时，可用世界模型模拟用户反馈，替代部分真实流量/AB实验，大幅降低训练成本与周期'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前自主数据科学Agent依赖试错工作流，80%以上时间消耗在模型训练、数据处理等高成本计算上，严重限制训练与推理效率，亟需能提前预测操作效果的转移模型，避免无效高成本执行。

### 方法关键点
- 混合架构设计：State Constructor将原始环境转为包含任务、数据、运行时、日志的结构化状态；Cost-Aware Router判断操作成本，轻量操作走Compiler直接执行，高成本操作走LLM-based Simulator预测下一个状态，执行超时自动切换为模拟
- 两阶段训练策略：先在8K规模的真实+合成转移轨迹数据集上做SFT初始化，再用Reflective World Model Optimization（基于GRPO的误差感知RL策略）迭代修正预测误差
- 高质量数据集构建：构造DSWorld-8K数据集，包含真实执行轨迹和LLM合成、经过真实执行校验的转移样本，每个样本配CoT推理轨迹解释转移逻辑

### 关键结果
- 转移预测任务：对比o4-mini等最强基线，平均性能提升35.6%
- Agent训练场景：RL训练速度提升14倍，性能与真实执行训练基本持平
- Agent推理场景：搜索式Agent推理速度提升3-6倍，性能下降可忽略

轻量执行+重操作模拟的混合架构做世界模型，是兼顾Agent效率与精度的高性价比路径
