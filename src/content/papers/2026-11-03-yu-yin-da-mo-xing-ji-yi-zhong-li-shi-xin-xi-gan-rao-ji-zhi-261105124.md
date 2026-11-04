---
title: 'The Right Source Is Not Enough: Understanding History Interference in Speech-LLM
  Memory'
title_zh: 语音大模型记忆中历史信息干扰机制的因果分析
authors:
- HongJin Song
- Weiqiao Shan
- Runwu Shi
- Yifei Wu
- Yujin Wang
- Jiale Luo
- Jiasheng Kuang
- Xinyu Yang
- Zhaoqi Cui
- Chuizheng Kong
affiliations:
- Beijing Institute of Technology
- Northeastern University, China
- Institute of Science Tokyo
- Ant Group
- Wuhan University
arxiv_id: '2611.05124'
url: https://arxiv.org/abs/2611.05124
pdf_url: https://arxiv.org/pdf/2611.05124
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM 多轮对话记忆干扰机制研究
tags:
- Speech-LLM
- Memory Interference
- Causal Intervention
- Multi-turn Conversation
- Activation Patching
one_liner: 通过因果干预揭示Speech-LLM中历史信息干扰的两条路径，区分源角色与答案值的独立影响
practical_value: '- 多轮对话Agent（如电商智能客服）做记忆管控时，不能仅做源的存取和识别，还要在答案生成阶段管控历史值的影响，避免用户之前咨询的订单/商品信息错误套用到新问题的回答中

  - RAG/生成式推荐的答案优化可参考双信号干预思路：在模型深层强化当前query对应的源角色权重，同时在中间层抵消无关召回片段的答案值影响，两者联合可修复约80%的历史干扰错误

  - 长上下文候选排序场景（如多轮商品搜索）的历史干扰会提前嵌入问题-候选状态，仅靠后期attention掩码无法消除，需针对性做中间层状态管控，效果优于开放生成场景的掩码方案'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Speech-LLM多轮对话的记忆优化主要聚焦信息留存与检索能力，忽略了已保留的无关历史信息会干扰当前问题回答——即便模型能正确识别目标源，仍可能出现用历史无关值作答的错误，这一干扰机制此前未被明确拆解。

### 方法关键点
- 基于MOSS-Audio-8B、MiMo-Audio-7B两个开源语音大模型开展控制实验，构造包含目标源+无关历史源的多轮输入，设置中性/竞争历史对照组，排除上下文长度的通用影响
- 设计三类因果干预：阻断对无关源的直接attention访问、跨条件迁移问题-候选隐藏状态、拟合低维源角色/历史值子空间做定向干预，区分两类信号的独立影响
- 分别测试开放生成、多项选择两种回答场景的干扰路径差异

### 关键结果
- 自然语音数据集上，加入竞争历史后MOSS准确率从84.23%降至78.73%，MiMo从48.23%降至39.67%，错误高度定向到历史源对应的值，而非随机错误
- 开放生成场景下，阻断后期对无关源的访问可消除98%以上的历史值错误；多项选择场景下仍有70%左右的错误留存，源于早期访问已将干扰嵌入问题-候选状态
- 源角色信号的影响峰值在模型深层（22~23层），历史值信号的影响峰值在中间层（16层左右），两者联合干预可修复79.1%~83.8%的自然发生的历史干扰错误

最值得记住的结论：可靠的对话记忆不仅需要留存和检索正确的信息，还需要控制这些信息如何参与答案计算，仅靠源识别无法完全排除无关历史值的干扰
