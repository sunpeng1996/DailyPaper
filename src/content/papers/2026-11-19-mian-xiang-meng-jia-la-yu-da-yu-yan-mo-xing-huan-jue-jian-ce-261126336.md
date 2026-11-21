---
title: 'One Framework to Diagnose Them All: A Stratified Benchmark for Bengali LLM
  Hallucination'
title_zh: 面向孟加拉语大语言模型幻觉检测的分层诊断基准框架
authors:
- Asif Shahriyar Sushmit
- Shefayat E Shams Adib
- Abdullah Al Jubaer Gem
- Ahmed Shafin Ruhan
- MD. Nazmuddoha Ansary
- Biplab Kumar Sarkar
- Syed Rifat Raiyan
- Ajwad Abrar
- Abdullah Bin Hasan
- Adib Sakhawat
affiliations:
- Islamic University of Technology
- Bengali.AI
- North Dakota State University
- Bangladesh University of Engineering and Technology
- BRAC University
arxiv_id: '2611.26336'
url: https://arxiv.org/abs/2611.26336
pdf_url: https://arxiv.org/pdf/2611.26336
published: '2026-11-19'
collected: '2026-11-21'
category: LLM
direction: 大语言模型 · 低资源语言幻觉检测
tags:
- LLM Hallucination
- Low-resource NLP
- Benchmark
- LLM Evaluation
- Bengali LLM
one_liner: 构建跨文化、任务、幻觉类型的三层分层孟加拉语LLM幻觉检测基准
practical_value: '- 小语种跨境电商LLM客服、推荐文案生成等低资源语言场景，可复用「文化距离-任务类型-错误模式」三层分层的幻觉检测数据集构建方法，避免数据集碎片化浪费标注资源

  - 幻觉检测系统评估需设置多阶段分层测试集，单阶段排行榜和两阶段排名相关系数仅0.35的结论可直接复用为评估方案设计参考，避免结果失真

  - LLM作为零样本幻觉裁判时，需重点优化 discourse-level 遗漏类幻觉的识别准确率，同时对预测置信度做校准（最高ECE达0.29）降低误判率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
低资源语言幻觉研究碎片化严重，不同错误模式单独构建数据集导致标注资源浪费，不同研究结果缺乏可比性。
### 方法关键点
提出Alikbachan孟加拉语幻觉检测基准，沿「人工验证的文化距离区间、6类任务、5大类32子类幻觉分类体系」三层交叉分层构建，包含2516条挖掘得到的阶段1测试集，以及5000条配额抽样构建的金标阶段2测试集，配套开源竞赛验证其诊断能力。
### 关键结果
4个零样本LLM裁判在不同分层上macro-F1差异超30个点，裁判整体ROC-AUC达0.74~0.95但置信度校准较差（ECE 0.04~0.29）；单prompt 32B裁判仅达竞赛排名的57百分位；25支参与两阶段竞赛的队伍中24支在阶段2得分平均下降17.6分，两阶段排名Spearman相关系数仅0.35，单阶段排行榜结果长期参考性极低。
