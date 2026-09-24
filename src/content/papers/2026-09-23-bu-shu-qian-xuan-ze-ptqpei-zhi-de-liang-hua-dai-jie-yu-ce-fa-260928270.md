---
title: Predicting Quantization Price for Selecting PTQ Configurations Before Deployment
title_zh: 部署前选择PTQ配置的量化代价预测方法
authors:
- Junbin Qiu
- Jian Mu
- Weitong Zhang
- Yao Shu
affiliations:
- 香港科技大学（广州）
arxiv_id: '2609.28270'
url: https://arxiv.org/abs/2609.28270
pdf_url: https://arxiv.org/pdf/2609.28270
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM推理优化 · PTQ配置选择
tags:
- PTQ
- LLM Quantization
- Hessian
- Model Compression
- Deployment
one_liner: 基于前向KL与下游曲率提出统一量化代价度量，可部署前跨家族高效优选PTQ配置
practical_value: '- 业务侧：生成式推荐、导购Agent、用户Query理解等场景的LLM部署降本，可直接用该量化代价度量替代全量训测候选配置，大幅降低PTQ方案选型成本

  - 架构侧：复用统一量化代价框架，可将不同比特、量化粒度、预量化变换（如AWQ、SmoothQuant）放到同一维度对比，无需单独开发各配置的评估逻辑

  - 工程侧：直接借鉴低成本Trace近似实现，无需存储全量Hessian矩阵，仅预计算每层Hessian迹即可完成配置打分，内存开销低，适配7B/70B等大模型的离线选型流程'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有PTQ方法需完成全量量化部署才能得到精度损失，无法在部署前跨比特、量化粒度、预量化变换等不同配置家族统一打分，全量遍历候选配置成本极高，单独的重建误差、Hessian敏感度等局部指标又无法覆盖多维度配置的全局精度影响，亟需统一的预部署选型度量。

### 方法关键点
- 将PTQ配置选择建模为部署预算约束下的优化问题，目标最小化全精度模型到量化模型的前向KL散度
- 推导得到量化代价的二次表达式：每层配置产生的层输出误差协方差乘以下游曲率的迹，天然消除一阶项影响，可兼容所有PTQ配置家族
- 提出低成本近似打分方法，仅需预计算每层Hessian迹、候选配置的输入尺度和扰动尺度3个标量即可完成打分，无需构建完整量化模型
- 基于预计算的打分表做预算约束下的离散搜索，快速选出最优配置组合

### 关键实验结果
在OPT-125M、Qwen3-0.6B上，量化代价与实际KL漂移的相关系数最高达0.9483；在Llama-3.2-1B 3比特量化任务上，比SOTA比特分配方法HIGGS的配置搜索速度快40%，下游任务平均准确率高0.67个百分点，配置搜索时间比AMQ低20倍以上，同时在预量化变换选择、量化粒度分配任务上均取得最优PPL和下游任务得分。

### 最值得记住的结论
PTQ配置选择的核心是构建跨配置家族的统一量化代价度量，而非局限于固定量化结构下的比特分配
