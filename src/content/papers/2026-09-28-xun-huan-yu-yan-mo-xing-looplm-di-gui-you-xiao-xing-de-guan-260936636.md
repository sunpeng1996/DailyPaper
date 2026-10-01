---
title: What Makes Recurrence Effective in Looped Language Models?
title_zh: 循环语言模型（LoopLM）递归有效性的关键影响因素与优化方案
authors:
- Xinlin Zhuang
- Siyuan Wang
- Imran Razzak
- Weiyang Liu
affiliations:
- The Chinese University of Hong Kong
- MBZUAI
arxiv_id: '2609.36636'
url: https://arxiv.org/abs/2609.36636
pdf_url: https://arxiv.org/pdf/2609.36636
published: '2026-09-28'
collected: '2026-10-01'
category: LLM
direction: 大语言模型 · LoopLM 架构优化
tags:
- LoopLM
- Recurrent LLM
- Test-time Scaling
- Reasoning
- Architecture Optimization
one_liner: 系统拆解LoopLM递归生效的边界与架构要素，提出轻量条件组合方案实现跨推理预算性能提升
practical_value: '- 端侧轻量化导购Agent/商品推理场景可复用LoopLM的参数共享+动态循环深度设计，无需增加模型参数即可根据任务复杂度（如多轮意图拆解、优惠规则计算）调整循环次数，平衡推理性能与延迟

  - 针对推荐/搜索场景的推理密集型任务，优先采用「中等物理深度+适度循环次数」的平衡配置，搭配通道级历史状态注入+轻量时间步门控，可在同参数下获得更高推理准确率

  - 需同时兼顾知识查询（如商品属性问答）与推理需求的场景，可在递归核心外增加输出侧非递归Coda层缓解低循环次数下的知识性能衰减，输入侧增加非递归Prelude层支撑超训练深度的推理扩展'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM参数量快速膨胀导致训练部署成本陡增，LoopLM通过参数共享的递归结构实现计算深度扩展，无需新增参数即可灵活调整推理算力，但递归生效的边界、不同架构设计的影响规律尚不明确，尤其缺乏超训练深度下的性能稳定优化方案。

### 方法关键点
- 所有对比实验严格控制物理深度、训练有效深度、推理深度、训练流程四要素一致，对比全层递归的BaseLoop与带非递归输入Prelude/输出Coda层的CoreLoop两种架构
- 对比初始状态注入的局限，提出基于近邻状态差的动态历史状态注入方案，结合Loop Gating/Branch Gating/AdaLN三类轻量时间步调制策略，验证多条件策略的组合增益
- 任务拆分为知识类、推理类两大组，覆盖欠展开、训练深度匹配、超训练深度扩展三个推理预算场景进行全维度验证

### 关键结果
基于Llama3.1-1B、Qwen3-0.6B两个backbone训练，评测覆盖SciQ、ARC、ProofWriter等11个基准，核心数据：
1. 超训练深度下递归可提升推理性能2.97pp，但知识性能下降10.69pp；
2. 4物理层×5循环的平衡配置在超训练深度下推理性能超过同训练算力的非递归模型1.24pp；
3. 历史状态注入+时间步门控的组合方案在3倍训练深度下整体精度比BaseLoop高1.16pp。

### 核心结论
LoopLM的递归收益高度依赖任务类型与架构配置，有效深度不是性能的唯一决定因素，动态历史条件+时间步调制的轻量组合可实现跨推理预算的鲁棒性能
