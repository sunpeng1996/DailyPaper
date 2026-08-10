---
title: 'Measuring Concept Content in Text from LLM Activations: ESG Evidence from
  Concept Vectors and Linear Probes'
title_zh: 从LLM激活值衡量文本概念内容：基于概念向量与线性探测的ESG实证
authors:
- Luc Hazenoot
- Zhaochun Ren
- Amirhossein Zohrehvand
affiliations:
- Leiden Institute of Advanced Computer Science, Leiden University
arxiv_id: '2608.07208'
url: https://arxiv.org/abs/2608.07208
pdf_url: https://arxiv.org/pdf/2608.07208
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: LLM内部知识提取 · 文本概念度量
tags:
- LLM Activation
- Linear Probe
- Concept Extraction
- ESG Classification
- RFM
one_liner: 利用冻结LLM内部激活值做文本概念度量，性能接近微调分类器且优于模型直接输出
practical_value: '- 电商商品/评论合规性、属性标签识别场景，可直接用冻模LLM激活加轻量线性探测替代微调，节省标注训练成本，性能接近域内微调模型

  - 搜索Query隐式意图识别、商品卖点挖掘等需判断概念强度的场景，可复用RFM生成连续概念得分，无需依赖人工标注分级标签

  - Agent做长文本理解（用户评论、商品详情页摘要）时，可通过提取激活值获取模型未显式输出的隐式概念信息，提升理解准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有文本概念度量方法仅依赖表层文本特征（词频、嵌入相似度等），无法还原读者对文本的隐含判断，且LLM显式输出内容与内部存储知识存在gap，任务特定微调成本高。
### 方法关键点
采用开箱即用的冻结LLM，分别通过Recursive Feature Machine（RFM）算法提取概念向量、线性探测两种方法挖掘内部激活值的概念信息，对比表层特征基线、嵌入基线、LLM直接回答三类方案。
### 关键结果
在ESG人工标注数据集上，最优线性探测方案精度仅比域内微调分类器低0.6个百分点，无需任何任务微调；12组对比中11组优于同LLM的直接回答，证明激活值包含显式响应未上报的概念信息；线性探测性能优于RFM，但RFM可输出连续概念强度得分，适配分级判断场景。
