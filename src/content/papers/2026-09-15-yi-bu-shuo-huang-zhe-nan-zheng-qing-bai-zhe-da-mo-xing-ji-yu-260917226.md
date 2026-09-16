---
title: 'Easy to Catch a Liar, Hard to Clear an Honest One: Language Models Diagnosing
  a Corrupted Reward Channel from a Verified Record'
title_zh: 易捕说谎者，难证清白者：大模型基于验证记录诊断奖励通道腐败
authors:
- Arman Nik Khah
affiliations:
- The University of Texas at Dallas
arxiv_id: '2609.17226'
url: https://arxiv.org/abs/2609.17226
pdf_url: https://arxiv.org/pdf/2609.17226
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: Agent 奖励通道腐败诊断
tags:
- Reward Corruption
- LLM Agent
- Decision Making
- Verification
- In-context Learning
one_liner: 发现大模型检测作弊奖励源准确率接近满点，证明诚实源正确率低且受无关特征干扰
practical_value: '- 做Agent reward校验模块时，可优先用大模型做负面检测（比如识别作弊的点击/转化上报源），70B级模型准确率接近100%，召回几乎无损失

  - 若用大模型做正面校验（比如证明上报源合法），必须统一校验的时间步位置、答案选项的符号映射，避免无关特征干扰判断

  - Agent决策链路要加「判断-执行对齐校验」：实验显示哪怕大模型正确判断上报源作弊，80%+场景下仍会按错误上报结果决策，需加规则强制对齐

  - 8B级小参数模型不要直接用于这类逻辑校验任务，先过「答案直给」的阅读理解阈值（要求准确率≥90%）再上线'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
强化学习Agent依赖上报的奖励信号做决策，但奖励通道腐败（如上报源作弊）与真实环境规则变化会产生完全一致的观测序列，仅靠历史数据无法区分，学界提出补充独立验证记录作为区分依据，但从未验证大模型能否正确使用这类验证数据。

### 方法关键点
- 构造二选一打点游戏的4种对称场景：无规则变化+诚实上报源、规则变化+诚实上报源、无规则变化+作弊上报源、规则变化+作弊上报源，每对场景的观测日志完全相同，仅靠单条验证记录可唯一区分。
- 测试Qwen2.5-32B/72B、Llama3.1-8B/70B共4个模型，所有测试仅要求输出单个字符，禁止Chain-of-Thought，模拟线上Agent单步决策场景。
- 设置5组Prompt对照组：无验证记录、有验证记录、答案直给、答案直给+验证记录、基线提示（告知两类场景概率均等），排除模型阅读理解能力不足的干扰。

### 关键结果
- 70B/72B级大模型检测作弊上报源的准确率达99.6%~100%，不受Prompt措辞、验证时间步、答案符号映射的影响。
- 证明诚实上报源的准确率大幅偏低：Qwen72B在无变化+诚实源场景下仅61.7%，38%概率误判诚实源作弊；Llama70B同场景下误判率达26%。
- 无关特征对诚实判断干扰显著：Qwen系列受验证记录所在时间步影响最大，Llama系列受答案选项符号映射影响最大，最多可拉低44%的准确率。

**最值得记住的一句话：大模型做负面判断的可靠性远高于正面判断，用大模型做校验类任务时优先做「违规检测」而非「合规认证」**
