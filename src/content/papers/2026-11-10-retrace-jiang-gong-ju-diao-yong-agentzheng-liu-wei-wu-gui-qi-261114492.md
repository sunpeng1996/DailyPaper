---
title: 'ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows'
title_zh: ReTrace：将工具调用Agent蒸馏为无规划器可执行工作流
authors:
- Kaiyuan Hou
- Yang Ping Kuo
- Indranil Bhattacharya
- Rohith Nama
- Arushi Gupta
- Carlos D. Castillo
- Prathap Ramachandra
- Xiaofan Jiang
- Francesco Carbone
affiliations:
- Columbia University
- Amazon
arxiv_id: '2611.14492'
url: https://arxiv.org/abs/2611.14492
pdf_url: https://arxiv.org/pdf/2611.14492
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 工具调用流程蒸馏优化
tags:
- Agent Distillation
- Workflow Automation
- LLM Agent
- Tool Calling
- SOP Execution
one_liner: 基于Agent运行轨迹与推理文本提取规则，生成无LLM规划的工作流，大幅降本提效
practical_value: '- 高并发固定SOP类Agent业务（如电商客服自动化、订单审核、售后处理），若执行次数超过75次，可通过该方案蒸馏为无规划器工作流，成本降24%、延迟降99%以上，ROI极高

  - 从Agent轨迹提取动作规则时，必须结合每步的推理文本，而非仅用工具调用记录，可提升6~8个点的流程准确率，还能覆盖历史轨迹未出现的分支

  - 不要给工作流生成器直接喂大量原始轨迹，超过阈值（τ2-bench>16条、生产数据>8条）会因上下文过长导致生成质量下降，建议先聚合成规则IR再输入

  - 生成的工作流可通过3轮训练失败样本修复，准确率可从66.7%提升至81.2%，甚至超过原始Agent效果，修复成本极低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM Agent可直接遵循自然语言SOP执行业务流程，但每步都需要调用LLM做路径规划，高并发场景下延迟和成本极高；手工开发固定工作流又需要大量研发人力，现有轨迹复用方案仍需运行时调用LLM选步骤，未解决根本问题。

### 方法关键点
- 输入为SOP+少量带推理文本的Agent成功运行轨迹，输出为无规划器可执行工作流，运行时无需LLM做步骤选择，仅工具内部可按需调用模型
- 构建分三步：1）提取：从每步推理文本抽动作触发条件、输入来源，从工具调用记录抽动作、参数；2）聚合：多轮轨迹规则合并为中间规则文档（IR），统一变量、补全推理提到但未出现在轨迹中的分支；3）合成：将IR翻译成对应平台的可执行代码/工作流图
- 支持3轮低成本修复：仅用训练集失败样例修改工作流代码，无需修改上层规则IR

### 关键实验结果
- 数据集：79个亚马逊生产业务流程、τ2-bench客服数据集、SOP-Bench工业SOP数据集
- 对比基线：原始Agent、少样本工作流生成、AWM记忆Agent、Skill Factory等
- 核心数字：生产场景流程完成率93.8%（原始Agent96.8%），单任务成本降24%；τ2-bench成功率75.8%，延迟从170s降至1.3s，3轮修复后成功率升至81.2%，超过原始Agent的80.6%；SOP-Bench修复后成功率87.8%，延迟从46.6s降至0.4s

> 最值得记住：执行频率高、逻辑相对固定的Agent业务，一次性蒸馏为无规划器工作流的成本，只要执行75次就能完全收回
