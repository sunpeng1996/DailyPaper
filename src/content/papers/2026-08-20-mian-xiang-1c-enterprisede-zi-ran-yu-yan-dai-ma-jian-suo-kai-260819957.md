---
title: 'Natural Language Code Retrieval for 1C:Enterprise: An Open Benchmark and Efficient
  Bi-Encoder'
title_zh: 面向1C:Enterprise的自然语言代码检索：开源基准与高效双编码器
authors:
- Konstantin Chesnokov
- Chingiz Mingazov
affiliations:
- Independent Researcher, Moscow, Russia
- Independent Researcher, Kazan, Russia
arxiv_id: '2608.19957'
url: https://arxiv.org/abs/2608.19957
pdf_url: https://arxiv.org/pdf/2608.19957
published: '2026-08-20'
collected: '2026-08-21'
category: Other
direction: 代码检索 · 领域专用双编码器优化
tags:
- Code Retrieval
- Bi-Encoder
- Matryoshka Representation Learning
- Benchmark Dataset
- Dense Retrieval
one_liner: 针对1C:Enterprise领域缺检索基准的痛点，开源专用数据集与基于MRL优化的高效双编码器
practical_value: '- 垂直领域缺标注数据时，可调用大模型生成大规模合成三元组做预训练/微调，大幅降低标注成本，该方案可复用到电商垂类商品检索、Agent工具检索等场景

  - 采用Matryoshka Representation Learning做向量降维，256维即可保留99.9%的检索效果，同时将稠密索引存储、相似度计算量降低为原来的1/3，可直接用于向量召回、RAG检索的性能优化

  - 做领域效果评估时，可采用平衡子集macro、查询加权micro、垂直场景子集三类指标交叉验证，同时通过n-gram重叠审计排查训练测试集泄露问题，避免结果虚高'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
1C:Enterprise是俄语区主流企业软件，其代码检索同时涉及俄语文法与高度领域化财会/开发术语，此前无公开基准数据集与专用检索模型，小领域标注数据稀缺问题突出。
### 方法关键点
1. 开源3413条经过PII脱敏的真实查询-代码对基准与可复现评估框架；2. 基于公共代码仓库用gemma-4-26B-A4B-it生成78.4万条合成三元组解决标注不足问题，微调时引入MRL与隐私感知分词器；3. 采用多维度评估指标，同时做13-gram重叠审计排除训练测试泄露干扰。
### 关键结果数字
模型平衡macro nDCG@10达0.5992，优于基线架构的0.4932与google/embeddinggemma-300m的0.5404；MRL截断到256维时仅损失0.1%检索效果，存储与相似度计算量降低2/3；移除重叠样本后指标无明显下降，验证结果可信度。
