---
title: 'SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via
  Representation Verbalization'
title_zh: SAEVerbalizer：通过表示言语化生成稀疏自编码器特征的解释
authors:
- Weihan Meng
- Hongzhu Guo
- Yi Jing
- Dewen Liu
- Zijun Yao
- Xiaozhi Wang
- Lei Hou
- Juanzi Li
affiliations:
- Tsinghua University
- Peking University
- Fudan University
arxiv_id: '2608.13538'
url: https://arxiv.org/abs/2608.13538
pdf_url: https://arxiv.org/pdf/2608.13538
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: LLM可解释 · SAE特征言语化
tags:
- SAE
- LLM Interpretability
- Feature Explanation
- Representation Verbalization
- PEFT
one_liner: 提出SAEVerbalizer框架，直接从SAE解码器方向生成特征自然语言解释，解决现有方法浅层低效的问题
practical_value: '- 做LLM4Rec可解释时，可复用该框架将SAE提取的用户/物品语义特征直接转换为自然语言解释，替代原有依赖行为归因的低效方案

  - 跨LLM部署SAE相关能力时，可借鉴其轻量adapter适配方案，无需全量重训即可复用已有的言语化能力，降低部署成本

  - 做Agent决策链路可解释时，可基于该思路将LLM内部激活特征转换为可验证的自然语言描述，提升Agent决策可追溯性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有SAE特征解释高度依赖外部观测LLM行为，不仅易得到浅层解释，大规模收集行为证据还存在计算效率低的问题，难以支撑SAE可解释能力落地。

### 方法关键点
1. 提出SAEVerbalizer框架，将SAE解码器方向直接注入LLM内部表示，微调LLM下游层即可生成对应特征的自然语言解释，无需依赖外部行为数据
2. 支持搭配轻量adapter适配不同LLM的SAE特征，大幅降低跨模型迁移成本

### 关键结果
- 学习到的言语化能力可泛化至未见过的SAE特征，可跨独立训练的SAE字典迁移
- 仅添加轻量adapter即可扩展至不同LLM的SAE特征解释任务
- 干预实验验证：注入多方向可生成对应组合含义的解释，反方向注入可得到对应的语义偏移解释
