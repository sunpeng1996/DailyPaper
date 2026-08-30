---
title: 'Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners'
title_zh: 超越F1：AI模型安全扫描器的覆盖度与故障恢复能力评估
authors:
- Qianlong Lan
- Vinothini Pandurangan
- Anuj Kaul
- Indranil Sanyal
affiliations:
- eBay Inc.
arxiv_id: '2608.27424'
url: https://arxiv.org/abs/2608.27424
pdf_url: https://arxiv.org/pdf/2608.27424
published: '2026-08-27'
collected: '2026-08-30'
category: Eval
direction: AI模型安全工具评测
tags:
- Model Security
- Static Analysis
- Benchmark
- Evaluation Metrics
- Supply Chain Security
one_liner: 基于170份PyTorch/Pickle样本基准评测3款模型安全扫描器，提出更全面的安全工具评估维度
practical_value: '- 自研/引入LLM/推荐模型安全扫描工具时，不能仅用F1等准确率指标，需新增覆盖度、故障恢复、无有效输出占比等可用性维度评估

  - 多工具冗余部署时，优先验证各工具在对方失效样本集上的检测能力，避免无价值的重复选型，降低运维成本

  - 内部模型供应链管控流程中，需补充对畸形序列化样本的容错检测逻辑，避免扫描器崩溃导致恶意样本漏防'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有AI模型安全静态扫描器的评估仅关注输出有效安全判断的样本，忽略无有效输出的覆盖度、故障恢复等核心能力，无法支撑生产环境工具选型。

### 方法关键点
构建包含170份Pickle、PyTorch格式样本的基准测试集，覆盖145个样本族，其中135个有安全真值、10个为无标签畸形样本；评测时明确区分有效覆盖、分析完成、明确安全判断、非安全发现、不支持输出五类结果。

### 关键结果
标注样本集上ModelAudit明确判断率100%，Fickling为81.5%，ModelScan为49.6%；ModelScan在输出明确判断的样本上F1、精确率、召回率均达100%；Fickling无独立于另外两款工具的独有检出样本；ModelScan分析失败的48个恶意样本，另两款工具均能正确检出。
