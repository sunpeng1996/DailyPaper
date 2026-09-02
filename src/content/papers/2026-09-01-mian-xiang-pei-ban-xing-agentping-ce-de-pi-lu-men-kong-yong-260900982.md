---
title: Disclosure-Gated User Simulation for Companion-Agent Evaluation
title_zh: 面向陪伴型Agent评测的披露门控用户模拟器
authors:
- Yao Liu
- Yu He
affiliations:
- Tsinghua University
arxiv_id: '2609.00982'
url: https://arxiv.org/abs/2609.00982
pdf_url: https://arxiv.org/pdf/2609.00982
published: '2026-09-01'
collected: '2026-09-02'
category: Eval
direction: Agent评测 · 用户模拟
tags:
- User Simulation
- Agent Evaluation
- Gating Mechanism
- LLM Fine-tuning
- LLM-as-a-Judge
one_liner: 提出带披露层级门控的用户模拟器，解决陪伴Agent评测中模拟用户过度合作的问题
practical_value: '- 训练业务场景的用户模拟器（如电商咨询、售前导购Agent的测试用户）时，可采用「真实对话+合成对照轨迹」的双分支数据方案：真实分支保障回复自然度，合成分支定向生成同一人设下的正负行为对照数据，解决纯真实数据缺少可控门控轨迹的问题

  - 规模化Agent评测需同时设置两个验收标准：一是榜单排名保序（与可靠基线的rank correlation ≥0.95），二是绝对分数尺度稳定，避免出现仅排名一致但所有模型得分整体漂移的无效评测，尤其适合客服、导购等交互类Agent的效果验收

  - 条件式行为（如用户仅在满足特定条件下披露信息、跳转下单等）可通过SFT内化到模型权重，推理时无需携带显式的条件标注，可大幅缩短prompt长度，降低KV cache开销，提升推理效率'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM模拟用户是Agent规模化评测的主流方案，但存在核心缺陷：模拟用户过度合作，会主动披露全部信息，导致被测系统得分与提问数量正相关，而非真正引导用户主动表达；现有修正机制既无精确可复现的规范，也未量化过组件对评测结果的实际影响。

### 方法关键点
- 设计5级有序披露门控，合并为3个可观测披露层（表层事实/中层感受/核心脆弱点），根据Agent的行为动态调整门状态，触发说教、触碰用户反目标等负面行为时，门控会非对称回退
- 训练语料采用双分支：真实分支来自生产对话，提供自然语言表达；合成分支生成同一人设下不同Agent行为的对照轨迹，专门学习门控逻辑
- 门控能力通过SFT内化到模型权重，推理时无需显式提供每个信息的门控标注

### 关键结果
在CompanionBench英文语料上测试12个被测系统：
- 去掉合成数据分支后，中层披露对比度从0.52降至0.08，门控能力几乎消失，与未训练基座水平相当
- 122B参数的正式版模拟器与原基准榜单的排名相关度达0.993，是唯一同时满足「排名保序」「分数尺度稳定」两个验收标准的方案
- 直接prompt GPT-5.1作为模拟器，虽然排名相关度达0.972，但所有系统得分统一上浮0.521，尺度完全不可比

### 核心结论
Agent评测不能只看模型排名，必须同时校验绝对分数的稳定性和内在行为指标的一致性，否则极易得到看似正确实则无效的评测结论
