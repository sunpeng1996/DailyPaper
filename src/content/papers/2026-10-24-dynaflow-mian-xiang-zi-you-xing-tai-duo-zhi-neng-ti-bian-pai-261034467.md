---
title: 'DynaFlow: Learning Free-Form Multi-Agent Orchestration'
title_zh: DynaFlow：面向自由形态多智能体编排的学习框架
authors:
- Ruhao Liu
- Qi Li
- Shizun Wang
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2610.34467'
url: https://arxiv.org/abs/2610.34467
pdf_url: https://arxiv.org/pdf/2610.34467
published: '2026-10-24'
collected: '2026-10-27'
category: MultiAgent
direction: 多智能体 · 自适应工作流编排
tags:
- Multi-Agent Orchestration
- Workflow Synthesis
- LLM Agent
- SFT
- Dynamic Collaboration
one_liner: 将自由格式可执行工作流合成纳入主Agent动作空间，仅训练主Agent实现自适应多智体协作，性能超基线10.9个百分点
practical_value: '- 多Agent系统架构可复用「仅训练主编排Agent、子Agent全冻结」范式，无需重训各领域子Agent即可迭代调度能力，大幅降低电商导购、客服等多Agent系统的训练成本

  - 两阶段SFT训练思路可直接迁移：先蒸馏正确回答轨迹做初步微调，再过滤存在前提注入、验证偏差、信息流缺陷的样本做二次微调，适合推荐多源召回结果编排、营销活动多Agent协同等调度类任务

  - Dynamic路由机制可落地：给主Agent增加「是否需要调用协作」的判断分支，简单任务直接响应、复杂任务才调用多Agent，可降低约40%的算力消耗，适合电商咨询、搜索query理解等场景

  - 工作流缺陷排查的三个维度（前提注入、验证偏差、信息流缺陷）可直接作为多Agent系统bad case诊断标准，快速定位调度层面的问题'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体系统依赖预定义协作结构，无法适配不同任务的动态协作需求，要么过度调用导致算力浪费、延迟升高，要么协作不足导致效果不达预期；且多数方案需要同时训练所有智能体，训练成本高、子能力复用性差。

### 方法关键点
- 扩展主Agent动作空间为三类：直接回答、普通工具调用、生成JavaScript格式的自由形态工作流；工作流支持自定义子Agent角色、串行/并行依赖、中间结果传递与验证逻辑，执行后返回结果和trace供主Agent迭代决策
- 完全解耦编排能力与子Agent执行能力，仅训练主Agent，所有子Agent保持冻结，可直接复用任意预训练子Agent
- 两阶段SFT训练：第一阶段用教师模型蒸馏的正确回答轨迹做初步微调；第二阶段过滤掉存在前提注入、验证偏差、信息流缺陷的低质量样本，用筛选后的高质量数据进一步强化编排能力
- 支持两种执行模式：Dynamic模式主Agent自主判断是否需要调用工作流，Forced模式强制先调用工作流再处理任务

### 关键实验结果
在6个基准数据集（AIME数学竞赛、PolyMATH多语言数学、GPQA-D科学问答、HotpotQA多跳检索）共688个问题上测试，所有模型统一使用Qwen3.5-27B backbone：
- Forced模式下DynaFlow整体准确率达88.08%，比最强基线AFlow高10.9个百分点，比未训练的Base主Agent高12.21个百分点
- Dynamic模式下准确率达87.94%，与Forced模式几乎持平，同时47.1%的简单问题直接回答无需调用工作流，平均调用子Agent数量减少41%

### 核心结论
多智能体协作的核心增益不仅来自任务拆分，更来自跨阶段的可靠信息流传递与验证，仅优化编排调度层即可在不提升子Agent能力的前提下大幅提升系统整体性能
