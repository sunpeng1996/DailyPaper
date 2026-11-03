---
title: 'SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training'
title_zh: SWE-Trail：面向编码Agent训练的历史引导轨迹收集框架
authors:
- Ziming Li
- Lu Yu
- Jiatan Huang
- Qing Cui
- Jun Zhou
- Chuxu Zhang
affiliations:
- University of Connecticut
- Ant Group
arxiv_id: '2611.02074'
url: https://arxiv.org/abs/2611.02074
pdf_url: https://arxiv.org/pdf/2611.02074
published: '2026-10-31'
collected: '2026-11-03'
category: Agent
direction: Agent训练 · 轨迹采集优化
tags:
- Coding Agent
- Trajectory Collection
- LLM Training
- History Guidance
- SWE-bench
one_liner: 仅用历史引导轨迹采集节点不暴露给Agent，提升编码Agent下游任务表现
practical_value: '- 训练Agent轨迹数据时，不要把引导历史直接放进Agent上下文，避免训练测试分布不一致导致效果下降，可复用在导购、决策类推荐Agent的训练数据生产环节

  - 可复用历史轨迹的决策分歧点、重复失败模式作为新轨迹的采集干预节点，无需修改Agent本身的输入逻辑，即可提升训练数据质量

  - 轨迹采集的收益不单纯看采集到的成功轨迹数量，轨迹的过程合理性对下游模型效果影响更大，可参考优化推荐、广告场景的样本筛选规则

  - 历史引导采集和事后轨迹筛选可互补，先优化采集过程再做筛选，比单纯增加独立采样数量的ROI更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent训练轨迹多采用独立采样，随采样量增加冗余度快速上升；若直接把历史轨迹作为提示输入Agent生成新轨迹，会导致训练时存在测试时没有的辅助信息，出现分布偏移，反而降低下游性能。

### 方法关键点
- 分两阶段设计，离线阶段先基于历史轨迹编译检测器规则，识别需要额外采集的决策状态（如混合成败历史的分歧点、全失败历史的重复错误模式），全程不把历史暴露给Agent
- 在线阶段当Agent执行到检测器命中的状态时，从Agent普通上下文生成多个候选下一步动作，并行执行短horizon后基于仓库证据选最优路径继续，最终只保留选中路径作为训练轨迹
- 不同历史类型采用不同采样温度：混合/全失败历史用更高温度鼓励动作多样性

### 关键实验
用300个SWE-rebench V2问题采集轨迹，训练124B Ling-3.0-flash-base模型，对比独立采样基线，SWE-Trail在SWE-bench Multilingual提升2.33个百分点，SWE-bench Pro提升1.60个百分点；仅用采集流程不加历史的对照组只提升0.11个百分点，验证历史引导的收益；Qwen3-14B上也分别提升3.11、2.42个百分点，效果跨模型通用。

### 核心结论
历史轨迹的价值不止于本身的内容，更适合用来引导新轨迹的采集位置，而非直接作为Agent的输入提示
