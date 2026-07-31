---
title: 'Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes
  and Compute Tradeoffs'
title_zh: 重新思考本地计算机操作Agent的推理时缩放：失效模式与算力权衡
authors:
- Woongkyu Lee
- Jungwook Choi
affiliations:
- Hanyang University
arxiv_id: '2607.28573'
url: https://arxiv.org/abs/2607.28573
pdf_url: https://arxiv.org/pdf/2607.28573
published: '2026-07-30'
collected: '2026-07-31'
category: Agent
direction: 本地计算机操作Agent推理优化
tags:
- Computer-Use Agent
- Inference Scaling
- Local LLM
- Failure Mode Analysis
- Efficiency Optimization
one_liner: 系统分析本地计算机操作Agent四类推理时缩放的失效模式与算力收益权衡
practical_value: '- 做本地端Agent（如电商本地导购、私域运营Agent）时，上下文历史设为4轮左右最优，超过会出现收益饱和、假成功概率上升，还会额外增加token成本

  - 不要盲目给本地小模型Agent加大最大执行步长，推理能力不足的小模型加步长只会把失败从超时变成提前误判完成，不会提升成功率，反而线性增加成本

  - 小模型优先用单阶段Agent架构，两阶段规划-落地架构会额外引入格式解析、规划能力不足的失效，反而比单阶段效果差、成本高；必须用两阶段的话可搭配最多4路并行候选计划抵消部分损失

  - 所有推理时缩放策略不要均匀分配算力，要针对失效模式做选择性分配，比如检测到循环停滞时再加步长/并行计划，平时用基础配置即可'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
本地部署计算机操作Agent（CUA）在隐私保护、成本控制上优势显著，但现有推理时缩放技术均针对大模型设计，在资源受限的本地小模型上的收益边界、失效模式完全不明确，缺乏系统性的量化权衡依据，导致很多本地Agent优化方向投入产出比极低。

### 方法关键点
- 将推理时缩放拆分为4个独立维度：**contextual scaling**（历史上下文长度H）、**temporal scaling**（最大执行步长S）、**structural scaling**（单阶段端到端/两阶段规划-落地架构）、**parallel scaling**（候选计划并行数P）
- 效果指标用OSWorld任务成功率，成本指标用单任务平均步数、累计prompt token数，同时对所有失败案例做模式分类归因

### 关键实验
- 数据集：OSWorld基准的361个Ubuntu真实GUI任务，无辅助接口输入，仅靠截图感知环境
- 测试模型：Qwen3-VL-8B/30B、UI-TARS-1.5-7B、OpenCUA-7B
- 核心数字：H从0升至4时，单Agent成功率从18%提升至28.56%，H升至8时成功率降至27.16%同时token成本上升30%+；S从15升至100时成功率基本无提升，token成本线性上涨2倍；两阶段Agent比同配置单Agent成功率低5-8pct，token成本高40%以上；P从1升至4时两阶段成功率回升3-4pct，token成本翻2倍。

### 最值得记住的一句话
本地小模型Agent的推理时缩放大多只会转移失效模式，而不会提升成功率上限，性价比最高的方案是用中等上下文长度、限制步长的单阶段架构，仅在必要时触发并行缩放。
