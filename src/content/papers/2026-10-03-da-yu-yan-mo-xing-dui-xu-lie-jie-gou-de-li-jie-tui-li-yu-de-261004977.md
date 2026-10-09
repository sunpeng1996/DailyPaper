---
title: Do LLMs Understand Sequential Structure? A Controlled Study of Inference and
  Generation
title_zh: 大语言模型对序列结构的理解：推理与生成的对照实验
authors:
- Jerry Wang
- Zhengxiang Wang
- Ting Yu Liu
- Hsin-Ling Hsu
- Yi-Cheng Lai
- Tengfei Ma
affiliations:
- University of Illinois Urbana-Champaign
- Stony Brook University
- National Chengchi University
arxiv_id: '2610.04977'
url: https://arxiv.org/abs/2610.04977
pdf_url: https://arxiv.org/pdf/2610.04977
published: '2026-10-03'
collected: '2026-10-09'
category: LLM
direction: LLM序列理解能力受控评估
tags:
- Sequential Reasoning
- In-Context Learning
- Agent Simulation
- Markov Model
- Controlled Evaluation
one_liner: 通过受控博弈与n-gram任务揭示LLM序列结构理解的三类可分离能力与高阶依赖瓶颈
practical_value: '- 做用户行为模拟、多Agent仿真时，不要仅用表面分布匹配评估效果，需加入序列规则校验，避免看似真实的模拟实际不符合用户行为的条件依赖逻辑

  - 推荐系统用LLM做用户序列建模、下一个Item生成时，优先控制依赖阶数在2阶以内，高阶依赖（≥4阶）LLM生成保真度会陡降，可配合传统n-gram模型做兜底校验

  - 做Agent交互策略识别（如用户购物决策序列模式识别、竞价对手策略识别）时，更长的上下文序列不会提升识别准确率，反而可能引入噪声，建议控制序列长度在有效规则覆盖的最短范围内

  - 高可靠Agent应用可拆分规则识别与分步执行模块，引入teacher forcing机制校验模型的规则理解能力，避免识别正确但执行错误的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM被广泛用于交互Agent、用户行为模拟、序列推荐等场景，这类场景要求LLM不仅匹配表面行为频率，还要能还原序列背后的条件依赖结构，但现有评估多关注整体效果，缺乏对底层序列理解能力的受控验证，无法区分表面分布匹配和真实规则理解。
### 方法关键点
- 设计四层递进的受控任务：从石头剪刀布（RPS）的策略识别，到一阶/二阶马尔可夫规则的推理生成，再到无交互的1~8阶随机n-gram序列续写，拆分策略识别、分布匹配、规则执行三类独立能力
- 覆盖7款主流LLM评估：包括DeepSeek V4 Chat/Reasoner、GPT-5、GPT-4.1、Gemini 3 Flash、Qwen3-8B等，涵盖闭源/开源、不同参数规模与推理能力等级
- 针对性指标设计：策略识别用精确匹配准确率，确定性规则生成用重叠率、严格匹配率，高阶随机序列用上下文条件似然增益（CCLG）、加权JS散度（WJS）
### 关键结果数字
- 所有模型的马尔可夫策略识别准确率平均比非马尔可夫策略低15%以上，即使交互序列长度从100轮增加到1000轮，识别准确率不升反降，而传统MLE基线在相同条件下可达100%准确率
- 正确识别策略的前提下，马尔可夫玩家的生成MSE比非马尔可夫玩家高100%以上，仅41.8%的错误识别案例能保持边际分布TV≤0.02，表面分布逼真不代表底层规则正确
- n-gram续写任务中，当依赖阶数上升到8阶时，多数模型的CCLG陡降、WJS提升40%以上，即使明确给出完整转移规则也无法消除高阶依赖带来的性能下降
### 核心结论
正确的策略识别、表面的分布匹配与忠实的条件规则执行是LLM序列理解的三类可分离能力，表面行为保真度可能掩盖底层生成机制的错误
