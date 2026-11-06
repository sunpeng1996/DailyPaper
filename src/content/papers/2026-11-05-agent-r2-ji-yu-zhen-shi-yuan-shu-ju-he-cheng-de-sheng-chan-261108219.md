---
title: 'Agent-R$^2$: Scaling Agents for Realistic Productivity Work via Real-Source
  Data Synthesis'
title_zh: Agent-R²：基于真实源数据合成的生产力场景Agent训练框架
authors:
- Teng Pan
- Zixuan Wang
- Yuchen Yan
- Qifei Wu
- Yao Chen
- Yingqi Qu
- Ruiqing Zhang
- Yongliang Shen
affiliations:
- Zhejiang University
- Baidu Inc.
arxiv_id: '2611.08219'
url: https://arxiv.org/abs/2611.08219
pdf_url: https://arxiv.org/pdf/2611.08219
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 生产力场景训练数据合成与优化
tags:
- Agent Training
- Data Synthesis
- Reinforcement Learning
- LLM Agent
- Rubric-based RL
one_liner: 提出真实源驱动的Agent训练数据合成框架，仅用4k实例训练4B模型超越235B基线
practical_value: '- 电商运营/数据分析Agent落地可直接复用3阶段数据合成pipeline：从公开行业语料挖掘真实工作流，匹配商家/平台真实业务文件作为输入，生成对应任务指令和细粒度打分规则，大幅降低人工标注成本

  - 多格式输入类Agent（如商品资质审核、销售数据分析、营销方案生成）可复用SFT+细粒度rubric RL的训练范式，小参数模型即可达到接近大几十倍参数量模型的效果，推理成本可降低90%以上

  - 针对生成式推荐/广告文案、营销活动方案容易出现虚假信息、数据不符的问题，可复用缓解shortcut行为的方法：要求输出内容可追溯到输入证据，训练时鼓励多步验证，降低错误输出率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent难以落地真实生产力工作，核心瓶颈是缺乏覆盖真实工作意图、异构文件上下文、可交付物级评估标准的可扩展训练数据。现有合成数据要么依赖人工编写工作流（可扩展性差），要么用LLM生成的文件（缺乏真实文件的结构复杂性、交叉引用等特性），导致Agent容易出现shortcut行为：未充分验证输入证据就输出看似合理但实际错误的结果。

### 方法关键点
- 3阶段真实源数据合成pipeline：1）从公开语料+O*NET职业活动种子挖掘面向文件的工作流蓝图，无需人工预设；2）搜索并验证公开真实文件作为附件，保留PDF/Word/Excel/PPT多格式、结构不完整、跨文件依赖等真实特性；3）基于工作流和附件合成用户指令、细粒度可交付物级rubric，配套专家执行的参考轨迹和参考输出。
- 两阶段训练：先基于专家轨迹做SFT，学习工具调用和工作流执行逻辑；再用基于rubric的GRPO强化学习优化，仅用可交付物结果奖励不惩罚中间工具调用错误，鼓励探索和错误恢复。

### 关键实验
从10k语料候选合成4k高质量训练实例，训练4B参数的Agent-R2-4B，对比基线包括Qwen3全系列、DeepSeek-v3.1、GLM-4.7、GPT-4.1等：GDPval Pass@1达51.0%，比基线4B模型提升18.6个点，超越235B参数的Qwen3-235B-A22B-Thinking（48.0%）；跨域OfficeQA Pass@1达14.8%，同样超越235B基线的13.8%；有效缓解shortcut行为，输出可追溯数值占比提升7.6个点。

### 最值得记住的一句话
用真实源合成的少量高质量训练数据+rubric驱动的RL，小参数Agent也能在复杂生产力任务上超越远超自身规模的大模型基线。
