---
title: Calibration and Risk-Budgeted Decisions with System One Models
title_zh: 面向System One模型的校准与风险预算决策框架
authors:
- Soundouss Messoudi
- Youness Mansar
affiliations:
- Heudiasyc - UMR CNRS 7253
- Université de Technologie de Compiègne
- Independent Researcher
arxiv_id: '2610.19811'
url: https://arxiv.org/abs/2610.19811
pdf_url: https://arxiv.org/pdf/2610.19811
published: '2026-10-14'
collected: '2026-10-16'
category: LLM
direction: LLM工作流·风险预算二元决策优化
tags:
- System_One_Model
- Risk_Control
- LTT
- False_Omission_Rate
- Calibration
one_liner: 基于LTT统计框架实现System One模型风险可控阈值选择，将风险超标率从42%降至7.8%
practical_value: '- 可复用LTT阈值选择框架到RAG召回文档过滤、内容安全审核、推荐负样本过滤等不对称风险场景，在严格控制漏判风险的前提下最大化系统效用，避免直接用模型输出概率设阈值的风险超标问题。

  - 轻量级System One决策模型可替代「大模型embedding+小模型分类」的两级流水线，既降低API调用成本，又避免embedding阶段的延迟瓶颈，本地LoRA微调后可覆盖大部分低延迟决策需求。

  - 对于内容审核、敏感词拦截等高风险业务，不要依赖模型宣称的校准能力，必须用独立校准集做阈值的统计验证，优先保证核心风险可控性，再优化过拒率。

  - 冷启动阶段可先用通用System One模型做基线，若LTT无法给出有效阈值，再用少量标注数据微调本地开源小模型，平衡冷启动速度和风险可控性。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
LLM与Agent工作流中存在大量低延迟要求的二元决策场景（如内容审核、prompt注入检测、RAG召回过滤），传统方法要么依赖模型校准假设直接设阈值，易出现严重风险超标；要么引入拒识机制 defer 到人工/大模型，无法适配完全自动化的业务场景，且不对称风险下（漏判代价远高于误判），现有方法无法保证核心风险可控。

### 方法关键点
- 针对不对称风险场景，将核心风险定义为False Omission Rate（FOR，即做出效用最优决策时的漏判率），优化目标为在FOR不超过预设风险预算的前提下，最大化效用最优决策的覆盖比例，最小化过拒/上下文冗余。
- 采用Learn Then Test（LTT）统计框架，基于独立校准集的有限样本做二项分布假设检验，选择最大的可认证阈值，保证FOR超标的概率不超过预设统计误差δ，无需依赖模型的校准能力。
- 对比三类阈值策略：Naive（直接设阈值为风险预算α，假设模型完全校准）、Empirical（选校准集上FOR≤α的最大阈值，无统计保证）、LTT（带统计保证的阈值选择）。

### 关键结果
在6个数据集（内容审核、prompt注入检测、Agent轨迹安全、RAG重排序）上对比8个模型，结果显示：Naive策略风险超标率达42%，平均超标7.09个百分点，极端场景下超标73.26个百分点；Empirical策略超标率达51.7%，平均超标1.17个百分点；LTT策略仅7.8%的场景超标，平均超标0.1个百分点。本地LoRA微调的0.8B开源System One模型推理延迟仅98ms/请求，成本0.003美元/千次，比「8B大模型embedding+岭回归分类」流水线延迟降低98%，效果与商用System One模型相当。

### 核心结论
不要相信任何模型宣称的「天然校准」，高风险自动化决策必须用统计方法做风险认证，而非直接用模型输出概率设阈值。
