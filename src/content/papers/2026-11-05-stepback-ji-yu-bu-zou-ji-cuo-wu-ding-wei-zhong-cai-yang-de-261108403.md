---
title: 'StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning'
title_zh: StepBack：基于步骤级错误定位重采样的高效测试时推理方法
authors:
- Yang Ouyang
- Jung-Eun Kim
affiliations:
- North Carolina State University
arxiv_id: '2611.08403'
url: https://arxiv.org/abs/2611.08403
pdf_url: https://arxiv.org/pdf/2611.08403
published: '2026-11-05'
collected: '2026-11-06'
category: Reasoning
direction: 高效CoT推理 · 步骤级错误重采样
tags:
- Self-Consistency
- Chain-of-Thought
- Test-Time Inference
- Error Localization
- Token Efficiency
one_liner: 提出步骤级错误定位重采样推理方法，匹配Self-Consistency精度同时最高降低41.26%的token消耗
practical_value: '- 电商Agent多步推理场景（如用户复杂需求拆解、跨品类选品链路推理）可复用StepBack逻辑，无需每次重跑全推理链路，仅重采样错误步骤及后续，大幅降低推理时延和token成本

  - 生成式推荐采用CoT做用户兴趣路径推理时，可直接使用无需额外模型的NLL-SIGNAL错误定位规则，无需额外训练就能降低30%左右推理token消耗，精度几乎无损

  - 可将StepBack与现有自适应推理方法（如Adaptive Consistency）结合，进一步降低复杂推荐场景大模型推理成本，实测组合后比原SC@32省5.2倍token还高0.9个点精度

  - 优化推荐系统LLM推理链路时，可参考draft与suffix的分配策略：精度优先场景用多draft少suffix，成本优先场景用少draft多suffix'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Self-Consistency（SC）是提升Chain-of-Thought推理精度的通用方案，但需要生成多条完整推理轨迹，token成本随采样数和轨迹长度线性增长；现有优化方法仅在完整轨迹维度控制采样数量，没有利用推理错误多发生在中间步骤、早期步骤可复用的特性，存在大量冗余计算。

### 方法关键点
- 先采样少量draft推理轨迹，按自然分隔符（空行、编号）拆分为独立推理步骤
- 用两种轻量信号定位首条错误步骤：一是基础模型自带的步骤级NLL突增（NLL-SIGNAL，无额外开销），二是Process Reward Model的步骤得分突降（PRM-SIGNAL，准确率更高）
- 复用错误步骤之前的正确前缀，仅重采样错误步骤及后续后缀，所有候选答案通过多数投票得到最终结果，可无缝兼容现有自适应推理方法

### 关键结果
在GSM8K、MATH500、HotpotQA等7个数学推理和多跳QA基准上测试，对比SC@32基线：
- 采用PRM-SIGNAL的StepBack平均精度超过SC 0.17~0.82个百分点，同时减少18.66%~22.80%的token消耗，GSM8K场景下最高节省41.26%的token
- 结合DSC自适应推理方法后，GSM8K场景下比SC@32少用5.2倍token，精度还高0.9个百分点；错误定位的计算开销仅占总推理时长的7%~11%，不会抵消token节省的收益

### 最值得记住的一句话
大模型测试时推理的效率优化，不仅可以控制采样轨迹的数量，还可以在单条轨迹内部精准分配计算资源，只给可能出错的步骤分配采样预算。
