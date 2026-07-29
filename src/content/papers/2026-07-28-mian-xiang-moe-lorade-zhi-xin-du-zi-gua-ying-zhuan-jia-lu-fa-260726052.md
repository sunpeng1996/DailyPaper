---
title: 'Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts
  LoRA'
title_zh: 面向MoE-LoRA的置信度自适应专家路由算法CARE
authors:
- Tom Saliencro
- Rohan Desai
- Priya Nair
- Maya Lindqvist
- Daniel Whitmore
affiliations:
- University of California, Irvine
- University of Washington
arxiv_id: '2607.26052'
url: https://arxiv.org/abs/2607.26052
pdf_url: https://arxiv.org/pdf/2607.26052
published: '2026-07-28'
collected: '2026-07-29'
category: Training
direction: PEFT优化 · MoE-LoRA自适应路由
tags:
- LoRA
- MoE
- Adaptive Routing
- Uncertainty Estimation
- OOD Detection
one_liner: 提出无额外参数的单前向传播MoE-LoRA自适应路由CARE，同算力提精度、同精度省12%专家
practical_value: '- 现有部署的MoE-LoRA服务可直接替换固定top-k路由为CARE，无需重训，同算力下可提升电商文案生成、query理解、用户意图识别等任务精度，同精度下降低12%推理成本

  - 复用路由器分布置信度+专家输出不一致性信号，可零成本获得单前向传播的OOD检测能力，用于异常query识别、低置信度推荐结果人工兜底、违规内容前置拦截

  - 预算恒温器设计可直接复用给多expert召回/排序模块，根据请求难度动态分配计算资源，在固定整体算力预算下最大化业务效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有MoE-LoRA普遍采用固定top-k路由策略，所有token分配相同数量专家，导致简单token算力浪费、困难token算力不足，限制模型效果天花板；同时现有大模型不确定性估计方法多依赖多轮前向传播或额外参数，推理成本高，无法复用路由阶段天然产出的分布信号。
### 方法关键点
- 借鉴核采样思路设计专家准入规则：按路由器输出权重降序累加，直到累计质量达到阈值τ，作为基础入选专家集，置信度越高的token需要的专家越少
- 新增认知不确定性扩展：若已入选专家输出的加权方差超过阈值，最多额外新增γ个专家，优化歧义样本的处理效果
- 预算恒温器：在小范围验证集上通过二分搜索校准全局阈值τ，保证平均激活专家数完全匹配目标算力预算，无需改动模型结构和训练逻辑
- 天然支持不确定性输出：融合路由分布熵和专家不一致性得分，单前向传播即可获得序列级置信度，可直接用于OOD检测和选择性预测
### 关键实验
在LLaMA-3.1-8B、Qwen2.5-7B两个骨干上，覆盖常识推理、数学、代码、知识四大类共20+基准任务，对比LoRA、DoRA、LoRAMoE、FlyLoRA等10+基线：同平均4个专家的算力预算下，常识推理任务平均精度提升0.5个点，数学/代码/知识任务平均提升0.9个点；匹配固定k=4基线精度时，平均激活专家数减少12%；OOD检测AUROC达0.668，优于MSP、路由熵、多轮MC-dropout等方法。
### 核心结论
MoE路由器的输出分布本身就是天然的样本难度/置信度信号，无需额外模型或计算开销即可实现算力的动态最优分配。
