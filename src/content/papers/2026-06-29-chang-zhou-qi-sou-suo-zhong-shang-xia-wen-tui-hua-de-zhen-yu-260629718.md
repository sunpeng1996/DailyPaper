---
title: Diagnosing and Mitigating Context Rot in Long-horizon Search
title_zh: 长周期搜索中上下文退化的诊断与缓解
authors:
- Shijie Xia
- Yikun Wang
- Zhen Huang
- Pengfei Liu
affiliations:
- Shanghai Jiao Tong University
- Fudan University
- SII
- GAIR
arxiv_id: '2606.29718'
url: https://arxiv.org/abs/2606.29718
pdf_url: https://arxiv.org/pdf/2606.29718
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: LLM Agent · 长上下文搜索优化
tags:
- Context Rot
- LLM Agent
- Long-horizon Search
- Context Management
- Rejection Sampling
one_liner: 诊断长周期Agent搜索的上下文退化现象，系统评测多种缓解策略给出工程选型指导
practical_value: '- 开发长周期多轮搜索Agent、多轮推荐对话Agent时，优先采用「上下文修剪+压缩」混合策略，可在性能、调用成本和退化缓解之间取得最优平衡

  - 若业务使用强能力大模型基座，可尝试基于子Agent调用的上下文隔离方法，能获得比被动上下文管理更高的性能增益

  - 多轨迹采样聚合生成答案时，过滤掉模型主动放弃、标注不确定的轨迹，仅保留置信答案聚合，可带来平均2.6%~4.9%的准确率提升

  - 越频繁触发上下文压缩/修剪越能缓解退化，但会增加工具调用成本和未完成任务率，需要根据业务对延迟和准确率的要求平衡触发阈值'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有上下文退化研究大多聚焦单轮长输入场景或人类参与的多轮对话，缺乏对长周期Agent搜索场景（多轮多源、渐进累积上下文）的针对性分析，不同上下文管理方法对退化的缓解效果也缺乏系统对比，无法给工程落地提供清晰选型指导，而上下文退化已经成为长周期深度搜索Agent的核心性能瓶颈。

### 方法关键点
1. 构建了长周期Agent搜索终止状态的细粒度分类体系，分为放弃、不确定答案、确定答案、无答案四类，采用LLM-as-judge自动标注，与人类判断一致性达98.7%；
2. 通过多组上下文剪枝实验，验证上下文退化的成因，分析累积上下文与退化现象的关联；
3. 系统评测了三类共7种上下文管理方法（压缩类3种、修剪类3种、隔离类1种），额外提出了一种无需修改Agent框架的rot感知后处理拒绝采样方法。

### 关键结果
在BrowseComp、BrowseComp-Plus、xbench-DeepSearch三个基准，对4个主流开源大模型测试：
1. 核心现象：长周期搜索中，累积上下文会导致模型直接放弃回答或提前输出不确定答案，退化程度随轨迹长度增加而加剧，上下文窗口大小本身不是主要性能瓶颈；
2. 混合「上下文修剪+压缩」策略平均准确率比原生ReAct提升8%以上；
3. rot感知过滤在三种聚合方法下，平均带来2.6%~4.9%的准确率提升。

### 核心结论
长周期Agent搜索的性能瓶颈不是上下文窗口大小，而是累积上下文带来的上下文退化问题。
