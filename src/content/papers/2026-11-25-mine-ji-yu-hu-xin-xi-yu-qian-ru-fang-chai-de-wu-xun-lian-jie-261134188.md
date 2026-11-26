---
title: 'MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual
  Information and Embedding Variance'
title_zh: MINE：基于互信息与嵌入方差的无训练间接Prompt注入防御方法
authors:
- Truong Phan
- Ngoc-Quan Pham
- Dat Quoc Nguyen
affiliations:
- Qualcomm AI Research
arxiv_id: '2611.34188'
url: https://arxiv.org/abs/2611.34188
pdf_url: https://arxiv.org/pdf/2611.34188
published: '2026-11-25'
collected: '2026-11-26'
category: RAG
direction: RAG安全 · 间接Prompt注入防御
tags:
- Prompt Injection
- RAG
- Training-free
- Mutual Information
- Embedding Variance
one_liner: 提出无需训练、攻击无关的RAG预过滤方法，通过最大化查询相关度抵御间接Prompt注入
practical_value: '- 电商导购/客服RAG系统可直接接入MINE作为召回后预过滤模块，无需训练、无额外LLM调用成本，即可将静态Prompt注入攻击成功率（ASR）压至1%以下，同时几乎不损失回答准确率

  - RAG召回后重排序可复用MINE的「互信息+子集内嵌入方差」联合优化思路，相比单纯按cosine相似度排序，准确率提升7pct以上，ASR下降7pct以上

  - 调用外部工具的Agent系统可适配JSON感知的MINE变种，抵御工具返回内容的注入攻击，在InjecAgent数据集上ASR可低至0.12%，同时保持99%以上的有效调用率

  - 长文本RAG场景优先选择MINE类预过滤方案，相比Prompt工程类防御，长上下文下ASR稳定≤3.31%，不会因上下文变长稀释防御效果，同时推理延迟更低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG系统的间接Prompt注入防御均为被动式：Prompt工程类易被注入指令绕过，监督检测类需针对每种新攻击重新训练，泛化性差，长上下文场景下防御效果骤降，普遍存在准确率与安全性trade-off差、推理延迟高的问题。

### 方法关键点
- 核心思路转变：不检测攻击，而是从召回上下文中筛选与用户查询最相关的span子集，注入内容天然相关性低、语义离散，会被自动过滤
- 优化目标：最大化span子集与查询的互信息，同时最小化子集内嵌入方差，超参数α控制两者权重，最优取值为0.4
- 工程优化：将组合子集选择问题松弛为连续权重优化，用投影梯度上升迭代20步即可求解，取top-k权重的span按权重降序排列，适配LLM lost-in-the-middle bias
- Agent场景适配：新增JSON感知切分器，保留原始字段顺序避免破坏结构化工具返回结果

### 关键结果
构建了长上下文Prompt注入基准LC-Inj-SQuAD，平均上下文长度4032词；在4个数据集（Inj-SQuAD、Inj-TriviaQA、LC-Inj-SQuAD、InjecAgent）上对比9种基线，静态攻击下MINE是唯一同时保持准确率≥79%、ASR≤3.31%的无训练防御方案；长上下文场景下相比最强Prompt工程基线Sandwich，准确率高17~28pct，ASR低24~51pct，推理延迟低3倍以上；自适应攻击下是唯一可用的防御方案，长上下文ASR为23.2%，远高于其他基线的可用度。

**最值得记住的一句话**：对抗间接Prompt注入的最优思路不是被动检测攻击，而是主动筛选与用户意图高度相关的内容，从根源上切断注入内容的影响路径。
