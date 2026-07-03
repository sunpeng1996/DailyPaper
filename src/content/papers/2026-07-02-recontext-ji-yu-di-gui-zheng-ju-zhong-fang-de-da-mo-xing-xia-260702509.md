---
title: 'ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning'
title_zh: ReContext：基于递归证据重放的大模型长上下文推理框架
authors:
- Yanjun Zhao
- Ruizhong Qiu
- Tianxin Wei
- Yuanchen Bei
- Zhining Liu
- Lingjie Chen
- Ismini Lourentzou
- Hanghang Tong
- Jingrui He
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2607.02509'
url: https://arxiv.org/abs/2607.02509
pdf_url: https://arxiv.org/pdf/2607.02509
published: '2026-07-02'
collected: '2026-07-03'
category: Reasoning
direction: LLM长上下文训练-free推理优化
tags:
- Long-Context Reasoning
- Training-Free
- Attention Signal
- Evidence Replay
- Inference Optimization
one_liner: 训练-free的长上下文推理框架，利用模型内部注意力信号递归重放证据，稳定提升多基座任务表现
practical_value: '- 电商RAG/长对话客服/商品说明书问答场景可直接复用核心逻辑：不剪枝原始上下文，仅基于模型内部注意力信号抽取query关联的证据片段重放在问题前，既避免信息丢失，又解决长上下文关键信息被淹没的问题，无需额外训练

  - 工程上可复用其KV cache复用策略：预存原始上下文的KV cache，每次重放证据时仅处理新增证据和query部分，大幅降低额外推理开销，仅引入少量延迟即可提升效果

  - 多轮对话Agent场景可借鉴递归证据选择思路：每轮对话基于历史选中的证据递归补充新的相关片段，避免多轮交互后关键上下文丢失，无需外挂额外检索模块'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前大模型上下文窗口持续扩大，但长上下文场景下模型往往无法有效利用输入中已存在的相关证据，上下文访问能力和实际利用率存在显著gap；现有优化方案要么需要修改模型底层解码逻辑，要么依赖外部检索/上下文压缩，容易丢失细粒度信息，在复杂多跳任务上表现不稳定。

### 方法关键点
- 完全训练-free的推理框架，全程保留完整原始上下文，仅基于模型内部query-conditioned的注意力相关性信号抽取候选证据
- 抽取的token级证据会映射回原文本的完整句子/局部片段，避免碎片化信息干扰；支持递归多轮选择证据池，每轮选择都基于之前累积的证据池作为条件，补充新的相关片段
- 推理时将筛选出的证据池重放在原上下文和最终问题之间，相当于给模型做关键信息高亮，最终答案从「原上下文+证据池+问题」的完整prompt生成
- 基于关联记忆理论给出单调性证明：证据重放会让模型隐层表示和答案embedding的余弦相似度单调提升

### 关键实验
在8个128K长上下文数据集（覆盖事实问答、多跳推理、叙事理解、claim验证等）上，对比Vanilla、AttnSharp、DySCO等主流长上下文优化方法，在Qwen3-4B、Qwen3-8B、Llama3-8B三个基座上均取得最优平均排名，平均准确率从Vanilla的0.24提升到0.30，相对提升24.6%；64K上下文场景下相对提升可达35%，仅引入少量推理延迟，内存开销和原生推理基本持平。

**最值得记住的结论**：长上下文推理的优化方向不止扩大窗口或压缩输入，更好地组织prompt中已有的证据、给模型做关键信息高亮，也能实现稳定的效果提升。
