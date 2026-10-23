---
title: 'MMedAgent-Plus: Scaling Multimodal Medical Agents across Modalities, Tasks
  and Workflows'
title_zh: MMedAgent-Plus：跨模态跨任务跨工作流的可扩展多模态医疗Agent
authors:
- Ruoxin Wang
- Yuanting Pan
- Binxu Li
- Ruiyang Ji
- Yaqian Chen
- Jiayuan Ding
- Qifan Wang
- Lifu Huang
- Mingjie Li
- Yu Zhang
affiliations:
- Duke University
- Stanford University
- Yale University
- Princeton University
- Virginia Tech
arxiv_id: '2610.27233'
url: https://arxiv.org/abs/2610.27233
pdf_url: https://arxiv.org/pdf/2610.27233
published: '2026-10-18'
collected: '2026-10-23'
category: Agent
direction: 多模态Agent · 工具编排与工作流优化
tags:
- Multimodal Agent
- Tool Orchestration
- Instruction Tuning
- Workflow Optimization
- LLM Planner
one_liner: 提出融合视觉语言规划器与18个专家模型的多模态医疗Agent，实现多任务工作流自动编排
practical_value: '- 多工具统一接口设计可直接复用：给召回/排序/内容生成等异构业务模型封装统一入参出参格式，大幅降低Agent调度复杂度

  - 指令调优范式可迁移：针对业务工具调用场景构造万级标注样本做LoRA微调，可显著提升工具选择、流程编排准确率

  - 分层评估框架可复用：拆解工具选择、结果合成、端到端执行三个维度分别评估，便于快速定位Agent全链路瓶颈'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有医疗AI中，单任务专家模型泛化性差，通用多模态模型精度不足，两类模型均无法自动编排存在依赖关系的多步骤工作流，难以适配复杂医疗场景需求。
### 方法关键点
1. 采用分层架构：上层为视觉语言规划器，下层封装18个各任务SOTA专家模型，覆盖12类任务、8种模态，所有工具统一入参出参接口；
2. 规划器基于32个公开医疗基准的20.9万条样本做指令微调，覆盖单/多工具、单/多轮全场景工具调用模式；
3. 规划器自动决策工具调用顺序、传递中间结果，最终基于工具输出合成高可信响应。
### 关键结果数字
单工具多轮、多工具多轮、多工具单轮场景工具调用准确率分别达91.0%、98.1%、80.7%；输出的忠实度、完整度、简洁度得分达14.4-14.8/15；端到端执行场景工具调用准确率90.6%，最终答案准确率0.98，持平单任务SOTA专家模型，远超基线的0.28。
