---
title: 'MetroLLM-Bench: Evaluating Language Models as Transit Kiosk Runtimes'
title_zh: MetroLLM-Bench：面向地铁自助终端运行时的大语言模型评估基准
authors:
- Remco Hendriks
affiliations:
- Continker
arxiv_id: '2609.10016'
url: https://arxiv.org/abs/2609.10016
pdf_url: https://arxiv.org/pdf/2609.10016
published: '2026-09-08'
collected: '2026-09-11'
category: Eval
direction: LLM工具调用垂直场景评测基准
tags:
- Benchmark
- Tool-Calling
- PEFT
- Edge-LLM
- LLM-Evaluation
one_liner: 推出955用例地铁终端LLM评测基准，验证4B小模型PEFT微调可赶超GPT系列性能
practical_value: '- 做端侧Agent/工具调用落地时，可优先验证4B级小模型PEFT微调方案，Q4量化后仅2.6GB，确定性任务性能可赶超GPT系列，成本远低于大模型调用

  - 垂直场景任务评测可采用分层打分机制：Tier1用确定性规则测核心功能正确性，Tier2用LLM裁判测语义质量，兼顾效率和合理性

  - 垂直场景模型选型可复用结论：2B/4B小模型PEFT微调ROI最高，27B级大模型微调甚至可能出现负收益，无需盲目追大参数'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
传统地铁自助终端的规则逻辑修改需走完整代码发布流程，迭代效率极低；将LLM作为终端策略层替代方案时，缺乏垂直场景下衡量工具调用、结构化输出等核心能力的专业评测基准。
## 方法关键点
1. 构建含955个真实地铁场景用例的基准，覆盖6个真实地铁系统、11类任务（路径规划、票价计算、对抗输入等），要求模型调用结构化工具并输出机器可解析的终端状态；
2. 采用两层打分机制：Tier1为14项确定性指标，Tier2为8项语义质量指标（6项采用LLM裁判）；
3. 75/25拆分训练集和held-out评测集，共测试26款不同厂商的LLM。
## 关键结果数字
PEFT微调的4B Qwen 3.5 Tier1得分91.3，超过GPT-5.6的90.6/90.0，Q4量化后仅2.6GB；9B/27B同系列模型在该场景下无额外性能提升；2B模型PEFT增益达+7.03，27B模型微调增益为-0.91；规则基线Tier1得分84.6。
