---
title: 'AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM
  Evaluation and Error Diagnosis'
title_zh: AMLworld-Compact：基于重要性加权降采样的低成本LLM评测与错误诊断
authors:
- Natapong Nitarach
- Phume Ngampornsukswadi
- Pittawat Taveekitworachai
- Surapon Nonesung
- Warit Sirichotedumrong
- Kunat Pipatanakul
affiliations:
- SCB DataX, SCBX Group
- Independent Researcher
arxiv_id: '2610.13627'
url: https://arxiv.org/abs/2610.13627
pdf_url: https://arxiv.org/pdf/2610.13627
published: '2026-10-09'
collected: '2026-10-13'
category: Eval
direction: LLM评测 · 降采样优化
tags:
- LLM Evaluation
- Importance Sampling
- Cost Reduction
- Error Diagnosis
- Dataset Construction
one_liner: 提出HT-Coreset降采样协议构建轻量评测集，大幅降低LLM反洗钱交易检测任务的评测成本
practical_value: '- 大模型业务评测降本可复用HT-Coreset思路：保留全部高价值样本（如风险case、bad case），按模型预测置信度分层抽样普通样本，用Horvitz-Thompson权重修正指标，保证结果无偏

  - 海量召回/排序模型离线评测可参考该降采样逻辑：无需全量打分，分层抽样即可得到接近全量的指标估计，大幅降低评测算力消耗

  - LLM输出正确性校验不要仅依赖lexical checks：实测错误结果也有56%的lexical通过率，合规校验、文案生成等场景需增加规则+语义双重校验逻辑'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM在AMLworld反洗钱交易检测任务评测成本极高，单条交易需对应独立graph prompt，全量百万级样本评测开销大；普通均匀采样或平衡子集采样会导致precision、F1等指标结果有偏。
### 方法关键点
提出HT-Coreset协议构建AMLworld-Compact评测集，保留全部非法交易样本，对合法交易按监督得分分层抽样，配合Horvitz-Thompson权重修正指标，得到无偏的全量测试集指标估计。
### 关键结果
- 评测样本量在HI-Small、LI-Small数据集上分别压缩271倍、611倍
- F1的RMSE仅0.00-2.58个百分点，远低于带HT权重均匀采样的4.44-7.41
- 7个开源LLM的加权precision接近全预测为非法的基线水平，错误输出仍有56.2%可通过lexical校验
