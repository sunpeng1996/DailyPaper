---
title: 'Decoupled Predictive Decision Making: A Shared Conditional Predictor for Agents'
title_zh: 解耦式预测决策框架：面向Agent的共享条件预测器
authors:
- Lang Mo
- Xingxuan Zhang
- Qi Wang
- Mingchao Hao
- Hao Yuan
- Chunjing Gan
- Wang Lu
- Peng Cui
affiliations:
- Stable AI
- Tsinghua University
arxiv_id: '2611.02075'
url: https://arxiv.org/abs/2611.02075
pdf_url: https://arxiv.org/pdf/2611.02075
published: '2026-10-31'
collected: '2026-11-06'
category: Agent
direction: Agent决策架构 · 语义与推理解耦
tags:
- Agent
- Decision Making
- Conditional Prediction
- Decoupled Architecture
- LLM
one_liner: 将Agent决策拆为语义编码与共享条件预测模块，多任务决策准确率与效率双提升
practical_value: '- 可复用这套解耦架构，把LLM仅作为语义编码器，历史经验推理交给结构化数据预训练的通用预测器，无需微调LLM即可快速适配业务决策任务（如搜索推荐候选排序、工具调用决策）

  - 历史数据无需拼接进LLM上下文，直接喂给条件预测器，实测全链路GPU耗时比缓存few-shot方案低80.3%，适合高QPS线上业务

  - 针对不平衡数据集（如电商低转化样本少的场景），架构比few-shot prompting的平衡准确率高14.51%，可显著缓解多数类偏置问题

  - 新增业务反馈仅需要更新历史数据集，不需要重新训练模型，迭代效率远高于微调方案，适合快速迭代的电商/广告场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent架构将语义理解、经验推理、答案生成耦合在同一LLM内，经验学习能力无法独立优化；few-shot prompting受上下文窗口限制、样本利用率低、易受类别偏置影响，且需频繁微调模型适配新任务，成本高迭代慢。

### 方法关键点
- DPDM解耦架构将Agent决策拆为三个独立可替换模块：1）冻结LLM作为语义编码器，将当前任务上下文、候选、历史记录统一编码为特征；2）预训练的结构化数据通用条件预测器LimiX-2，基于编码后的历史特征和标签预测当前任务目标概率；3）决策规则将概率映射为最终选择
- 全程无需微调LLM和条件预测器权重，新增反馈仅更新输入的历史数据集即可自动适配新任务
- 支持任意语义编码器接入，共享同一个条件预测器权重

### 关键实验
覆盖5类任务共50个基准数据集，对比baseline为同参数LLM的few-shot/zero-shot prompting、Jev API服务：
搭配Qwen3.5-27B语义编码器时，DPDM平均准确率达84.92%，较few-shot prompting的78.80%提升6.12个百分点；工具调用任务ToolPRMBench BFCL绝对准确率提升34.26%；相同历史输入条件下，不平衡数据集平均平衡准确率较few-shot提升14.51%；全链路GPU耗时仅为缓存few-shot prompting的19.7%。

### 核心结论
Agent的经验学习能力可以独立于语义理解能力作为单独的基础模型能力优化，解耦架构能同时兼顾语义适配性、经验推理效率和迭代速度。
