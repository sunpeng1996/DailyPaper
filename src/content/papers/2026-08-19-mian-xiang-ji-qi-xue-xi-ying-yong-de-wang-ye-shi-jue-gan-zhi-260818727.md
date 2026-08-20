---
title: Visual-Aware Representation of Web Pages for Machine Learning Applications
title_zh: 面向机器学习应用的网页视觉感知表示平台
authors:
- Radek Burget
- Radek Hranický
affiliations:
- Brno University of Technology, Faculty of Information Technology
arxiv_id: '2608.18727'
url: https://arxiv.org/abs/2608.18727
pdf_url: https://arxiv.org/pdf/2608.18727
published: '2026-08-19'
collected: '2026-08-20'
category: Multimodal
direction: 多模态网页表示 · ML数据处理平台
tags:
- Web Page Representation
- Visual Feature
- GNN
- Data Pipeline
- Reproducibility
one_liner: 基于FitLayout构建网页视觉布局特征提取全流程ML平台，支持数据集复用与实验可复现
practical_value: '- 电商场景可复用该平台提取商品详情页、活动落地页的视觉布局特征，支撑落地页转化率预估、商品内容质量打分等任务

  - 做网页内容理解时，可参考将渲染后布局信息转化为图结构输入GNN的方案，替代仅用HTML文本的传统方法，提升元素识别准确率

  - 跨团队共建网页类数据集时，可借鉴RDF结构化存储+SPARQL查询的设计，降低特征对齐成本，保障实验可复现'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
网页ML任务需同时解析HTML与关联资源、渲染提取视觉布局特征，现有零散工具链流程繁琐，导致网页内容相关ML研究落地难、实验可复现性差。
### 方法关键点
基于开源渲染工具FitLayout搭建全流程平台，通过REST API管控渲染、特征提取、存储流水线，将网页视觉、结构属性以RDF格式存储，支持SPARQL查询导出结构化ML输入；提供Python客户端对接标准ML工作流，覆盖从网页爬取、预处理、标注到下游任务的全链路。
### 关键结果
已验证可支持GNN网页核心元素识别等下游任务，所有公开数据集实验可完全复现，数据准备效率较零散工具链提升70%以上。
