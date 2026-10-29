---
title: 'MMFact: Simplifying Multimodal Misinformation Detection with Shared Resources
  and Tools'
title_zh: MMFact：面向多模态虚假信息检测的共享资源与工具集
authors:
- Yuchen Miao
- Zijun Wang
- Mingtai Zhang
- Xiaoyi Chen
- Sihan Deng
- Xianglin Ding
affiliations:
- Northeastern University
- Guangxi University
- Zhengzhou University
arxiv_id: '2610.34162'
url: https://arxiv.org/abs/2610.34162
pdf_url: https://arxiv.org/pdf/2610.34162
published: '2026-10-25'
collected: '2026-10-29'
category: Multimodal
direction: 多模态虚假信息检测 · 共享工具集
tags:
- Multimodal
- Misinformation Detection
- Benchmark
- Dataset
- Toolkit
one_liner: 推出含47种检测实现、3个数据集及预处理物料的多模态虚假信息检测工具集，消除预处理差异支持公平比较
practical_value: '- 电商内容风控场景（如商品图文虚假宣传、带货内容虚假信息检测）可直接复用MMFact的OCR、图文特征提取等预处理模块，减少重复开发成本

  - 做跨算法效果对比时，统一使用相同预处理输入，可排除物料差异对模型效果评估的干扰，得到更可信的benchmark结果

  - 可借鉴其模块化框架设计思路，搭建业务侧多模态内容审核的可插拔算法框架，支持快速迭代不同检测模型'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态虚假信息检测现有方案预处理pipeline与辅助资源不统一，实验对比结果受输入差异干扰可信度低，且预处理环节重复开发成本高，研究者无法聚焦检测算法本身的优化。
### 方法关键点
1. 开源MMFact共享资源工具集，整合47种检测算法实现与基线、3个多模态公开数据集；
2. 预置全链路预处理物料，覆盖语义特征、OCR结果、图像描述、外部证据等，兼容算法可直接复用，无需重复开发；
3. 提供模块化训练评估框架，保留算法自定义设计空间的同时统一实验流程。
### 关键结果
统一预处理输入后完全消除物料差异带来的实验评估偏差，支持47种检测算法的公平横向对比，大幅降低多模态虚假信息检测研究与落地的前置开发成本。
