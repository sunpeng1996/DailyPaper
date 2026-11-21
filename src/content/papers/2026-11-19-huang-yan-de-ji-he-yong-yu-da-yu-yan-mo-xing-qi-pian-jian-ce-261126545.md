---
title: 'The Geometry of Lies: Knowledge and Persona Directions for Detecting Deception
  in Large Language Models'
title_zh: 《谎言的几何：用于大语言模型欺骗检测的知识与人格方向》
authors:
- Md. Abdullah Al Zami
- Suraiya Shanaz
- Mahdi Hasan
- Shoaib Ahmed Dipu
- Farig Yousuf Sadeque
- Md. Sabbir Ahmed
affiliations:
- Department of Computer Science and Engineering, BRAC University, Dhaka, Bangladesh
arxiv_id: '2611.26545'
url: https://arxiv.org/abs/2611.26545
pdf_url: https://arxiv.org/pdf/2611.26545
published: '2026-11-19'
collected: '2026-11-21'
category: LLM
direction: 大模型对齐 · 欺骗行为检测
tags:
- LLM
- Deception Detection
- Linear Probe
- Representation Engineering
- Alignment
one_liner: 扩增人格库构建人格与知识隐空间方向，提升跨类型大模型欺骗检测性能，优于单数据集线性探针
practical_value: '- 电商Agent/导购机器人对齐场景，可复用无监督表示方向探针方案，替代高成本标注训练的分类器，降低虚假回复/隐瞒信息的检测成本

  - 涉及未授权信息拒答的业务场景，可参考知识方向构造方法，区分Agent故意隐瞒信息与真的未知的相同拒答表述，提升合规性

  - LLM驱动的商品评价/营销内容审核场景，可在模型中间层提取人格+知识特征组合，提升跨品类虚假宣传内容的泛化检测能力'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有Linear probe作为低成本LLM谎言检测器泛化性差，跨谎言类型失效；70B规模大模型上无标注角色诱导的检测方向未验证，知识类谎言与诚实否认表述完全一致，现有方案无法区分。
### 方法关键点
1. 扩增公开人格库，加入刻意隐瞒已知知识的角色及对应诚实对照组，提取人格方向区分诚实/欺骗角色回复
2. 构造知识方向：对比模型可回答与不可回答问题后的相同否认表述，解耦表述一致性下的意图差异
### 关键结果
在Liars' Bench的4款大模型中，人格方向在3款上的谎言排序性能优于单数据集探针；人格+知识方向组合在全部4款模型上性能优于同层监督探针，其中2款可有效区分表述完全一致的知识类谎言与诚实否认。
