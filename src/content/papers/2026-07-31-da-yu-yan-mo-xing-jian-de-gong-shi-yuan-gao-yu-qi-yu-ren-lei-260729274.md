---
title: Language Models Agree With Each Other, Not With Readers
title_zh: 大语言模型间的共识远高于其与人类读者的共识
authors:
- Kazuki Nakayashiki
- Keisuke Watanabe
affiliations:
- Glasp Inc.
arxiv_id: '2607.29274'
url: https://arxiv.org/abs/2607.29274
pdf_url: https://arxiv.org/pdf/2607.29274
published: '2026-07-31'
collected: '2026-08-03'
category: LLM
direction: 大语言模型共识度度量与对齐研究
tags:
- LLM Evaluation
- Human Alignment
- Model Convergence
- Human Preference
- Text Analysis
one_liner: 用真实读者自发高亮数据证实大模型间共识度达人类读者间的2.3倍，规模越大共识越高
practical_value: '- 做LLM生成内容的人类偏好对齐时，需避免使用实验诱导的标注数据，优先用用户自发行为（如电商详情页高亮、好评重复提及内容）作为真实偏好基准，减少标注偏差

  - 多模型集成生成推荐文案、商品卖点时，优先选择小模型做多样性生成，大模型共识度过高会导致内容同质化严重，降低用户新鲜感

  - 做LLM生成效果评估时，不能仅用多模型间的共识度作为评估指标，其与真实人类偏好的相关性远低于预期，需补充真实用户反馈校准'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
过往大模型同质化研究采用实验诱导的人类标注数据，标注者受模型prompt干扰，结果存在人工偏差，无法反映真实人类共识水平。
### 方法关键点
采用120篇网页文档上2523组读者自发高亮数据（默认关闭他人高亮显示，无实验诱导），以匹配长度、深度的句子集重叠度减去随机重采样预期重叠度作为共识度度量指标，对比18款不同厂商、不同规模大模型的共识差异。
### 关键结果数字
人类读者间共识度为0.040，大模型间共识度中位数达0.093（是人类的2.3倍），头部大模型间共识度达0.203，为人类的5.1倍、GPT-4o自身重复调用共识度的2倍；小模型间共识度与人类接近，无模型与读者的共识度显著高于人类间共识度；后续新发布的4款模型测试结果均符合预设预测，未超出人类共识区间。
