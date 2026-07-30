---
title: 'OptimismBench: Forecasting Bias and the Alignment Effect in Language Model
  Judgment'
title_zh: OptimismBench：大语言模型概率判断的方向偏差与对齐效应评测基准
authors:
- Seonglae Cho
- Adriano Koshiyama
affiliations:
- Holistic AI
- University College London
arxiv_id: '2607.26981'
url: https://arxiv.org/abs/2607.26981
pdf_url: https://arxiv.org/pdf/2607.26981
published: '2026-07-29'
collected: '2026-07-30'
category: Eval
direction: LLM评测 · 认知偏差审计
tags:
- LLM Evaluation
- Cognitive Bias
- Alignment Effect
- Probability Judgment
- Multilingual Benchmark
one_liner: 提出无真值反向配对偏差测量方法，发布多语言基准，揭示主流LLM概率判断的普遍乐观偏差与对齐效应
practical_value: '- 搭建LLM辅助决策类业务（如选品预判、营销活动效果预估、用户风险判断）时，先用OptimismBench风格的反向配对方法对选用的LLM做偏差测试，根据测试结果给模型输出加校准系数，避免模型固有乐观/悲观偏差传导到业务决策，比如选品场景下如果模型偏乐观，可适当下调其预测的爆品概率。

  - 自行对齐训练业务专属LLM时，可参考文中的Skew指标监控训练过程中的偏差方向变化，根据业务需求调整奖励权重：风控类场景需偏谨慎，可参考Qwen的对齐方案压缩乐观偏差；营销机会挖掘场景可参考Llama的对齐方案保留适当乐观性。

  - 多语言跨境业务选LLM时优先选择偏差跨语言稳定性高的模型，文中证实模型身份对偏差的影响是语言的4.7倍，无需为不同语言单独做偏差校准，可大幅降低运维成本。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM校准指标仅统计无符号误差，无法识别概率判断的方向偏差；而LLM作为决策辅助工具在风险评估、项目预判等场景应用越来越广，其系统性的乐观/悲观倾向会直接传导到下游决策，此前缺乏无真值即可测量方向偏差的方案。
### 方法关键点
- 核心采用反向配对设计：对同一场景分别询问正向结果概率P(成功)和反向结果概率P(失败)，定义Skew = P(成功) - (100 - P(失败))作为方向偏差得分，无需外部真值即可判断偏差方向与大小，Skew>0为乐观，<0为悲观。
- 设计4类测试赛道：校准控制赛道（有明确基准率，做 sanity check）、概率估计赛道（无基准率，为主测试赛道）、推荐赛道、显著性赛道，覆盖不同决策场景。
- 配套多维度消融实验：覆盖prompt格式、temperature、提问视角、自去偏差提示、跨语言测试、基座与对齐后模型对比等，验证偏差的稳定性。
### 关键实验结果
- 测试8家厂商的16款主流LLM，14款存在显著乐观偏差（Skew范围+4.2~+16.6），仅Anthropic的两款前沿模型偏悲观（Opus -5.1，Sonnet -7.7）。
- 11组基座vs对齐后配对测试显示，对齐训练决定偏差方向：Qwen系列对齐后偏差向负向移动（降低乐观），Llama系列对齐后偏差向正向移动（放大乐观）。
- 17款模型6语言对比显示，模型间偏差方差是语言间方差的4.7倍，模型身份对偏差的影响远大于使用的语言。
- 目前已发布覆盖10种语言的3870条测试条目，支持定制化偏差审计。
### 核心结论
LLM的方向偏差是稳定的可测量属性，但同一模型在不同任务框架下偏差方向可能反转，需针对具体业务场景做定制化偏差 profiling，而非默认统一偏差方向。
