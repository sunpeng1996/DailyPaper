---
title: 'RISE: Adaptive Imagination for World Action Models'
title_zh: RISE：面向世界动作模型的自适应想象框架
authors:
- Hongbo Lu
- Liang Yao
- Chenghao He
- Hao Han
- Fan Liu
- Wenlong Liao
- Tao He
- Pai Peng
affiliations:
- COWARobot Co. Ltd
- Shanghai Jiao Tong University
- Hohai University
arxiv_id: '2608.20430'
url: https://arxiv.org/abs/2608.20430
pdf_url: https://arxiv.org/pdf/2608.20430
published: '2026-08-19'
collected: '2026-08-25'
category: Agent
direction: Agent世界模型 · 自适应计算调度
tags:
- World Action Model
- Adaptive Computation
- Counterfactual Dataset
- Autonomous Driving
- Planning
one_liner: 提出可插拔自适应想象框架与反事实驾驶数据集，平衡世界动作模型的规划性能与推理开销
practical_value: '- 自适应调度思路可迁移到生成式推荐推理优化：简单请求/低不确定性用户走短路径召回排序，高不确定性场景（新用户、模糊query）才调用高成本LLM/RAG模块，平衡效果与时延

  - 反事实数据集构建思路可复用：基于电商真实点击流生成不同曝光组合的反事实转化样本，补充小流量/负向体验场景的训练数据，提升风险识别能力

  - 可插拔模块设计降低落地成本：无需改造原有推荐/Agent模型主干，仅新增轻量收益评估+门控模块即可实现自适应计算，改造成本低兼容性强'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有世界动作模型（WAM）对所有场景分配固定的未来推演预算，简单场景推演冗余增加时延，复杂场景推演不足影响决策质量；同时真实日志仅记录已发生的单一未来，缺乏安全关键场景的监督信号，限制模型风险感知能力。

### 方法关键点
- 新增轻量自适应调度器：Latent Evaluator评估当前推演前缀的风险与继续推演的未来规划收益，Rollout Gate权衡收益与计算成本，逐步做出继续/停止决策，实现场景自适应的推演深度
- 构建CounterDrive反事实数据集：基于真实驾驶场景生成不同风险等级的反事实未来，经人工校验标注轨迹有效性、事件发生时间、因果类别，补充风险场景监督信号
- 三阶段训练范式：先训练基础WAM的预测器与可变前缀规划器，再训练评估模块的风险与规划增益评估能力，最后训练门控模块的成本感知停止策略

### 关键实验结果
在NAVSIM v1/v2、nuScenes自动驾驶基准测试，对比SOTA WAM基线：NAVSIM v1 PDMS达91.5，超基线0.8个点；v2 EPDMS达90.8，超基线0.9个点；nuScenes平均轨迹L2误差0.31m、碰撞率0.10，均为最优；平均仅需2.4次推演，时延287ms，优于固定/随机推演策略；调度器可直接迁移到其他WAM架构，无需修改主干即可提升PDMS 1.2个点。

**最值得记住的一句话**：没有普适的固定计算预算，自适应分配算力到高收益场景是兼顾效果与效率的核心路径
