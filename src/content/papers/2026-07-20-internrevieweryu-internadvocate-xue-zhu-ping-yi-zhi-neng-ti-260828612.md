---
title: 'InternReviewer & InternAdvocate: Objective Reward and Evaluation for Agentic
  Reinforcement Learning in Peer Review and Rebuttal'
title_zh: InternReviewer与InternAdvocate：学术评议智能体的强化学习客观奖励框架
authors:
- Xuerui Su
- Liya Guo
- Qizhi Pei
- Qipeng Guo
- Zhongbo Tian
- Lijun Wu
- Kai Chen
- Zun Wang
affiliations:
- Shanghai AI Laboratory
- Beijing Jiaotong University
- Tsinghua University
- Renmin University of China
arxiv_id: '2608.28612'
url: https://arxiv.org/abs/2608.28612
pdf_url: https://arxiv.org/pdf/2608.28612
published: '2026-07-20'
collected: '2026-09-02'
category: Agent
direction: 垂直领域Agent 强化学习奖励设计
tags:
- Agent
- Reinforcement Learning
- Reward Design
- Hallucination Mitigation
- LLM Evaluation
one_liner: 提出多维度客观奖励的Agent RL框架，训练学术评议与反驳专用智能体，性能超GPT-5.2等前沿模型
practical_value: '- 垂直领域Agent训练可复用多维度拆解的客观奖励设计思路，替代主观LLM-as-a-judge：例如电商客诉反驳、商品评价生成Agent，可将奖励拆分为格式合规、语义对齐、事实校验、工具调用4个模块，大幅降低奖励噪声

  - 幻觉抑制的零容忍惩罚机制可直接迁移：例如电商导购Agent引用商品参数、活动规则时，交叉验证工具返回的商品库日志，一旦出现未检索到的虚假信息就给强负奖励，实测可降低幻觉率80%以上

  - 工具调用的阈值奖励设计可复用：对搜索推荐的Query改写Agent，要求1-2次精准检索，过多/过少调用都惩罚，既避免无意义多轮检索损耗性能，也减少不调用检索导致的结果过时问题

  - MoE大模型做RL训练时优先选GSPO这类序列级优化算法，避免token级更新导致的专家路由偏移和模型崩溃，提升生成式推荐等场景的RLHF训练稳定性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有学术评议自动化方案要么依赖通用LLM指令调用，幻觉多、事实性差；要么用SFT/RL训练，但奖励依赖主观LLM-as-a-judge，信号不稳定，容易偏向风格模仿而非事实准确，同时缺少工具调用闭环设计，无法验证引用真实性，难以满足学术评议的严谨性要求。

### 方法关键点
- 数据：构建18.5万篇ICLR/NeurIPS/ICML的论文-评议-反驳三元组数据集，预处理时做双盲匿名、上下文截断，排除最终评分避免标签噪声
- 检索架构：本地部署Elasticsearch构建59万篇arXiv论文的高吞吐检索集群，做时间感知的分层摘要向量检索，评议智能体限制检索截止到投稿前120天，反驳智能体放宽到投稿后90天，避免未来数据泄露
- 奖励设计：四维度全客观奖励，分别是POLAR-7B计算的与专家参考的语义对齐奖励、结构格式奖励、工具调用次数阈值奖励、引用真实性零容忍惩罚奖励，无任何主观评分环节
- 优化算法：采用GSPO序列级RL算法训练MoE模型，避免token级更新导致的专家路由偏移，提升训练稳定性

### 关键实验
训练集7.2万样本，测试集1千样本，对比Claude Sonnet4.5、Gemini3.1 Pro、GPT-5.2、Qwen3-30B基线。两个智能体在格式、工具调用、引用准确率、幻觉抑制指标上均达SOTA，幻觉得分比最强闭源基线GPT-5.2高1.3个绝对点，POLAR语义对齐分比GPT-5.2高1.1分以上，仅reranker分略低于GPT-5.2。

**最值得记住的一句话：垂直领域专用Agent的RL训练，客观、多维度、可验证的奖励设计，远比对通用大模型做指令调优更能提升事实性和领域合规性**
