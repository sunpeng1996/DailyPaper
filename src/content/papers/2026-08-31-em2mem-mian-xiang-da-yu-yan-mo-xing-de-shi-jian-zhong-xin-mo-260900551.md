---
title: 'EM^2Mem: Event-Centric Multimodal Memory for Large Language Models'
title_zh: EM²Mem：面向大语言模型的事件中心多模态记忆框架
authors:
- Yijun Chen
- Yaqi Zheng
- Yanya Li
- Boyi Xiao
- Buqiang Xu
- Shuofei Qiao
- Jizhan Fang
- Xinle Deng
- Yunzhi Yao
- Xuehai Wang
affiliations:
- 浙江大学
- 华南理工大学
- 联想集团
arxiv_id: '2609.00551'
url: https://arxiv.org/abs/2609.00551
pdf_url: https://arxiv.org/pdf/2609.00551
published: '2026-08-31'
collected: '2026-09-02'
category: LLM
direction: 多模态大模型 · 长视频推理记忆
tags:
- Multimodal Memory
- Long Video QA
- Event Centric
- RAG
- LLM Reasoning
one_liner: 提出以事件为锚点的先对齐后检索多模态记忆框架，提升长视频QA精度与推理效率
practical_value: '- 直播/商品短视频等多模态内容库的QA/检索场景，可借鉴事件锚点设计，提前将字幕、画面、结构化属性（商品、动作、话题）绑定到30s级事件单元，避免推理时跨模态对齐，降低Latency和Token消耗

  - 多模态RAG系统可优化索引结构，不再按模态拆分存储，而是按业务语义单元（如单次商品讲解、一轮用户交互）预聚合多源证据，检索直接返回完整语义单元，提升召回准确率与生成的归因性

  - 对于低频更新、高频查询的静态多模态内容库，可采用预构建事件索引的方案，单次构建成本可在查询量超过23次后实现摊销，整体成本远低于推理时动态对齐的方案

  - Agent的长期记忆模块可借鉴「事件单元+双层关联图」的设计，短期记忆按事件绑定多模态信息，长期记忆抽离语义规律并关联回原始事件，兼顾推理效率与记忆溯源能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态记忆方案多按模态拆分存储字幕、关键帧、摘要等孤立片段，长视频QA时需要LLM在推理阶段重新完成跨模态、时序对齐，不仅占用大量上下文窗口、归因困难，还会带来极高的推理延迟和Token成本，无法适配长时序多模态内容的高并发查询需求。

### 方法关键点
- 采用「先对齐后检索」设计：先将长视频切分为30s基础事件段，以事件锚点为统一索引，绑定每个事件的字幕、关键帧、结构化元数据（动作、对象、话题、场景、实体），形成独立的事件记忆单元
- 构建多层级时序上下文视图：按3分钟、10分钟、1小时粒度聚合事件摘要，关联到覆盖范围内的所有基础事件单元，支持不同时间粒度的推理需求
- 新增双层事件关联图：episodic graph存储跨事件的实体、对象、时序关联，semantic graph存储跨事件的长期规律（习惯、偏好、稳定关系），所有节点均关联回原始事件锚点，支持证据溯源
- 推理阶段直接检索事件单元，通过关联图做轻量扩展，筛选后输出紧凑证据视图给LLM生成答案，无需再做跨模态对齐

### 关键结果
在EgoLifeQA、Ego-R1 Bench、Video-MME (L)三个长视频QA基准上测试，相比最强记忆基线WorldMM：平均准确率分别提升2.0、2.4、3.7个百分点，单query延迟降低4.67倍，总推理Token减少63.66%，事件级Top-5证据召回提升7.0个百分点；预构建索引的成本在查询量超过23次后即可实现收益逆转。

> 核心结论：多模态记忆的核心不是存储信息量的大小，而是如何把异构证据组织成与用户查询逻辑对齐的可检索单元，预对齐的成本可通过高频查询充分摊销
