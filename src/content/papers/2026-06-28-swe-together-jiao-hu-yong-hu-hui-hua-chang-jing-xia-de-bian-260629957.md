---
title: 'SWE-Together: Evaluating Coding Agents in Interactive User Sessions'
title_zh: 《SWE-Together：交互用户会话场景下的编码Agent评估基准》
authors:
- Yifan Wu
- Zhuokai Zhao
- Songlin Li
- Ho Hin Lee
- Jiacheng Zhu
- Shirley Wu
- Tianhe Yu
- Serena Li
- Lizhu Zhang
- Xiangjun Fan
affiliations:
- Meta
arxiv_id: '2606.29957'
url: https://arxiv.org/abs/2606.29957
pdf_url: https://arxiv.org/pdf/2606.29957
published: '2026-06-28'
collected: '2026-07-01'
category: Eval
direction: Agent 多轮交互能力评估基准
tags:
- Coding Agent
- Multi-turn Benchmark
- Interactive Evaluation
- User Simulator
- LLM Agent
one_liner: 构建基于真实多轮编码交互的Agent评估基准，配套用户模拟器，同时评估结果正确性与交互成本
practical_value: '- 搭建业务场景智能助手（如运营代码助手、客服Agent）的评估体系时，可复用「最终结果正确率+交互反馈轮数」的双维度框架，更贴合真实用户体验

  - 多轮交互Agent的效果复现可借鉴基于真实会话构建的LLM用户模拟器方案，保留原始用户意图的同时大幅降低真人测试成本

  - 从真实交互日志筛选评估用例时，可参考「可复现场景状态、明确用户目标、可观测结果」三个筛选标准，保障benchmark可落地'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent基准均为静态单轮模式，仅向Agent输出完整任务描述后评估最终代码质量，完全不匹配真实场景下用户多轮澄清目标、补充约束、修正错误的交互特性，无法衡量真实协作体验。
### 方法关键点
1. 从11260条真实用户-Agent编码会话中，筛选出109个具备可复现仓库状态、清晰用户目标、可观测结果的仓库级任务，构建多轮评估基准SWE-Together；
2. 搭建反应式LLM用户模拟器，严格保留原始用户意图，在Agent任务推进过程中按需提供反馈，支持不同Agent的会话复现；
3. 采用双维度评估：同时衡量最终仓库正确性、交互过程中所需的纠错反馈轮数。
### 关键结果
前沿编码Agent实验显示，能力越强的Agent最终成功率越高，同时所需的人工干预轮数越少，对应更优的用户体验。
