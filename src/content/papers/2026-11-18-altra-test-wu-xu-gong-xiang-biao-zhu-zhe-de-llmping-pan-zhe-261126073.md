---
title: 'AltRA-Test: An Alternative Annotator Test for LLM Judges Without Shared Annotators'
title_zh: 《AltRA-Test：无需共享标注者的LLM评判者替代标注有效性检验方法》
authors:
- Nagham Omar
- Rotem Dror
- Almog Gueta
- Avigdor Gal
- Roi Reichart
- Nitay Calderon
affiliations:
- Technion
- University of Haifa
- Google Research
arxiv_id: '2611.26073'
url: https://arxiv.org/abs/2611.26073
pdf_url: https://arxiv.org/pdf/2611.26073
published: '2026-11-18'
collected: '2026-11-20'
category: Eval
direction: LLM评估 · 标注替代有效性检验
tags:
- LLM-as-Judge
- Statistical Test
- Annotation Efficiency
- IAA
- Evaluation Method
one_liner: 提出无需所有样本共享标注者的统计检验方法，判定LLM替代人类标注的统计合理性
practical_value: '- 做推荐/广告场景的标注降本时，可直接复用AltRA-Test检验当前LLM+Prompt方案是否可替代人工标注，不需要所有样本共享标注者，适配大规模分散标注的业务场景

  - 实测仅需约100条标注样本即可完成检验，小样本验证成本极低，可快速迭代不同LLM、Prompt的标注替代方案ROI

  - 当LLM标注的混合标注组IAA不劣于全人组时即可落地替代，无需追求LLM标注绝对准确率，降低替代阈值，提升降本空间'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM替代人类标注的有效性检验方法仅支持所有样本由同一批标注者标注的密集场景，而大规模标注通常为不同样本由不同标注子集完成，无法适配。
### 方法关键点
AltRA-Test采用bootstrap重采样逻辑：对每个样本抽取k条人类标注，替换1条为LLM标注，生成配对的全人类标注组、人-LLM混合标注组；当混合组的标注者间一致性(IAA)统计上不劣于全人组时，即可判定LLM替代具备统计合理性。
### 关键结果
1. 理论证明为渐近显著性水平α的一致性检验；
2. 覆盖20个多模态数据集、18款LLM、5种Prompt的实验显示，仅需约100条样本即可完成检验；
3. 模拟实验中替代决策正确率优于现有基线，真实场景中约半数设置下LLM可通过检验。
