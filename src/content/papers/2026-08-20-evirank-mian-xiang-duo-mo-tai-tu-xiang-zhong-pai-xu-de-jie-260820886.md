---
title: 'EviRank: Structured Relevance Evidence for Multimodal Image Re-ranking'
title_zh: EviRank：面向多模态图像重排序的结构化相关性证据框架
authors:
- Enjun Du
- Siyi Liu
- Zirong Chen
- Xinyu Zuo
- Jinwen Luo
- Ruiwen Tao
- Lisheng Duan
- Haijin Liang
- Jin Ma
- Junfu Pu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- Tencent Yuanbao
- The University of Hong Kong
arxiv_id: '2608.20886'
url: https://arxiv.org/abs/2608.20886
pdf_url: https://arxiv.org/pdf/2608.20886
published: '2026-08-20'
collected: '2026-08-24'
category: RecSys
direction: 多模态搜索 · 图像检索重排序优化
tags:
- Multimodal Retrieval
- Re-ranking
- Evidence-based Reasoning
- Distillation
- Training-free
one_liner: 将多模态图像重排序转化为语义约束满足问题，免训练实现SOTA，可蒸馏轻量低耗学生模型
practical_value: '- 电商多模态搜图场景可直接复用6类语义槽+约束标签（required/forbidden/ignorable）的规则框架，解决用户「找同款改属性」的复杂查询匹配问题，免训练快速上线

  - 重排阶段可借鉴「确定性rubric打分 + 基于证据的列表比较」的免训练流程，快速迭代baseline，降低冷启动成本

  - 线上性能受限时，可参考用结构化证据作为监督蒸馏轻量小模型的方案，保证90%以上效果的同时降低推理延迟

  - 复杂多模态查询解析可参考将多源输入统一转化为结构化证据包的思路，降低大模型CoT幻觉问题'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态图像重排器要么把多维度相关性压缩为黑盒嵌入，要么依赖自由形式CoT容易遗漏/幻觉细粒度约束，无法适配「保留实体改属性」这类组合式查询需求。
### 方法关键点
借鉴NLP基于评分规则和检查表的评估思路，将重排转化为语义约束满足问题：1）将任意纯文本、纯图像、组合式查询解析为统一证据包，覆盖实体、属性等6类语义槽，每个槽标注为required/forbidden/ignorable三类约束；2）重排流程改为证据条件验证，结合确定性规则打分和基于证据的列表比较，全程免训练；3）可选将结构化证据作为监督蒸馏轻量学生模型，适配线上低延迟需求。
### 关键结果
在文本到图像、图像到图像、组合式图像检索三类任务共5个基准数据集上实现SOTA，蒸馏的学生模型保留90%以上教师效果，推理成本大幅降低。
