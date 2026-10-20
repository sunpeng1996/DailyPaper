---
title: 'HSPR: Recovering Software-Agent Benchmark Scores via Hierarchical Posterior
  Inference'
title_zh: HSPR：基于分层后验推理的Agent基准分数高效恢复方法
authors:
- Wanyi Chen
- Wanqin Shen
- Yuanchen Shi
- Zhensu Sun
- Fang Kong
affiliations:
- Soochow University
- Singapore Management University
arxiv_id: '2610.24611'
url: https://arxiv.org/abs/2610.24611
pdf_url: https://arxiv.org/pdf/2610.24611
published: '2026-10-16'
collected: '2026-10-20'
category: Agent
direction: Agent 基准测试高效评估优化
tags:
- Agent Evaluation
- Hierarchical Inference
- Adaptive Testing
- Benchmarking
- Posterior Estimation
one_liner: 结合分层响应建模与自适应查询，10%任务预算下实现SOTA的Agent基准分数恢复精度
practical_value: '- 内部Agent性能评估场景可直接复用该方案，仅跑10%的测试用例即可拿到误差<2pp的全量分数，大幅降低评估成本

  - 推荐系统A/B测试可借鉴后验引导采样逻辑，仅抽样少量用户即可估计全量策略效果，缩短测试周期

  - LLM4Rec模型选型评估可复用历史响应分组的不确定度建模思路，降低长尾query/item的评估误差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
软件Agent基准测试通常需要执行成百上千个任务，全量执行时间/金钱成本极高；传统小任务子集采样方法仅能保证Agent排名一致性，分数估计误差大，且历史响应数据的模式无法有效迁移到新Agent的评估中，亟需低成本高精度的基准分数恢复方案。

### 方法关键点
- 基于历史Agent的响应数据，用正则化逻辑IRT模型拟合任务难度、区分度参数，通过SVD提取残差因子，按源响应签名对任务分组，每组共享不确定的成功率先验
- 每观测一个目标Agent的任务执行结果，同时更新全局潜在状态后验和分组成功率后验，实现组内、组间的信息传递
- 采用后验引导的自适应查询策略，每次选择能最大程度降低全量分数后验方差的任务组，组内随机采样任务执行
- 最终全量分数估计采用后验中位数，搭配源数据选择的校准项修正偏差，最小化绝对损失

### 关键实验
在SWE-bench的4个任务集（Lite/Verified/Full/Pro）上测试，对比Uniform、Mid-Range、ATLAS-port、PTA-IRT等7个基线，10%任务预算下：HSPR在3个数据集上MAE最低，所有数据集上MaxErr最低，平均MAE仅1.664pp，比最强基线PTA-IRT的2.478pp低32.9%；去掉组不确定度或自适应查询，宏观MAE分别上升8.6%、85.4%；预算在5%-20%区间时，MAE随预算提升持续下降。

### 核心结论
对于有历史响应数据的基准测试，仅用10%的执行预算即可拿到误差<2pp的全量分数估计，成本仅为全量测试的1/10。
