---
title: 'CARE-3D: Reinforcement Learning for Evidence Grounded Agentic Reasoning in
  Situated 3D Scenes'
title_zh: CARE-3D：面向3D场景证据落地推理的强化学习框架
authors:
- Xiaoqian Hu
- Ruihong Qiu
- Yanran Tang
- Sen Wang
affiliations:
- The University of Queensland
arxiv_id: '2611.29969'
url: https://arxiv.org/abs/2611.29969
pdf_url: https://arxiv.org/pdf/2611.29969
published: '2026-11-22'
collected: '2026-11-27'
category: Agent
direction: 具身智能体 · 3D场景推理优化
tags:
- EmbodiedAgent
- GRPO
- CreditAssignment
- ToolUse
- 3DVision
- ReinforcementLearning
one_liner: 提出融合反事实证据归因与工具覆盖采样的GRPO强化后训练框架，提升3D智能体推理证据一致性
practical_value: '- 反事实证据归因（CARE）的信用分配思路可直接迁移到搜索/推荐/导购Agent的工具调用优化：当Agent调用召回、用户画像、库存查询等工具时，通过mask工具返回结果前后的目标转化/正确答案概率差计算中间奖励，替代仅依赖最终转化的稀疏奖励，大幅提升工具调用的合理性

  - Group Coverage Sampling（GCS）的工具多样性保障方案可复用在多工具Agent训练中：在GRPO训练时补充低频次工具的采样样本并对工具标识做loss
  mask，避免冷门高价值工具被策略遗忘，适配电商场景下多工具（券计算、物流查询、尺码推荐等）的调用需求

  - 仅微调LoRA、冻结底层基座与工具模块的强化后训练范式可直接复用在业务Agent迭代中，不需要重训基座或工具逻辑，大幅降低训练成本与上线风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有3D场景具身推理方法依赖监督轨迹拟合，仅能模仿预设的证据获取模式，无法优化返回证据对答案的实际支撑度；仅用最终答案奖励的强化学习存在中间工具调用信用分配难、低频工具被低估的问题，导致模型常依赖文本先验而非实际场景证据输出答案，空间推理准确率与证据-答案一致性差。
### 方法关键点
- 两阶段训练范式：先通过SFT让智能体学会基本的3D接地工具调用与证据推理逻辑，强化后训练阶段冻结3D接地模块与基座模型，仅用GRPO微调LoRA参数
- 反事实证据归因（CARE）：对比工具返回证据被mask前后，标准答案的对数似然差得到证据增益，作为中间奖励分配给对应工具调用，解决证据效用的信用分配问题
- 组覆盖采样（GCS）：每个GRPO组除6个自由采样轨迹外，补充2个低频工具的覆盖采样轨迹，对工具标识做loss mask，避免低频高价值工具在训练中消失
### 关键实验
在MSQA、Beacon3D两个3D推理基准上测试，对比SFT、仅用答案+格式奖励的GRPO baseline：CARE-3D在Qwen3-VL-4B基座下MSQA整体得分提升7.6pp，Beacon3D对象级一致性得分提升4.5pp；跨4个不同基座均获得稳定增益，其中空间推理类任务最高提升10.8pp，SFT阶段的证据不敏感错误修复率达45.6%。
最值得记住的一句话：工具调用的奖励不能只看最终结果，反事实对比工具返回信息的贡献、保障低频次工具的探索度，能大幅提升智能体的推理可靠性与证据一致性
