---
title: Towards Realistic Evaluation of Uncertainty Quantification for LLM-Based Recommender
  Systems
title_zh: 大语言模型推荐系统的不确定性量化真实评估基准
authors:
- Hao Wu
- Sipeng Chen
- Weikai Li
- Tianyi Chen
- Qiancheng Yang
- Hang Zhou
- Yizhou Sun
- Wei Wang
- Xiao Luo
affiliations:
- University of Wisconsin–Madison
- Northwestern University
- University of California, Los Angeles
- The University of North Carolina at Chapel Hill
arxiv_id: '2611.33036'
url: https://arxiv.org/abs/2611.33036
pdf_url: https://arxiv.org/pdf/2611.33036
published: '2026-11-24'
collected: '2026-11-25'
category: RecSys
direction: LLM推荐系统 · 不确定性量化评估
tags:
- LLM4Rec
- Uncertainty Quantification
- Evaluation Benchmark
- Re-ranking
- Reliability
one_liner: 提出固定排序UQ评估基准，对比8种异质信号在LLM推荐场景的监控效果
practical_value: '- 工程上可优先用Top10Mass信号做LLM排序的Error@10故障检测：Llama场景下Error-AUROC达0.628，优于其他标量UQ方法，适合业务高不确定性请求的降级触发

  - 选型UQ方法必须在业务所用LLM backbone上验证：不同backbone下UQ效果排序差异极大，比如Top10Mass在Llama上排第一，在Qwen上仅排第三

  - 做用户历史/商品信息扰动根因诊断可优先用Perturbation Rank Instability信号：其配对控制响应的Source-AUROC达0.675，远优于标量UQ信号，可辅助定位推荐效果劣化原因'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM作为推荐排序器可支持零/少样本排序，但输出排序的可靠性缺乏有效监控手段；现有UQ方法要么介入排序生成过程改变输出，要么从不同维度提取信号，无统一评估范式，无法直接对比选型。

### 方法关键点
- 固定排序评估范式：所有UQ方法基于预生成的固定LLM排序结果做监控，不修改候选顺序，消除排序变动对UQ效果的干扰
- 覆盖两类核心评估任务：一是排序故障检测，判断UQ信号能否识别目标商品不在Top10的Error@10案例；二是配对控制响应一致性，判断UQ信号能否定位是用户历史还是商品文本扰动导致的排序效果下降
- 对比8种异质UQ信号：覆盖概率类、校准类、分解类、扰动敏感类、采样类共5大类UQ方法

### 关键结果
在MIND、Amazon Books、Amazon Movies、Yelp 4个数据集上，基于Llama-3.1-8B-Instruct和Qwen3-8B两个骨干验证：
1. Llama Warm-start场景下，Top10Mass的Error-AUROC达0.628，为所有标量信号最高，相比次优方法高0.082；长尾目标场景下其Error-AUROC下降到0.547，优势大幅收窄
2. 配对控制诊断任务中，Perturbation Rank Instability的Source-AUROC达0.675，比最优标量信号高0.144
3. 不同backbone下UQ方法排序完全不同，Qwen场景下最优方法为Decomposed LLM UQ，Error-AUROC为0.559

最值得记住的结论：没有通用最优的UQ方法，需结合任务类型、所用LLM backbone、业务场景选型，优先选择和监控目标直接对齐的UQ信号
