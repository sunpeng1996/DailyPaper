---
title: Efficient SWE Agent Benchmarking via Trajectory-Aware Evaluation
title_zh: 基于轨迹感知的软件工程Agent低成本基准评估方法
authors:
- Kefeng Duan
- Dewu Zheng
- Yanlin Wang
- Xiwen Wang
- Ensheng Shi
- Xilin Liu
- Yuchi Ma
- Jiachi Chen
- Mingwei Liu
- Zibin Zheng
affiliations:
- Sun Yat-sen University
- Huawei Cloud Computing Technologies Co., Ltd.
- Zhejiang University
arxiv_id: '2609.01603'
url: https://arxiv.org/abs/2609.01603
pdf_url: https://arxiv.org/pdf/2609.01603
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent 低成本效能评估优化
tags:
- Agent Evaluation
- Item Response Theory
- LUPI
- Trajectory-aware
- SWE Agent
one_liner: 将SWE Agent历史执行轨迹作为特权信息融入IRT框架，大幅降低全基准评测的时间与经济成本
practical_value: '- 业务内部迭代多步Agent（如导购Agent、工单处理Agent）时，可参考仅用10%校准子集的评估方案，不用跑全量测试集就能得到可靠的版本排名，大幅降低评测成本

  - 多步交互类Agent的评测可复用结构化轨迹摘要设计，提取任务目标、探索上下文、执行操作、路径概览四类特征，补充二进制对错标签之外的过程信号

  - 可复用LUPI师生蒸馏范式：训练阶段用仅离线可获取的特权信息（如历史全轨迹）做监督，部署阶段只用新Agent少量测试结果就能预测全量表现，适配快速迭代场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
SWE Agent全基准评测成本极高，例如SWE-bench全量跑一次GPT-4 Turbo驱动的SWE-agent成本超8000美元，现有基于IRT的低成本评测方法仅用到最终对错结果，丢弃了执行轨迹中的大量过程信号，导致低预算下得分与排名预测准确率不足。

### 方法关键点
- 提出PTA-IRT三阶段框架：①轨迹表征：将多步执行日志压缩为结构化摘要，包含任务目标、探索上下文、执行编辑、路径概览4个字段，保留二进制标签缺失的过程信息；②校准子集选择：拟合轨迹感知的4PL IRT模型，用加权Fisher信息得分筛选任务，按难度分层分配预算保证子集代表性；③能力估计：采用LUPI师生蒸馏范式，训练阶段教师模型使用轨迹特权信息，部署阶段学生模型仅用新Agent在校准子集上的对错结果即可预测全基准表现。

### 关键结果
在4个SWE-bench数据集（Lite/Verified/Full/Pro）上对比7种经典IRT基线，10%校准预算下PTA-IRT平均MAE低至0.041，Kendall's τ达0.888，Spearman's ρ达0.973，全面优于所有基线；仅5%预算下Kendall's τ就达到0.768，满足实用要求。

### 核心结论
多步交互Agent的评测中，过程轨迹信号比单纯的对错结果能提供多得多的信息量，用特权信息蒸馏可以在不增加线上评测成本的前提下大幅提升低成本评估的准确性。
