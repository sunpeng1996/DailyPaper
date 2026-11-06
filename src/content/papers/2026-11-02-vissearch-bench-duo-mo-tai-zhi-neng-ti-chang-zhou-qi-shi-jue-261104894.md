---
title: 'VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents'
title_zh: VisSearch-Bench：多模态智能体长周期视觉搜索评估基准
authors:
- ZhengXian Wu
- Qianhao Nie
- Zhuohong Chen
- Junjie Gao
- Yuyao Zhang
- Yunyao Yu
- Hangrui Xu
- Cheng Cheng
- Guiyu Ma
- Jin Zhang
affiliations:
- Tsinghua University
- Ant Group
- Renmin University of China
arxiv_id: '2611.04894'
url: https://arxiv.org/abs/2611.04894
pdf_url: https://arxiv.org/pdf/2611.04894
published: '2026-11-02'
collected: '2026-11-06'
category: Agent
direction: 多模态Agent · 视觉搜索能力评估
tags:
- Multimodal Agent
- Visual Search
- Benchmark
- Long-horizon Reasoning
- Tool Use
one_liner: 构建覆盖5类长周期视觉搜索任务的人工标注基准，评估多模态Agent的视觉上下文管理能力
practical_value: '- 做电商以图搜货/多模态导购Agent时，可复用5类任务划分逻辑（集合/序列/宽深/消歧/结构引导）设计业务场景测试用例，覆盖跨步骤视觉信息关联、相似款消歧等核心需求

  - 多模态Agent工程实现中，优先给ReAct框架配原生图像查看+裁剪工具，比仅用图像生成描述的模式在视觉密集型任务上准确率平均高3~7个百分点

  - 长周期多步视觉搜索任务的评估可复用「最终准确率+过程分」双指标体系，既能衡量整体任务完成度，也能定位单步错误的瓶颈

  - 电商同款识别/相似款召回场景，可参考Competitive Visual Disambiguation的任务设计思路，强制模型依赖视觉细节而非文本标签判断，降低文本shortcuts带来的badcase'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态搜索基准多仅要求某一步使用视觉信息，无法衡量Agent跨搜索步骤关联视觉证据、管理视觉上下文的能力；真实场景中（如电商以图搜货、文旅信息查询）需要Agent在多轮搜索中持续整合视觉信息、过滤候选、关联外部事实，现有基准无法覆盖这类长周期视觉搜索需求。

### 方法关键点
- 基准包含204条人工标注任务，覆盖7个主领域25个子领域，分为5类任务：集合式视觉搜索、序列式视觉搜索、混合宽深搜索、竞争性视觉消歧、视觉结构引导搜索
- 构建流程严格遵循视觉不可替代性、视觉证据可整合、公开可溯源三大原则，每条任务附带可追溯证据、参考答案、评分规则
- 采用双指标评估：Accuracy衡量最终答案完全正确的比例，Process Score衡量子问题/中间状态的正确率和完整度

### 关键结果
- 测试16个主流多模态模型：无工具直接回答的准确率最高仅6.37%；搭配ReAct框架后最优的ReAct+Kimi-K3准确率26.47%，ReAct+GPT-5.5过程分最高49.52%
- 搭配搜索工具后，模型准确率平均提升10~20个百分点，其中视觉消歧类任务无工具时准确率为0，搭配工具后最高可达44.12%
- 仅用图像生成描述的模式会丢失关键视觉细节，比原生查看图像的模式准确率低1~3个百分点

**最值得记住的一句话：** 即使是当前最优的多模态Agent，也仅能完成不到三分之一的长周期视觉搜索任务，跨步骤视觉上下文关联、多结果整合仍是核心瓶颈。
