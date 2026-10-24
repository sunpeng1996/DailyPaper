---
title: 'IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems'
title_zh: IF-MAP：基于影响函数启发的多智能体系统Agent优先级排序方法
authors:
- Jie Mao
- Pingchen Lu
- Zikun Qu
- Jiahang Sun
- Xiangyi Wang
- Zhiwei Shang
- Zhiyong Wang
- Guojun Xiong
- Zhongxiang Dai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Harbin Institute of Technology
- Harvard University
arxiv_id: '2610.24383'
url: https://arxiv.org/abs/2610.24383
pdf_url: https://arxiv.org/pdf/2610.24383
published: '2026-10-16'
collected: '2026-10-24'
category: MultiAgent
direction: 多智体系统 · Agent优先级优化
tags:
- Multi-Agent System
- Influence Function
- Agent Prioritization
- LLM Agent
- Black-box Optimization
one_liner: 提出黑盒无梯度的多Agent优先级排序方法，用有限资源最大化系统级性能增益
practical_value: '- 电商多Agent推荐/客服系统优化时，无需全量迭代所有Agent，先用IF-MAP探针方法测试每个Agent的响应敏感度，优先优化高收益节点，大幅降低调优成本

  - 可直接复用语义扰动探针设计：仅改动单个Agent的prompt（保留角色和输出接口），测试端到端业务指标变化，无需访问模型参数或梯度，适配业务黑盒场景

  - 优先级评分逻辑可迁移：基于prompt embedding位移和业务损失变化拟合局部响应模型，取响应向量L2范数作为优先级，比传统错误归因的优化指导更准确

  - 资源有限时优先给高优先级Agent升级大模型/做LoRA微调，实测增益是均匀选择的1.86-2.05倍，同时可减少60%+高算力模型的token消耗'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM多Agent系统已广泛应用于复杂任务，但全量优化所有Agent（修改prompt、升级模型、微调）的算力和人力成本极高；传统失败归因方法仅能定位错误责任，无法直接反映优化该Agent能带来的系统级增益，资源受限下无法判断优先投入方向。

### 方法关键点
- 黑盒语义探针：对单个Agent独立构造最多10种prompt语义扰动（保留角色定位和输出接口），其他Agent和系统结构固定，测量端到端损失变化
- 局部响应建模：将prompt扰动转化为embedding空间的位移，归一化后在低维子空间做岭回归，拟合每个Agent的局部响应向量
- 优先级评分：取响应向量的L2范数作为优先级，范数越大代表优化该Agent的潜在系统增益越高

### 关键实验
在代码生成、问答、数学推理共6类多Agent工作流上验证，对比7种失败归因基线方法：
1. Prompt优化场景：IF-MAP选择的Agent平均增益3.81pp，是均匀选择（1.85pp）的2.06倍，排名与实际增益的Kendall τb达0.741
2. 模型升级场景：选择的Agent平均增益7.62-16.42pp，是均匀选择的1.86-2.05倍，相比全量升级所有Agent减少63.6%-64.9%的目标模型token消耗

### 核心结论
多Agent系统的错误归因责任不等于优化收益，基于扰动响应的局部敏感度估计才是资源受限下选择优先优化目标的核心判断标准
