---
title: 'Identify, Locate, Link: End-to-End Key-Value Extraction from Document Images'
title_zh: 识别、定位、关联：文档图像端到端键值信息提取方法
authors:
- A. Said Gurbuz
- Ahmed Nassar
- Christoph Auer
- Maksym Lysak
- Lucas Morin
- Matteo Omenetti
- Tim Strohmeyer
- Panagiotis Vagenas
- Nikolaos Livathinos
- Michele Dolfi
affiliations:
- IBM Research Zurich
- ETH Zurich
arxiv_id: '2608.20868'
url: https://arxiv.org/abs/2608.20868
pdf_url: https://arxiv.org/pdf/2608.20868
published: '2026-08-21'
collected: '2026-08-24'
category: Multimodal
direction: 多模态文档理解 · 端到端键值提取
tags:
- VLM
- Document Understanding
- Key-Value Extraction
- Data Augmentation
- Layout-Aware Evaluation
one_liner: 基于256M参数轻量VLM实现无OCR预处理的端到端文档键值提取，性能超大模型且推理快5倍以上
practical_value: '- 电商场景的纸质发票、快递面单、商家资质文件结构化提取可复用该端到端无OCR方案，避免多阶段误差累积，降低推理时延

  - 小参数VLM微调的轻量化思路可迁移到端侧/离线文档处理任务，相比大参数量VLM可大幅降低部署成本

  - 保留语义子图的graph-based数据增强方法可复用在多模态实体关联任务的训练数据扩充场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统文档处理采用OCR级联下游结构化提取模型的链路，存在多阶段误差累积问题，而企业80%以上信息存储在非结构化文档中，结构化提取效率低、成本高。
### 方法关键点
1. 微调256M参数的轻量VLM SmolDocling，无需OCR预处理，单阶段完成键值的语义识别、空间定位、关系关联三个子任务；
2. 扩展DocTags新增key、value、区域、链接专用标签，支持在统一输出序列中表达多对多键值关系；
3. 设计结合合成表单填充+保留完整键值子图的图裁剪的数据增强pipeline，解决训练数据不足问题；
4. 提出融合文本匹配+空间边界框校验的布局感知评估框架，更贴合实际业务需求。
### 关键结果
在FUNSD、XFUND及大规模私有数据集上，布局感知评估指标优于大参数量零样本VLM基线，参数量仅为Qwen2.5-VL（7B）的1/27，推理速度提升5倍以上
