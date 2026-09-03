---
title: 'RealSWE: A Compositional Evaluation of Coding Agents under Realistic User
  Requests'
title_zh: RealSWE：面向真实用户请求的编码Agent组合式评估框架
authors:
- Gyuhyeong Kim
- Hyojung Gwon
- Jeonghyeon Kim
- Kyuhong Shim
- Sunjae Lee
affiliations:
- Sungkyunkwan University
arxiv_id: '2608.27831'
url: https://arxiv.org/abs/2608.27831
pdf_url: https://arxiv.org/pdf/2608.27831
published: '2026-08-30'
collected: '2026-09-03'
category: Agent
direction: Agent 编码智能体评估优化
tags:
- Coding Agent
- Agent Evaluation
- Benchmark
- LLM4Code
- Prompt Engineering
one_liner: 构建贴合真实用户输入的编码Agent评估基准，量化信息构成与风格对性能的影响
practical_value: '- 做业务Agent效果评估时，需基于真实用户请求分布构建测试集，避免使用人工构造的规整prompt，否则会高估实际落地性能，甚至错误选择效果更差的模型

  - 优化Agent的前置引导或多轮澄清逻辑时，优先引导用户补充高价值信息：问题类需求明确期望行为，需求类明确动机，复现步骤、环境信息等低价值内容可降低收集优先级

  - 做prompt优化时无需过度纠结正式/口语化等风格差异，核心要确保关键信息的覆盖度，内容比表达形式对效果的影响大得多'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent基准基于规整的GitHub issue构建，输入信息完整、风格正式，与真实用户短、信息稀疏、口语化的请求存在显著gap，导致基准评估结果高估实际落地性能，也无法定位影响Agent表现的核心因素。
### 方法关键点
- 构建6类信息分类体系（问题描述、期望行为、复现步骤等）和4维语言风格维度，量化SWE-CHAT真实请求与SWE-BENCH基准的分布差异
- 基于SWE-BENCH VERIFIED/PRO生成381组多变体任务族：同任务底层逻辑、金标补丁一致，仅信息构成、语言风格可变
- 发布两类产物：贴合真实用户分布的固定评估集RealSWE-BENCH，支持自定义信息/风格配置的消融实验框架RealSWE-FRAMEWORK
### 关键结果
- 7个主流LLM在RealSWE-BENCH上的平均分辨率比原SWE-BENCH低6.4pp，模型排名发生变化，单任务成本平均上升6.2%
- Bug修复任务中补充期望行为可提效+8pp，功能请求任务中补充动机最高提效+7pp；而复现步骤、环境信息对性能无显著增益，语言风格仅带来模型相关的小幅波动
### 核心结论
Agent任务中，请求的信息内容优先级远高于表达形式，精准补全高价值信息的收益远高于增加冗余信息、优化措辞。
