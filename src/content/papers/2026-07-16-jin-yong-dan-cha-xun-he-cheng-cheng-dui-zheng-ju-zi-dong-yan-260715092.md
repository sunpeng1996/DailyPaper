---
title: 'Rubrics on Trial: Evolving Rubrics from a Single Query via Synthetic Pairwise
  Evidence'
title_zh: 仅用单查询合成成对证据自动演化LLM评分规则的框架
authors:
- Haocheng Yang
- Licheng Pan
- Xiaoxi Li
- Zhichao Chen
- Zhiheng Zhang
- Yuan Lu
- Haoxuan Li
- Hao Wang
affiliations:
- National University of Singapore
- Xiaohongshu Inc.
- Zhejiang University
- Peking University
- Shanghai University of Finance and Economics
arxiv_id: '2607.15092'
url: https://arxiv.org/abs/2607.15092
pdf_url: https://arxiv.org/pdf/2607.15092
published: '2026-07-16'
collected: '2026-07-17'
category: Eval
direction: LLM评估规则生成 · 无标注偏好对齐
tags:
- LLM
- Rubric
- Preference Alignment
- Synthetic Data
- LLM Evaluation
one_liner: 仅依赖单查询无标注数据自动生成并校验高区分度的LLM评分规则集
practical_value: '- 电商/Agent场景下的LLM judge自动生成评估维度时，可复用其合成成对响应+校验筛除无效规则的逻辑，大幅减少人工标注成本

  - 推荐系统的文案生成、query改写等AIGC模块的离线评估，可借鉴该框架自动生成场景适配的评分维度，提升评估一致性

  - 做RLHF时如果缺少标注偏好数据，可参考其零标注生成结构化奖励信号的思路，快速适配新业务场景的对齐需求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM训练、评估所需的query专属结构化评分规则（rubric）构建成本高，直接生成的rubric缺乏有效性校验，普遍存在区分度低、仅考核风格、过度适配特殊情况等缺陷，依赖人工标注或偏好数据的方案泛化性差、落地成本高。
### 方法关键点
提出Rubrics on Trial零标注框架，从空集开始迭代演化rubric集，无需外部标注或额外模型训练；仅基于合成的rubric约束成对响应，对每个候选rubric做有效性校验，自动筛除无区分度、过度特异、仅考核风格的无效候选。
### 关键结果
在5个偏好基准测试集上验证效果，平均准确率达SOTA，7个评估集中有6个性能排名第一。
