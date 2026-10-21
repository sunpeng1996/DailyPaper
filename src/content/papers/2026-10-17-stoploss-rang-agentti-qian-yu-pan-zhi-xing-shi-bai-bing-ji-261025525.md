---
title: 'StopLoss: Teaching Agents to Predict Failure and Stop Early'
title_zh: StopLoss：让Agent提前预判执行失败并及时中止
authors:
- Jiarong Liang
- Xueguang Ma
- Dongfu Jiang
- Yuxuan Zhang
- Ping Nie
- Wenhu Chen
affiliations:
- University of Waterloo
arxiv_id: '2610.25525'
url: https://arxiv.org/abs/2610.25525
pdf_url: https://arxiv.org/pdf/2610.25525
published: '2026-10-17'
collected: '2026-10-21'
category: Agent
direction: Agent 执行失败预判 轻量化外置监控
tags:
- Agent
- Early Stopping
- Failure Prediction
- LoRA
- Cost Optimization
one_liner: 用7B-8B小模型做外置低开销监控，实现Agent执行失败提前预判，成本比通用Judge低1-2个数量级
practical_value: '- 可复用「小模型+LoRA微调做外置监控」的架构，无需修改原有Agent逻辑，适合电商导购Agent、广告投放Agent的无效执行提前中止，算力开销极低

  - 可借鉴outcome弱监督方案：用最终执行成败回标中间窗口数据，不需要人工标注中间阶段的失败信号，大幅降低训练数据成本

  - 成本核算逻辑可直接套用到推荐系统场景：监控ROI需要满足「避免的执行成本 > 监控开销 + 误杀成功任务的损失」，可用于多轮召回、重排序的early stopping决策

  - 阈值校准方法可复用：在成功轨迹上校准阈值控制误杀率，适合对推荐/广告准确率有硬性要求的业务场景，平衡成本和效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent执行时普遍会在注定失败的任务上消耗大量算力资源：基于预算的中止策略容易误杀本可成功的任务，调用通用大模型做判官监控的开销极高，往往超过节省的执行成本，亟需兼顾低开销、低误杀、高实用性的失败预判方案。
### 方法关键点
- 离线训练：用已完成的Agent全轨迹+最终验证结果回标每个中间窗口，失败轨迹所有窗口标ABORT，成功轨迹最后两步标DELIVER、其余标CONTINUE；对7B-8B级开源模型做LoRA微调，仅计算目标答案token的损失，无需访问Agent内部状态
- 在线推理：在固定步数（5、8、11…）执行检查，仅输入最近3步的动作+观测序列，直接从输出logit计算失败概率，多模型集成取平均；阈值在成功轨迹集上校准，控制目标误杀率，超过阈值即中止执行，全程不修改原有Agent执行逻辑
### 关键结果
在SWE-bench Verified、SWE-bench Pro两个代码Agent基准上，对比6款同系列通用大模型判官：
- 单步检查成本仅$0.00024，比通用大模型判官低1-2个数量级
- 在Verified数据集上保留99%的成功任务，单任务成本降低4.5%；在Pro高成本子集上搭配Qwen3-8B backbone最高降低48%的单任务成本，所有测试场景下成本均低于通用大模型判官方案
### 核心结论
光有好的失败排序精度不足以产生业务价值，必须满足「避免的执行成本 > 监控开销 + 误杀成功任务的损失」，早期中止策略才能真正划算
