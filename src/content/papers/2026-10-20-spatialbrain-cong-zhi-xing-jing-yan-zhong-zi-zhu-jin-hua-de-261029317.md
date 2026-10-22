---
title: 'SpatialBrain: Spatial Intelligence Growing from Experience'
title_zh: SpatialBrain：从执行经验中自主进化的空间推理Agent框架
authors:
- Yifan Zhou
- Ziyang Gong
- Xiaojun Ye
- Yifei Liu
- Donggang Li
- Xiaolong Zhou
- Zhihang Zhong
- Xue Yang
affiliations:
- Shanghai Jiao Tong University
- Zhejiang University
arxiv_id: '2610.29317'
url: https://arxiv.org/abs/2610.29317
pdf_url: https://arxiv.org/pdf/2610.29317
published: '2026-10-20'
collected: '2026-10-22'
category: Agent
direction: Agent 空间推理 · 无标注自进化
tags:
- Spatial Reasoning
- Agent Self-evolution
- 3D Fusion Memory
- Skill Library
- Multimodal Agent
one_liner: 冻结多模态基座权重，通过分离场景记忆、可复用技能、经验决策实现空间推理Agent无标注自进化
practical_value: '- 可复用「冻结基座权重+外置经验/技能库」的自进化架构，无需频繁微调大模型，大幅降低多模态导购、AR推荐等场景的Agent迭代成本

  - 3DFusionMemory的多视图空间信息融合方案可迁移到家装电商户型-商品匹配、线下商场AR导购的3D场景用户行为建模任务

  - 任务特征匹配+历史经验的工具调用决策逻辑，可优化现有推荐/搜索Query多模态理解Agent的工具调用准确率，减少冗余调用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有空间推理方案存在明显缺陷：全场景重建会带来高额成本与噪声干扰，直接生成答案容易遗漏多视图关联信息；已有的Agent记忆/技能方案无法区分场景专属证据和通用推理经验，跨任务泛化能力差，且依赖基座微调，落地成本高。

### 方法关键点
- 完全冻结视觉语言基座权重，拆分三层独立核心模块：3DFusionMemory融合多视图观测生成可查询的场景空间关系图，每个任务单独重建不跨场景留存；Spatial Skill Library存储参数化通用空间计算流程（如坐标变换、相对位置计算），支持跨场景复用；Spatial Cognition基于历史执行经验匹配任务特征，决策当前采用直接推理、工具调用还是记忆查询，无需标注数据。
- 无标注自进化机制：任务完成后抽象出不带场景坐标、不带参考答案的执行轨迹记录，仅更新策略经验库和技能可用状态，不修改任何模型权重。

### 关键实验
在MMSI、MindCube等5个主流空间推理基准测试，对比同基座GPT-5.6-sol直接回答效果，4个基准精度提升、1个打平，平均精度从67.5%提升到72.6%，其中MindCube基准提升达20.4个百分点；消融实验显示移除技能库、3DFusionMemory、经验决策模块后，精度分别下降10.9、12.4、8.8个百分点。

**最值得记住的一句话**：Agent能力进化不依赖基座微调，分离场景专属证据、通用可复用技能、经验决策逻辑的外置架构，可实现无标注的测试态自进化。
