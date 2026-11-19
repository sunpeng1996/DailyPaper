---
title: 'Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent
  Workflow'
title_zh: AnyS1：适配任意Agent工作流的通用快速决策系统（System-1）
authors:
- Rui Li
- Liyang He
- Zheng Zhang
- Zhenya Huang
- Qi Liu
affiliations:
- University of Science and Technology of China
- Nanyang Technological University
arxiv_id: '2611.23751'
url: https://arxiv.org/abs/2611.23751
pdf_url: https://arxiv.org/pdf/2611.23751
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent双系统执行优化
tags:
- DualSystemAgent
- System1
- AgentWorkflow
- CostOptimization
- ConfidenceCalibration
one_liner: 从公开Agent技能自动挖掘决策点，训练通用4B System-1，降本75%+且不损失任务成功率
practical_value: '- 电商/广告领域的流程类Agent任务（如客服SOP执行、投放规则判断）可先将节点拆分为D（确定性执行）、E（枚举选择）、G（开放生成）三类，将占比60%+的E节点用小模型承接，可实现75%+的推理成本下降，延迟最高降92%

  - 训练枚举类选择小模型时，优先采用真实容器运行产生的轨迹上下文作为训练数据，相比LLM生成的合成数据，跨场景准确率可提升18.8个百分点，避免合成数据与真实runtime上下文的分布差

  - 小模型训练加入label smoothing可大幅提升置信度校准效果，冷启动场景可直接复用全局置信度阈值，无需目标场景标注数据即可上线，仅需50轮无标注运行数据校准后即可达到最优降本效果

  - 多业务线共用Agent的场景可统一抽象决策点范式，训练通用System-1覆盖所有业务的选择类节点，无需为每个工作流单独开发小模型，大幅降低重复开发成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent每一步均调用大模型（System-2）执行，推理成本与延迟随流程长度快速上涨；而工作流中超过60%的中间节点仅需在有限候选中做选择，完全可由轻量模型承接。现有双系统Agent需为每个工作流手动预埋决策点钩子，无法跨场景通用，无法适配Agent动态加载技能的使用范式。

### 方法关键点
- 离线流程：从1072个公开Agent技能中自动挖掘可枚举决策点，在隔离容器中执行合成任务收集真实运行状态，构造包含25986条共识标注样本的Any-DP数据集，避免LLM合成数据与真实上下文的分布差异
- 模型设计：基于Qwen3.5-4B基座加位置无关指针头，训练时加入label smoothing保证置信度校准，单轮前向即可输出选项概率分布
- 运行时策略：将工作流节点分为三类：D节点（确定性逻辑，直接跑代码）、E节点（枚举选择，System-1判断，置信度低于阈值则fallback到System-2）、G节点（开放生成，直接走System-2）；支持冷启动全局阈值（AnyS1cold）和50轮无标注数据校准阈值（AnyS1warm）两种模式

### 关键结果
在3个无重叠训练数据的Agent基准（SOPBench、ALFWorld、WebShop）上，分别搭配DeepSeek-V4.1-Flash和GPT-6 Sol作为System-2验证：
- AnyS1warm相比纯System-2 Agent，单轮成本下降75%~91%，模型调用耗时下降63%~92%，任务成功率完全持平
- 冷启动版本AnyS1cold无需目标场景任何运行数据，成本下降81%~87%，成功率仅损失0.8个百分点以内
- 消融实验证明：真实运行状态训练比LLM合成数据准确率高18.8pt，label smoothing比硬交叉熵的跨场景一致率高5.3pt

### 最值得记住的结论
Agent工作流中多数节点为低复杂度枚举选择节点，通过通用轻量System-1承接+置信度fallback的双系统架构，可在几乎不损失效果的前提下将推理成本压缩至原有的1/10量级
