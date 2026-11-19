---
title: Can Programs Replace LLM Judges? Executable Program Judges for Scalable and
  Efficient Relevance Labeling
title_zh: 可执行程序判分器：替代LLM判分器实现高效可扩展相关性标注
authors:
- Eugene Agichtein
- Charles L. A. Clarke
- Kaustubh Dhole
- William Stern
affiliations:
- Emory University
- University of Waterloo
- Stanford University
arxiv_id: '2611.24849'
url: https://arxiv.org/abs/2611.24849
pdf_url: https://arxiv.org/pdf/2611.24849
published: '2026-11-18'
collected: '2026-11-19'
category: Eval
direction: 相关性标注 · LLM生成可执行判分程序
tags:
- LLM Judge
- Relevance Labeling
- Program Synthesis
- Efficient Annotation
- Retrieval Evaluation
one_liner: 用LLM生成主题级可执行标注程序，替代逐文档LLM判分，成本低可解释且精度相当
practical_value: '- 电商搜索/推荐相关性标注场景可复用该思路：当单query标注量超过200条时，用LLM生成query级可执行标注程序，成本低于逐文档LLM判分，且仅需CPU运行无GPU开销

  - 合规性标注场景（如广告相关性审核）可直接复用可解释性设计：生成的程序规则可人工审核、修改，解决LLM判分黑盒不可追溯的问题，满足监管要求

  - 少样本标注场景优先选择规则生成而非小模型训练：单query仅能获取3~16条标注时，引导LLM基于样本生成标注规则，效果优于训练单query LoRA分类器，样本利用效率更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM判分器已成为检索/推荐系统相关性标注的主流方案，但存在三大痛点：逐文档调用大模型成本随标注量线性增长、判分逻辑黑盒不可解释、结果不可复现，且易被内容注入攻击。现有少样本训练分类器的方案则存在小样本下拟合效果差、过拟合等问题，亟需低成本、可解释、可扩展的标注方案。
### 方法关键点
- ExecJudges框架调用一次前沿LLM（如Claude Opus 5.5）为每个查询/主题生成3份独立的可执行Python判分程序，程序仅使用正则匹配、词干提取、BM25计算等轻量确定性操作，无后续LLM调用
- 程序按照官方标注规范输出on_subject、some_answer等4个维度的判定结果，通过固定公式映射为相关性等级，多份程序的判分结果取平均向下取整得到最终标注，降低单程序的错误率
- 少样本增强版ExecJudges-L可注入3~16条该主题的人工标注样本，引导LLM生成更贴合标注规则的程序，无需训练模型
### 关键实验结果
在7个TREC公开检索数据集上对比Claude Sonnet 5.5 LLM判分器、单主题LoRA分类器等基线：无标注的ExecJudges与NIST人工标注的Krippendorff’s α达0.483~0.653，和Claude Sonnet 5.5判分精度相当；仅加入16条人工标注的ExecJudges-L α提升0.096~0.166，在所有数据集上精度均超过同标注量下训练的LoRA分类器，部分数据集超过同标注量的LLM判分器；生成的程序标注结果对TREC官方参赛系统的排序Kendall’s τ达0.87~0.94，和人工标注的排序一致性极高；单主题生成程序的固定成本仅为$0.17~0.49，标注量超过200条/主题时成本低于LLM逐文档判分。
### 核心结论
对于批量相关性标注场景，将LLM的推理能力从逐文档判分迁移到规则生成层面，可在保持精度相当的前提下大幅降低成本、提升可解释性
