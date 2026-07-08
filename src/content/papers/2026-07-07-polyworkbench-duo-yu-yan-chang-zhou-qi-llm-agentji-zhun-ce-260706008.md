---
title: 'PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents'
title_zh: PolyWorkBench：多语言长周期LLM Agent基准测试集
authors:
- Hongliang Li
- Yijin Liu
- Zhiwei Zhang
- Zihe Liu
- Xinyue Lou
- Jinan Xu
- Fandong Meng
- Kaiyu Huang
affiliations:
- Beijing Jiaotong University
- Weixin AI, Tencent Inc
arxiv_id: '2607.06008'
url: https://arxiv.org/abs/2607.06008
pdf_url: https://arxiv.org/pdf/2607.06008
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: 多语言长周期Agent性能基准评估
tags:
- LLM-Agent
- Multilingual
- Benchmark
- Long-Horizon
- Evaluation
one_liner: 推出覆盖5大职场域的多语言长周期LLM Agent基准，配套混合评估框架揭示多语言执行的复合负面影响
practical_value: '- 跨境电商多语言Agent评估可直接复用该混合评估框架：结构校验保证格式/数值正确性，可执行验证落地业务逻辑，LLM-as-Judge补充语义流畅度校验，避免单一评估维度的偏差

  - Agent脚手架对性能影响可达24个百分点，上线多语言Agent前需针对自身业务场景做脚手架选型测试，不要盲信通用开源脚手架的默认效果

  - 多语言任务存在错误跨步骤累积问题，可在Agent规划、工具调用、生成每一步插入跨语言语义一致性校验，避免最终输出和原始需求漂移

  - 涉及俄/西/德等小语种的跨境业务，中阶LLM可通过best-of-3采样的方式，用可控的计算成本换取14~21个百分点的任务成功率提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长周期Agent基准均默认单语言设定，多语言NLP基准仅覆盖静态单步任务，二者完全割裂，无法反映跨国/跨境业务中Agent需在统一工作流内处理多语言输入、推理、工具调用、输出的真实场景，多语言对Agent执行轨迹的复合负面影响长期被低估。

### 方法关键点
- 基准覆盖电商、知识工作、法务、本地化、制造5大职场域共67个人工构造任务，88%任务涉及3种及以上语言，平均每个任务含8.5个工具调用步骤，覆盖10种主流语言
- 采用混合评估框架：结构打分（按任务规则给部分完成项赋分）+ 可执行验证（自动化脚本校验数值、格式、功能正确性）+ LLM-as-Judge（评估语义一致性、流畅度等规则无法覆盖的维度）
- 核心评估指标为Pass@1（单轮任务平均结构分）、Pass@3（3轮采样最优结果平均结构分）

### 关键实验结果
测试18组模型+Agent脚手架组合，最优的Claude Opus 4.8+ClaudeCode组合Pass@1达0.921，其余所有组合均低于0.77；同一模型更换脚手架性能波动可达8~24个百分点；电商类任务是性能重灾区，中阶模型在电商域得分普遍比其他域低20~35个点；中阶模型采用3次采样选最优的策略，可提升14~21个百分点的任务成功率。

### 核心结论
多语言不是Agent输入输出的表层属性，而是会贯穿整个执行轨迹、带来错误复合累积的核心影响因子，评估多语言Agent不能仅测静态跨语言能力，必须结合长周期执行场景。
