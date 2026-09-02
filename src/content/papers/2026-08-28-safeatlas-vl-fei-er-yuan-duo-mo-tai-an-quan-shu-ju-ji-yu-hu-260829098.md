---
title: 'SafeAtlas-VL: Beyond Binary Multimodal Safety with Large-Scale Data and Guard
  Models'
title_zh: SafeAtlas-VL：非二元多模态安全数据集与防护模型
authors:
- Zongrui Wang
- Xiangyang Zhu
- Sicheng Wang
- Han Wang
- Dingyi Rong
- Zeyu Zhang
- Chunyi Li
- Yue Shi
- Kaiwei Zhang
- Zicheng Zhang
affiliations:
- Shanghai Jiao Tong University
- Shanghai Artificial Intelligence Laboratory
- East China Normal University
arxiv_id: '2608.29098'
url: https://arxiv.org/abs/2608.29098
pdf_url: https://arxiv.org/pdf/2608.29098
published: '2026-08-28'
collected: '2026-09-02'
category: Multimodal
direction: 多模态大模型 · 内容安全审核
tags:
- Multimodal Safety
- VLM
- Content Moderation
- Dataset
- Benchmark
- Safety Guard
one_liner: 发布1.5M五级标注多模态安全数据集、评估基准及F1超原有SOTA 4%的防护模型
practical_value: '- 电商商品图、UGC内容、Agent交互内容审核可复用五级风险分级+连续风险分输出逻辑，替代二元判断适配不同场景的管控粒度需求，降低误杀漏判

  - 多模态风险样本标注可复用disagreement-aware标注流程，提升歧义样本标注质量，降低标注噪音对模型效果的影响

  - 分级分类审核模型可复用soft cumulative ordinal head结构，同时输出离散风险等级和连续风险得分，灵活适配不同业务阈值调优需求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态安全审核方案多针对单一判断目标做二元决策，跨多模态交互的风险难以横向对比，歧义风险样本被掩盖，无法适配复杂场景下的分级管控需求。
### 方法关键点
1. 构建1.5M训练样本规模的SafeAtlas-VL数据集，覆盖15个危害大类、55个细分子类，对图像、用户请求、模型响应三个维度做五级有序风险标注，采用分歧感知标注流程，混合真实业务和合成数据源；
2. 配套5000样本的SafeAtlas-Bench留验集，支持五级分类预测和连续风险得分的评测；
3. 基于数据集做目标条件微调，训练SafeAtlas Guard系列防护模型，通过soft cumulative ordinal head同时输出五级分类结果和连续风险得分。
### 关键结果
8B参数的防护模型取得整体最优性能，无需使用其他基准的训练集即可实现优异泛化性，F1得分超原有SOTA约4%
