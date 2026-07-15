---
title: Multi-Agent LLMs Fail to Explore Each Other
title_zh: 多智能体LLM同伴探索失效问题与MACE优化框架
authors:
- Hyeong Kyu Choi
- Jiatong Li
- Wendi Li
- Xin Eric Wang
- Sharon Li
affiliations:
- University of Wisconsin–Madison
- University of California, Santa Barbara
arxiv_id: '2607.11250'
url: https://arxiv.org/abs/2607.11250
pdf_url: https://arxiv.org/pdf/2607.11250
published: '2026-07-13'
collected: '2026-07-15'
category: MultiAgent
direction: 多智能体协作 · 探索策略优化
tags:
- Multi-Agent
- Exploration
- Contextual Bandit
- LLM Agent
- Peer Selection
one_liner: 发现多智能体LLM存在同伴探索失效问题，提出轻量MACE框架大幅提升协作性能
practical_value: '- 多智能体业务系统（如电商多Agent推荐决策、智能客服群）不要指望LLM自主平衡探索/利用，纯prompt引导探索效果甚至不如随机选择，必须在算法层加显式探索逻辑，可直接复用MACE的LinUCB思路实现同伴选择

  - MACE的4维关系特征设计可直接迁移：同伴回复多样性、同伴独特性、历史表现、交互轮次，适配多Agent召回排序、多模型融合打分等场景的候选选择

  - 当系统内Agent能力/上下文差异越大（如电商场景下有选品、文案、定价等不同分工的异质Agent），探索的收益越高，优先在异质Agent池部署探索策略，同质Agent池可省略该模块节约开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多智能体LLM系统广泛应用于协作推理、任务分工等场景，但默认LLM能自主选择合适的协作同伴，实际上从Qwen2.5-7B到GPT-5都存在过早锁定某一交互对象的近视问题，导致协作效率低、累积后悔值高，该结构性缺陷尚未被系统性研究和解决。

### 方法关键点
- 将多智能体探索问题建模为Partially Observable Stochastic Game (POSG)，拆解为每个Agent独立的上下文多臂老虎机问题，避开原始问题NEXP-hard的求解复杂度
- 设计4种关系特征编码交互上下文：回复多样性、同伴独特性、历史表现、交互轮次，捕捉非稳态的同伴能力变化
- 基于LinUCB算法构造选择策略，用不确定性bonus鼓励探索未充分测试的同伴，根据交互reward实时更新模型参数

### 关键实验
在HotpotQA（上下文异质场景）、Math500、GPQA（参数异质场景）上测试，对比基线包括纯prompt引导的In-Context Exploration、随机选择、固定拓扑结构选择。结果显示：上下文异质场景下纯prompt探索比随机选择表现更差，MACE相较随机选择后悔值降低40%以上；参数异质场景下甚至GPT-5搭配MACE后性能也提升8%；MACE在HotpotQA上学到的策略可直接迁移到未见过的2WikiMultiHopQA数据集，仍比所有基线性能高12%左右。

### 核心结论
多智能体系统的探索收益和Agent池的能力多样性正相关，越异质的系统越需要显式的探索引导，不要指望LLM自主涌现多智能体探索能力
