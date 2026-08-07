---
title: 'HarnessOpt-Bench: Evaluating LLMs at Harness Optimization'
title_zh: HarnessOpt-Bench：大语言模型Harness优化能力评测基准
authors:
- Varun Ursekar
- Apaar Shanker
- Yash Maurya
- Shehab Yasser
- Vijay S. Kalmath
- Veronica Chatrath
- Yuan Xue
affiliations:
- Scale AI
arxiv_id: '2608.06301'
url: https://arxiv.org/abs/2608.06301
pdf_url: https://arxiv.org/pdf/2608.06301
published: '2026-08-05'
collected: '2026-08-07'
category: Eval
direction: Agent Harness优化能力评测
tags:
- LLM
- Agent
- Benchmark
- Harness Optimization
- Evaluation
one_liner: 推出面向高成本随机评估场景的Harness优化评测基准，完成5款前沿大模型的横向能力评测
practical_value: '- 做电商/推荐Agent优化时优先选更强基座模型，模型差异对优化效果的影响是Harness差异的1.8倍，无需过度纠结原生/通用Harness选择，二者无一致优势

  - 优化Agent Harness时优先尝试多维度修改（如prompt、工具调用、上下文管理、重试策略等），修改广度和最终增益强正相关，无需过度消耗算力读详细执行trace

  - 做Agent效果验证必须设独立held-out测试集，开发/验证集最佳得分普遍比测试集高，避免过拟合到评估噪声

  - 内部评估Agent优化能力可复用这套三拆分（dev给trace、val给聚合分、test完全隔离）+可信执行环境的框架，保证结果可复现、防作弊'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent的效果高度依赖Harness（包含prompt、工具、控制流、内存、编排代码的周边层），但业界缺少统一基准评估LLM自动化优化Harness的能力，尤其在评估成本高、反馈有噪声的真实场景下，不同模型、不同Harness的优化效果无法横向对比。

### 方法关键点
- 推出HarnessOpt-Bench基准，包含4类下游任务（OfficeQA、BrowseComp-Plus、Terminal-Bench、GAIA），固定种子Harness、评估预算，采用三数据拆分规则：dev返回执行trace、val返回聚合得分、test全程隔离仅用于最终评分
- 设计可信执行环境，隔离优化器与测试集，严格控制评估预算，记录所有候选版本支持审计，最终以种子Harness为基准的归一化增益作为核心评分指标
- 测试5款前沿LLM（Claude Opus-5、Sonnet-5、GPT-5.6-sol/terra、Kimi K3），分别搭配通用Harness和各模型原生Harness，完成111次有效跑测

### 关键结果
- 模型选择对优化增益的影响是Harness选择的1.8倍，原生Harness无一致优势，20组对比中通用Harness胜出11次
- 最优配置在OfficeQA任务上可捕捉63%的性能提升空间，GAIA任务上最高达到0.49的raw得分
- Harness修改覆盖的维度数与增益强正相关（Spearman ρ最高达0.88），读取详细执行trace的动作与增益负相关

### 核心结论
Harness工程正在成为模型本身的能力，而不仅仅是模型周边的基础设施。
