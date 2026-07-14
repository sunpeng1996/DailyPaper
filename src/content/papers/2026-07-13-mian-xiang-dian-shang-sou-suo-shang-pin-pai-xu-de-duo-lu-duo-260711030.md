---
title: 'MMRM: A Multiplex Multimodal Representation Model for Product Ranking in E-commerce
  Search'
title_zh: 面向电商搜索商品排序的多路多模态表征模型MMRM
authors:
- Zhen-Lin Chen
- Maosen Sheng
- Peng Lin
- Jianmin Chen
- Zhuojian Xiao
- Dongyue Wang
- Xiwei Zhao
affiliations:
- JD.COM
arxiv_id: '2607.11030'
url: https://arxiv.org/abs/2607.11030
pdf_url: https://arxiv.org/pdf/2607.11030
published: '2026-07-13'
collected: '2026-07-14'
category: RecSys
direction: 多模态推荐 · 多任务排序表征学习
tags:
- Multimodal Representation
- Contrastive Learning
- Multitask Learning
- E-commerce Search
- Ranking Model
one_liner: 基于MLLM统一对齐四类异构协同信号，生成解耦的多路多模态表征提升多任务排序效果
practical_value: '- 多模态MLLM微调时可引入q2i点击、i2i点击/加购/下单四类异构协同信号，配合任务专属token与投影层，一次推理即可输出多路解耦表征，避免多模型推理的算力浪费

  - 构建i2i对比学习数据集时，可基于行为时间窗口构建商品图，采样一二阶邻居作为正例、同子类商品作为硬负例，同时采用word2vec式降采样缓解热门商品偏差

  - 多任务排序模型侧可对应多路表征构建任务专属的用户行为序列建模模块，将任务专属用户表征输入对应任务塔，缓解多任务下的表征纠缠问题

  - 大参数MLLM做对比学习时可引入GradCache扩大batch size，在单H800上即可支持4B参数模型batch size到4096，有效提升对比学习效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有电商多模态排序方案仅用单一协同信号微调MLLM，无法适配CTR/ACR/CVR等多任务排序所需的异构信号；且多模态表征仅作为常规特征输入排序模型，未充分挖掘其在用户行为建模中的价值，易出现表征纠缠、多任务效果相互拖累的问题。
### 方法关键点
- 数据层：构建4类对比学习数据集，含q2i点击（query-商品点击对）、i2i点击/加购/下单（按10min/30min/7d行为窗口构建商品图，采样一二阶邻居为正例、同子类商品为硬负例），单类数据集规模达0.3B
- 表征层：MMRM基于Qwen3-VL-4B初始化，共享MLLM主干，新增[SEARCH]/[CLICK]/[CART]/[ORDER]4个任务专属token与对应投影层，单次推理即可输出4路解耦的多模态表征；训练时混合4类数据集，各任务仅用对应正例计算对比损失，其他任务样本作为batch内负例
- 排序层：多任务排序模型基于4路表征分别做软搜索筛选用户行为序列，通过多头目标注意力生成任务专属用户表征，输入MMoE与对应任务塔完成预测
### 关键结果
离线实验中，MMRM在4类任务的F1@5、NDCG@5均优于单任务微调、通用多任务MLLM基线；下游排序模型搭配全量4路MMRM表征，CTR GAUC达0.7037，较在线基线提升1.71pct，ACR、CVR GAUC分别提升0.89pct、0.92pct；线上A/B测试UCTR、UACR、UCVR分别提升0.42%、0.37%、0.35%，已全量部署京东搜索。
> 最值得记住的一句话：针对多任务排序场景，多模态表征的解耦程度与任务适配性，比单一表征的通用效果更能决定最终业务收益。
