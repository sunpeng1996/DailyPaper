---
title: 'CoBa: Cost-Effective Test-Time Scaling via Compute-Balanced Routing'
title_zh: CoBa：基于计算均衡路由的高性价比测试时扩缩方法
authors:
- Yan Zhou
- Yue Ouyang
- Kaiyang Zheng
- Suncheng Xiang
affiliations:
- 长沙理工大学数学与统计学院
- 上海交通大学生物医学工程学院
arxiv_id: '2608.07424'
url: https://arxiv.org/abs/2608.07424
pdf_url: https://arxiv.org/pdf/2608.07424
published: '2026-08-07'
collected: '2026-08-10'
category: Reasoning
direction: LLM测试时扩缩 · 计算资源调度
tags:
- Test-Time Scaling
- Compute Allocation
- Routing Policy
- Inference Optimization
- Reasoning
one_liner: 将测试时推理建模为计算分配问题，通过分层路由在精度相当前提下降本近50%
practical_value: '- 电商/广告场景的多候选生成（query改写、文案生成、推荐理由生成）可复用分层路由逻辑：先出少量候选用小模型粗筛，仅高价值/不确定候选调用大模型精评，大幅降低推理成本

  - Agent推理链路可复用停止准则：当多轮候选答案一致且小模型置信度达标时直接返回，无需执行后续工具调用/复杂推理步骤，降低端到端latency

  - 生成式系统的成本核算可参考parameter-weighted token设计，将模型参数量、token数、latency加权得到统一成本指标，辅助做精度与成本的帕累托优化'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有测试时扩缩方案（多候选采样、长链推理、强验证器打分）均为单轴堆计算，固定推理预算下不同方案相互挤占，无法根据任务难度动态分配资源，简单任务也会付出不必要的高成本。

### 方法关键点
- 将测试时推理建模为生成、轻量验证、强验证、停止四类动作的计算分配问题，决策状态包含候选集、得分与不确定性、剩余预算、历史行为四类可观测特征
- 采用三段式路由流程：先暖身生成2个初始候选，用规则（答案频率）+ 8B参数小模型对所有候选做轻量打分，若答案不稳定则补充生成最多8个候选
- 仅将排序前4的高价值/高不确定性候选路由给14B参数强验证器打分，融合多源得分选择最优答案，无强验证得分的候选不做人工惩罚或增益

### 关键结果
在MATH-500、AIME2024/2025等5个推理数据集、3个基座模型共3129组评测中，CoBa-Routed-Strong精度达85.13%，与自评估加权投票方案（85.20%）精度相当，parameter-weighted token成本降低49.1%；与best-of-16多数投票的精度差仅0.01%，parameter-weighted token成本降低58.9%；相比单采样解码精度提升3.74个百分点。

最值得记住的结论：测试时扩缩的核心不是盲目堆砌计算，而是把每一分计算资源花在能改变最终决策的场景。
