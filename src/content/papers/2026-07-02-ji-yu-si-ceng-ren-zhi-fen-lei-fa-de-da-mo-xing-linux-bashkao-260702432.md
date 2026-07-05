---
title: 'Automated grading of Linux/bash examinations using large language models:
  a four-level cognitive taxonomy approach'
title_zh: 基于四层认知分类法的大模型Linux/bash考试自动评分方案
authors:
- Manuel Alonso-Carracedo
- Ruben Fernandez-Boullon
- Pedro Celard
- Francisco J. Rodriguez-Martinez
- Lorena Otero-Cerdeira
affiliations:
- Universidade de Vigo, Department of Computer Science
- IFCAE-Institute for Research in Physics, Computing and Aerospace Science, Universidade
  de Vigo
arxiv_id: '2607.02432'
url: https://arxiv.org/abs/2607.02432
pdf_url: https://arxiv.org/pdf/2607.02432
published: '2026-07-02'
collected: '2026-07-05'
category: LLM
direction: 大模型自动评分 · 认知分类框架
tags:
- LLM
- Automated Grading
- Prompt Engineering
- Cognitive Taxonomy
- Evaluation Protocol
one_liner: 基于四层认知分类法测试四款前沿LLM的Linux/bash考试评分效果，给出优化方案与适用边界
practical_value: '- 做用户生成内容质量、Agent任务完成度、推荐文案效果等评估类任务时，可参考按认知复杂度分层的框架，提前预判LLM评分准确率边界，分层配置人机校验规则

  - 结构化评分规则注入prompt的效果远优于切换不同LLM供应商，业务侧做LLM评估类任务时优先优化prompt的规则清晰度，而非盲目更换大模型

  - 可复用本文多维度量化人机对齐度的评估协议（ICC/MAE/偏差），快速迭代自家LLM应用的prompt版本'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
计算类教育大规模招生下人工评分扩展性差，传统规则式自动评分无法处理等价答案、语法变体、部分得分场景，亟需高可靠性的自动化评分方案。
### 方法关键点
采用结合认知复杂度与操作影响的四层认知分类法（L1信息检索到L4高级系统管理），测试GPT、Claude Opus、Gemini、GLM四款前沿LLM，对比无引导基线prompt、评分规则增强prompt的效果，在1200份计算机专业大二学生真实作答数据集上验证，金标准为3名专家独立标注结果。
### 关键结果数字
带评分规则引导的Gemini 3.0 Pro取得最高人机对齐度：ICC(3,1)=0.888，MAE=0.10，Bland-Altman偏差=-0.014；对齐度随分类层级提升持续下降，高难度层级偏差最大；评分规则质量的影响远大于LLM厂商选择，结构化prompt可稳定提升对齐度
