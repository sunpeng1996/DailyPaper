---
title: Interpretable Adaptive Sampling for LLM Test-Time Scaling
title_zh: 面向LLM测试时缩放的可解释自适应采样方法
authors:
- Mobina Kashaniyan
- Ali Jannesari
affiliations:
- Iowa State University
arxiv_id: '2608.03961'
url: https://arxiv.org/abs/2608.03961
pdf_url: https://arxiv.org/pdf/2608.03961
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: LLM推理 · 测试时自适应采样
tags:
- Adaptive Sampling
- Test-time Scaling
- Fuzzy Control
- Interpretability
- LLM Inference
one_liner: 基于可解释模糊控制器为每个prompt动态分配采样预算，兼顾推理精度与计算效率
practical_value: '- Agent 多步推理、电商客服/营销文案生成场景可复用这套自适应采样逻辑，简单query少采样降时延，复杂query多采样提准确率，平衡成本与体验

  - 可直接复用论文的特征设计：prompt复杂度（长度、符号密度、语义歧义）+ 模型置信度（首帧输出token概率、熵）作为动态调整计算资源的输入信号，无需复杂训练即可上线

  - 测试时多候选聚合场景可搭配Borda+自置信度排序的选答策略，比固定Best-of-N效果更稳定，避免多采样引入的错误候选干扰

  - 对计算敏感的线上LLM服务（比如搜索query改写、推荐理由生成），优先用模糊控制替代黑盒分配策略，决策可审计，符合业务合规要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM测试时缩放技术（通过生成多候选答案聚合提升推理效果）普遍采用固定每query采样预算，既容易在简单query上浪费算力、复杂query上算力不足，又因固定预算或黑盒分配策略无法解释算力分配逻辑，不利于线上服务的调试、审计与成本管控。
### 方法关键点
- 特征层：提取两类归一化输入信号，prompt侧包括表面复杂度、NLP复杂度（覆盖符号密度、语义歧义、推理深度等维度）、prompt类型、预期回答长度；模型侧包括首版草稿输出的token概率置信度、分布熵、历史同类query表现
- 决策层：采用两级分层模糊控制器，先基于prompt复杂度+模型置信度输出粗粒度预算，再结合其余特征做细粒度修正，无需训练、决策过程完全可解释，避免硬阈值的鲁棒性问题
- 输出层：将连续预算分数映射为整数采样数，对高复杂度query设置最低采样数保底，最终通过自置信度排序+Borda聚合选出最优答案
### 关键结果
在GSM8K（小学数学）、MATH（高等数学）、SciQ（科学问答）三个数据集上测试Phi-3-mini、Qwen2.5-1.5B两个模型，对比固定Best-of-N、计算最优分配、自置信度选答等基线：
1. 对比固定N=8基线，MATH数据集上平均减少10.8%~14.5%采样数，精度仅下降0.007~0.018；GSM8K上精度基本持平，减少1.4%~3.9%采样数
2. SciQ数据集上精度优于所有基线，同时平均采样数降至6.94~7.27；当Nmax=32时，相比固定全预算采样最高可节省29.7%总计算量
### 核心结论
测试时缩放不应该盲目增加算力，而应该基于可解释的信号动态分配，在精度可控的前提下最大化算力效率。
