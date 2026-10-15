---
title: 'MA-Bench: Measuring Operational Planning in Language Models'
title_zh: MA-Bench：大语言模型作战规划能力评测基准
authors:
- Rodney Lafuente-Mercado
- Robert Sincero
- Phil Sage
- Yuan Xue
affiliations:
- Scale AI
- Data Machines
arxiv_id: '2610.19138'
url: https://arxiv.org/abs/2610.19138
pdf_url: https://arxiv.org/pdf/2610.19138
published: '2026-10-12'
collected: '2026-10-15'
category: Eval
direction: LLM开放规划 · 自动评测框架
tags:
- LLM-Evaluation
- Planning-Benchmark
- LLM-as-Judge
- Operational-Planning
- Expert-Rubric
one_liner: 提出首个基于军事任务分析的LLM开放规划能力评测基准，配套专家原子评分规则与校准LLM裁判范式
practical_value: '- 电商开放生成类任务（如活动方案、运营策略、商品卖点文案生成）可借鉴其原子化专家评分规则设计，区分提取、合成、推理三类要求分别加权，避免单一参考答案的偏差

  - LLM自动评测链路可复用其校准流程：先建立人类专家共识基线，要求评测LLM的一致性不低于专家平均水平，同时用跨厂商LLM校验排名稳定性，控制自偏好偏差

  - 复杂多文档Agent（如整合用户、商品、竞品数据的运营决策Agent）的能力评估可参考其错误拆解逻辑，区分内容遗漏和事实错误两类问题，精准定位能力短板'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent/LLM评测多针对有明确可验证结果的任务，而开放规划类任务无唯一正确答案，生成内容的流畅性、逻辑自洽性不代表没有遗漏关键判断、忽略冲突证据等致命问题，缺少针对性评测方案。

### 方法关键点
- 基于美军联合规划流程的任务分析环节设计10个专家构建的仿真场景，每个场景包含10-12份不完整、存在冲突的文档，长度3.6万-24.3万字符
- 配套1257条专家原子评分规则，区分单文档提取（Tier1）、跨文档合成（Tier2）、推理判断（Tier3）三类要求，同时标注重要性等级和负面禁止项，评分完全独立于生成文本的措辞、格式
- 采用校准后的推理LLM作为裁判，裁判仅可见评分规则和待评测输出，不可见原始文档，要求裁判与人类专家的一致性不低于专家之间的平均一致性

### 关键结果
- 评测20款前沿闭源/开源模型，最优模型Muse Spark 1.3仅达到62%的规则正确率，加权得分0.574
- 三类任务正确率分别为Tier1 58.1%、Tier2 49.0%、Tier3 33.4%，60%的错误为内容遗漏而非事实错误，现有模型在需要前瞻性判断的任务上表现最差
- 不同厂商的裁判LLM对模型排名的Spearman相关性达0.89以上，自偏好偏差不超过0.03，评测稳定性高

### 核心结论
开放规划类任务的核心缺陷是「该说的没说」，而非「说的内容错了」，仅靠参考文本相似度、准确率等传统指标会遗漏绝大多数致命问题
