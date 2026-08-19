---
title: 'From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents'
title_zh: 从序列到结构：面向LLM Agent的关系不确定性传播框架
authors:
- Zhengzhao Ma. Boxi Cao
- Yaojie Lu
- Hongyu Lin
- Xianpei Han
- Le Sun
affiliations:
- Chinese Academy of Sciences, Institute of Software
- University of Chinese Academy of Sciences
arxiv_id: '2608.16002'
url: https://arxiv.org/abs/2608.16002
pdf_url: https://arxiv.org/pdf/2608.16002
published: '2026-08-16'
collected: '2026-08-19'
category: Agent
direction: Agent 可靠性 · 不确定性量化
tags:
- LLM Agent
- Uncertainty Quantification
- Trajectory Modeling
- Graph Propagation
- Failure Detection
one_liner: 提出基于轨迹依赖图的关系不确定性传播框架RUPA，显著提升长时序LLM Agent的不确定性量化效果
practical_value: '- 电商导购Agent、多轮推荐场景可直接复用RUPA的轨迹图建模方法，将用户点击、query改写、推荐结果、反馈作为节点建模依赖，提前识别用户流失、任务失败风险

  - 不确定性引导的多候选动作选择逻辑可迁移到多轮推荐候选排序环节，每步选择风险最低的推荐策略，提升大促多轮触达、复杂导购等场景的任务成功率

  - 工程上可直接复用论文给出的7种关系权重默认配置（反馈、重复行为权重更高），无需复杂标注训练即可适配业务交互轨迹，大幅降低UQ模块上线成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent的UQ方法大多基于局部token概率、单步置信度，或把轨迹当成线性序列处理，忽略长交互过程中错误跨步骤依赖传播的问题，无法提前识别早期步骤错误引发的后续失败，严重制约长时序Agent在电商导购、任务型推荐等场景的落地可靠性。

### 方法关键点
- 轨迹图建模：将Agent执行历史转换为有向依赖图，节点覆盖用户指令、推理状态、工具调用、环境反馈，边对应7种核心依赖关系（时序、最新指令、重复行为、推理延续、并行分支、反馈、目标对齐）
- 关系感知不确定性传播：为不同关系边配置差异化权重（重复行为、反馈关系权重更高），沿依赖路径传播历史不确定性，叠加指数衰减动量项保留长时序风险趋势
- 置信度融合：结合当前节点局部不确定性（预测熵、工具调用错误信号）与传播得到的历史结构风险，输出轨迹级风险评分

### 关键实验结果
在τ-2、Terminal-Bench-2、GAIA三个Agent基准，6款26B~230B开源LLM上测试，对比5种主流UQ方法：平均AUROC比最优基线提升2~4.8个百分点，其中MiniMax-M2.7上从0.694提升至0.718；仅观察30%轨迹前缀时AUROC比基线高5~10个百分点，可更早识别失败风险；用于不确定性引导的动作选择时，任务成功率较随机选择最高提升10.8个百分点。

### 核心结论
LLM Agent的不确定性本质是轨迹级结构属性，而非独立单步置信度的线性叠加，显式建模跨步骤依赖才能实现可靠的风险预判。
