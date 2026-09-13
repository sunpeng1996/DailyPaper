---
title: 'DianShi-RxnDB: A Large-Scale, Fine-Grained Organic Reaction Data Platform
  Built via a Fully Automated Pipeline for Researchers and AI Agents'
title_zh: DianShi-RxnDB：面向研究者与AI Agent的大规模细粒度有机反应数据平台
authors:
- Yubin Wang
- Xingjian Wei
- Jiang Wu
- Yinfan Wang
- Boyu Zhu
- Lin Zhang
- Jianing Yu
- Huazheng Zeng
- Ruiyi Ding
- Junyuan Gao
affiliations:
- 上海人工智能实验室
- 复旦大学
- 上海交通大学
- 华东师范大学
- 华东理工大学
arxiv_id: '2609.06703'
url: https://arxiv.org/abs/2609.06703
pdf_url: https://arxiv.org/pdf/2609.06703
published: '2026-09-05'
collected: '2026-09-13'
category: Other
direction: 垂直领域AI Agent 结构化数据平台构建
tags:
- AI Agent
- Structured Data Platform
- Automated Data Extraction
- Vertical Domain Dataset
- Information Retrieval
one_liner: 构建了含1480万条高准确率结构化有机反应数据的平台，支持人工检索与AI Agent标准化调用
practical_value: '- 垂直领域结构化数据集构建可复用「多模态内容自动抽取→字段归一化→自动质量校验」的流水线方案，大幅降低人工标注成本

  - 面向AI Agent提供垂直领域检索能力时，可参考封装为MCP协议可组合工具的设计，降低Agent对接与工具调用的开发成本

  - 多源异构数据去重、细粒度字段对齐的方法论可直接迁移到电商商品/广告多源特征库的构建流程'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
高质量结构化有机反应数据是AI4Chem落地的核心基础，但现有相关知识分散在专利文本、图片、反应式等多源异构载体中，难以直接用于计算检索与AI模型训练。
### 方法关键点
1. 搭建全自动化多模态信息抽取+归一化+质量校验流水线，覆盖USPTO、EPO 1976-2025年公开的有机合成专利
2. 每条数据为单步实验记录，包含反应物、试剂、温度、反应时间、产率、来源专利链接等10+细粒度字段
3. 同时提供网页版人工检索工作台，以及适配AI Agent的MCP协议可组合结构化检索工具
### 关键结果数字
- 累计生成2400万条反应实例，其中1480万条（占比61.7%）通过自动化质量校验
- 1300条抽样人工评估字段级微平均准确率达92.95%
- 相比同类产品Pistachio，在去重记录量、表示粒度、字段准确率上均有明显优势
