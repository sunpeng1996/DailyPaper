---
title: 'Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning
  via Evidence-Aware Reinforcement Learning'
title_zh: 基于证据感知强化学习解决长上下文推理的重复复制问题
authors:
- Lizhe Fang
- Weizhou Shen
- Tianyi Tang
- Yisen Wang
affiliations:
- Peking University
- Alibaba Group
arxiv_id: '2607.19345'
url: https://arxiv.org/abs/2607.19345
pdf_url: https://arxiv.org/pdf/2607.19345
published: '2026-07-21'
collected: '2026-07-22'
category: Training
direction: 长上下文LLM · RL推理能力优化
tags:
- Long-Context LLM
- Reinforcement Learning
- Reward Shaping
- Reasoning
- Data Construction
one_liner: 提出证据感知奖励GEAR与自动标注管道，缓解长上下文推理重复复制，最高提4.6个准确率点
practical_value: '- 电商导购/会话理解类长上下文Agent做RL微调时，可复用GEAR奖励设计：新增关键证据匹配奖励+无关内容复制惩罚，减少无意义的输入复制，缩短推理链长度，降低推理成本同时提升回答准确率

  - 商品详情页QA、客服知识库等需要构造长文档问答训练数据的场景，可复用文中自动标注管道：先采样关键chunk再生成问题，自动获得证据标注，无需人工介入即可产出RL训练用样本

  - 长上下文LLM落地商品属性抽取、用户长评论理解等任务时，可复用n-gram重叠率指标评估模型的无关内容复制率，快速定位推理效率低的Bad Case'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
带思考链的长上下文LLM处理长输入时普遍存在重复复制故障：会大量直接拷贝prompt内容到推理轨迹，挤占token预算，且问题随上下文长度增长持续恶化，最终导致准确率下降、推理成本大幅上升。经分析根因是模型grounding能力不足，无法区分任务相关关键证据与无关干扰内容，存在无差别复制而非选择性提取信息的问题。

### 方法关键点
- 提出GEAR（Grounding Evidence-Aware Reward）奖励塑造机制：在标准准确率奖励基础上，新增两项互补信号：① grounding奖励：计算推理轨迹与关键证据的n-gram重叠率，鼓励模型关注相关信息；② 干扰惩罚：计算推理轨迹与无关上下文的n-gram重叠率，惩罚无意义复制；两项信号需同时使用，单独启用任意一项都会导致性能下降。
- 提出无人工标注的证据标注数据管道：对任意长文档，先分块采样1-3个chunk作为关键证据区，基于该区域生成QA对，再通过仅用关键区重答的方式验证正确性，自动构造带证据标注的训练数据。

### 关键结果
基于Qwen3.5系列9B/27B/35B MoE模型，用GSPO算法训练，在5个互不重叠的长上下文基准（Ruler、LongBench-v2等）上测试，相比仅用准确率奖励的RL baseline，32k上下文下平均提升1.5~2.8个点，128k上下文下平均提升2.1~4.6个点，同时推理轨迹3-gram重叠率最高下降8.7pct，思考长度最多缩短26.4%。

> 最值得记住的一句话：即便长上下文LLM评测已从简单检索转向复杂推理，精准的相关证据grounding能力仍然是不可或缺的核心能力，存在极大优化空间。
