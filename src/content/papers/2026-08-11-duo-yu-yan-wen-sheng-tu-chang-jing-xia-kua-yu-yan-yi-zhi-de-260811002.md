---
title: On the Limitations of Cross-Lingual Consistency in Multilingual Text-to-image
  Generation
title_zh: 多语言文生图场景下跨语言一致性的局限性研究
authors:
- Sicheng Zhang
- Zhonghao Yan
- Binzhu Xie
- Shi Qiu
- Muzammal Naseer
- Naveed Akhtar
- Mubarak Shah
affiliations:
- Khalifa University
- Queen Mary University of London
- The Chinese University of Hong Kong
- The University of Western Australia
- The University of Melbourne
arxiv_id: '2608.11002'
url: https://arxiv.org/abs/2608.11002
pdf_url: https://arxiv.org/pdf/2608.11002
published: '2026-08-11'
collected: '2026-08-12'
category: Multimodal
direction: 多模态文生图 · 跨语言基准评测
tags:
- Text-to-Image
- Cross-Lingual
- Benchmark
- Multimodal
- Evaluation
one_liner: 推出覆盖10种语言33K prompt的LingT2I基准，揭示多语言文生图的语言不平等与文化影响
practical_value: '- 跨境电商/多区域营销场景下的AI商品图、营销素材生成，可直接复用LingT2I基准测试不同语种prompt的生成效果，优先保障高流量语种的生成精度

  - 多语种广告素材生成流程中，需额外对齐prompt语种对应的当地文化语境，避免生成不符合用户认知的素材降低点击率与转化率

  - 自定义微调多语言文生图模型时，可参考论文揭示的语种依赖性能权衡规律，针对性补充小语种的prompt-图片训练对，缩小跨语言性能gap'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有文生图技术迭代与评测基本基于英语场景，跨语种生成性能差异、语言/文化对输出的影响缺乏系统评估框架，难以支撑公平包容的多语言文生图产品落地。
### 方法关键点
构建LingT2I公开评测基准，覆盖10种全球主流语言、总计33K条标注prompt，同时覆盖内容生成一致性、文本渲染准确率两类核心评测维度；基于该基准开展系统性多维度分析，挖掘语言属性、对应文化语境对生成结果的作用规律。
### 关键结果
验证多语言文生图存在显著的语种间性能不平等，不同语种在各评测维度上存在差异化的权衡关系，语言与文化因素会系统性影响模型输出效果。
