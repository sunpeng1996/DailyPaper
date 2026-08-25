---
title: 'ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and
  Frozen Workplace-Style Holdouts'
title_zh: ClawProBench：基于轨迹的AI Agent运行时覆盖与冻结工作场景评测基准
authors:
- YuanHang Xiao
affiliations:
- The Chinese University of Hong Kong
arxiv_id: '2608.22510'
url: https://arxiv.org/abs/2608.22510
pdf_url: https://arxiv.org/pdf/2608.22510
published: '2026-08-22'
collected: '2026-08-25'
category: Agent
direction: Agent评测 · 轨迹感知 运行时配置诊断
tags:
- Agent-Evaluation
- Runtime-Diagnosis
- Trace-Aware
- Benchmark
- Reliability-Assessment
one_liner: 推出结合轨迹评分、运行时覆盖、冻结场景的Agent完整配置联合诊断评测基准
practical_value: '- 做电商/运营类业务Agent内部评测时，不要仅看最终任务成功率，可复用论文的三维加权评分公式：0.65*正确性 + 0.35*流程合规性
  + 效率惩罚 + 安全门控，避免违规操作、冗余调用的Agent拿到高分。

  - 跨Agent框架/版本迭代对比效果时，可复用冻结holdout协议：锁死任务契约、输入输出、评分接口，排除场景漂移干扰，准确度量迭代的真实收益。

  - 上线前稳定性测试不要只测单次pass@1，至少测3次重复实验的严格通过率：论文数据显示单次通过率0.66的场景，三次全过的稳定通过率仅0.289，单次结果会严重高估上线稳定性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent评测大多只聚焦最终任务成功率，忽略运行时配置差异、执行流程合规性、重复调用可靠性、安全风险等维度，导致评测结果和上线实际表现差距大，也无法定位失败根因，无法支撑配置级的诊断优化。

### 方法关键点
- 双赛道场景设计：102个全场景覆盖66个通用工作任务+36个OpenClaw原生运行时任务，包含约束、恢复、规划、安全、合成、工具6大能力维度；额外提供68个冻结工作场景holdout，锁死任务契约、输入输出、评分接口，用于固定条件下的可靠性和跨运行时对比。
- 轨迹感知评分机制：得分公式为 `S = G_safety * (0.65C + 0.35P) * (1-E)`，其中C为正确性得分、P为流程质量得分（权重上限0.35，避免过度限制实现路径）、E为冗余调用效率惩罚、G_safety为安全门控，严重违规直接判零分。
- 跨运行时适配协议：定义标准化的场景映射、状态隔离、轨迹归一、评分接口层，支持OpenClaw、IronClaw、NanoClaw等多框架的同基准对比。

### 关键实验
在68个holdout场景评测37组Agent配置，单次pass@k-any为0.6638，三次重复实验全过的严格通过率仅0.2890；相同模型在不同版本OpenClaw上得分波动可达0.052，不同运行时框架上得分波动可达0.0716，严格通过率波动可达19.1个百分点；全场景与holdout场景的模型排序斯皮尔曼相关系数仅0.1754，95%置信区间跨零点，无法得到稳定的模型排序。

### 核心结论
Agent的评测对象是「模型+运行时+策略」的完整配置，而非孤立的模型本身，仅看最终答案的排名会掩盖运行时敏感性、单次成功的不可靠性、流程违规等问题。
