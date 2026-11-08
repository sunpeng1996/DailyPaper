---
title: 'HERIT: Enabling Global Access to Hanja-to-English Historical Translation by
  Mitigating Temporal Bias'
title_zh: 《HERIT：缓解时间偏差实现古汉英历史典籍翻译全局可访问》
authors:
- Dayeon Jeong
- Kyeongpil Kang
affiliations:
- Graduate School of Data Science, Kangwon National University
- Department of Computer Science and Engineering, Kangwon National University
arxiv_id: '2611.04949'
url: https://arxiv.org/abs/2611.04949
pdf_url: https://arxiv.org/pdf/2611.04949
published: '2026-11-02'
collected: '2026-11-08'
category: Other
direction: 低资源翻译 · RAG领域适配
tags:
- RAG
- Domain Adaptation
- Pseudo Labeling
- Machine Translation
- Temporal Bias
one_liner: 提出基于RAG生成伪标签的领域适配管线，解决古汉英翻译的时间偏差与数据稀缺问题
practical_value: '- 垂域低资源场景下（如小众品类商品文案生成、跨境电商小语种翻译），可复用「RAG生成高质量pseudo label+领域适配」的范式扩充训练集，降低标注成本

  - 处理时序分布不均的业务数据（如不同周期的用户行为、季节性商品特征）时，可借鉴时序偏差缓解思路避免模型过拟合历史旧数据

  - 跨语种垂域内容处理场景（如文创类古文献衍生品多语言介绍生成、海外用户历史类内容推荐），可参考该管线的低资源适配逻辑'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
历史典籍具备极高的多学科研究价值，但存在严重语言壁垒，人工翻译成本高、周期长；现有机器翻译模型受标注数据稀缺、语料固有时间偏差、垂域语言特殊性限制，效果无法满足落地要求。
### 方法关键点
1. 提出HERIT系统化领域适配管线，基于RAG从海量汉韩对照语料中生成高质量pseudo label数据，大幅扩充训练数据集；
2. 针对性覆盖不同历史时段的语料分布，同时缓解数据稀缺与跨时段时间过拟合问题。
### 关键结果
自动评估与人工评估结果均显示HERIT效果持续优于所有基线模型，已完成此前未翻译的历史档案部分内容翻译，可支撑全球研究者直接访问使用相关资源。
