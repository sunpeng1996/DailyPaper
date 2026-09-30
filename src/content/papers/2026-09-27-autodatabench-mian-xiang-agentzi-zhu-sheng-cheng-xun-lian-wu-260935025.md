---
title: 'AutoDataBench: Can Agents Write the Data That Feeds the Self-Improvement Loop?'
title_zh: AutoDataBench：面向Agent自主生成训练任务的评测基准
authors:
- Haotian Luo
- Haoyu Wang
- Zeyu Qin
- Huanjin Yao
- Yibo Wang
- Zhuotao Tian
- Shuai Wang
- Jiaya Jia
affiliations:
- HKUST
- SLAI
- NTU
arxiv_id: '2609.35025'
url: https://arxiv.org/abs/2609.35025
pdf_url: https://arxiv.org/pdf/2609.35025
published: '2026-09-27'
collected: '2026-09-30'
category: Eval
direction: Agent 训练数据合成能力评测
tags:
- Agent
- Synthetic Training Data
- Benchmark
- Recursive Self-Improvement
- Evaluation
one_liner: 提出首个按工业数据生产标准评测Agent生成可执行训练任务能力的基准，验证当前Agent效率仍低
practical_value: '- 生成电商/推荐/广告业务训练样本时，可复用「单样本先过有效性/难度/行为覆盖度三道校验再进训练集」的流程，避免无效样本浪费训练资源，比如生成用户行为模拟任务时先校验难度落在目标模型通过率12.5%-75%区间，确保样本有训练价值

  - 用Agent合成业务训练数据时，可优先按领域选择对应Agent，不要使用统一的通用Agent，不同领域Agent生成数据的表现差异极大，比如电商运营自动化任务和搜索Query改写任务要适配不同基座Agent

  - 业务冷启动缺训练数据时，给Agent更长的运行时间预算，高质量样本的单位成本几乎不变但产出量线性提升，比如给3倍时间预算可获得3倍量可用样本，单位成本波动<10%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM能力提升更多来自数据而非架构，Agent训练所需的可执行任务仍依赖人工编写，成本高、难以随算力扩展，是递归自改进循环的核心瓶颈。现有评测方法多通过训练后模型效果反推数据质量，不符合工业数据生产逐样本验收的实际流程，缺少直接评测单条训练任务是否符合生产标准的基准。

### 方法关键点
- 评测单元为单条任务生成episode：给定原始基准任务+目标模型尝试该任务的行为日志，要求Agent生成同领域新任务，全程无需训练目标模型
- 打分由三个维度乘积得到：① gate校验：排查任务无效、复制原题、无区分度等8类致命缺陷，存在即得0分；② 难度校验：目标模型通过率落在[0.125, 0.75]区间得1分，否则0分；③ 质量分：新任务覆盖目标模型原有错误行为模式的比例，达到60%即得满分
- 覆盖3类任务域：终端操作、软件工程、科学计算、业务流程自动化共24个原始任务，目标模型固定为deepseek-v4-pro，评分由固定的claude-opus-5执行

### 关键结果
- 5款主流前沿Agent在默认45分钟预算下得分均低于0.2（满分1），核心瓶颈是难度校准：仅14.6%~25%的生成任务落在有效难度区间，通过校验的任务模式覆盖率可达70%~96.7%
- 给最强Agent kimi-k3 4倍时间预算（180分钟），得分提升2.9倍至0.541，单条可用任务成本仅从11.88美元升至12.62美元，效率几乎不变
- 不同Agent在不同领域表现差异极大，无通用最优Agent

> 最值得记住的一句话：当前Agent已经能生成符合质量要求的训练任务，但难度校准是最大效率瓶颈，给Agent更长运行时间可线性提升产出而几乎不增加单位成本。
