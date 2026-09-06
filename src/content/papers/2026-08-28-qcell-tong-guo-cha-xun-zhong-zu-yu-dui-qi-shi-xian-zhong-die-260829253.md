---
title: 'QCell: Recombining and Aligning Cell Queries for Overlapping Instance Segmentation'
title_zh: QCell：通过查询重组与对齐实现重叠细胞实例分割
authors:
- Yaroslav Prytula
- Anton Popov
- Dmytro Fishman
affiliations:
- University of Tartu
- Ukrainian Catholic University
- Igor Sikorsky Kyiv Polytechnic Institute
- STACC OÜ
- Better Medicine OÜ
arxiv_id: '2608.29253'
url: https://arxiv.org/abs/2608.29253
pdf_url: https://arxiv.org/pdf/2608.29253
published: '2026-08-28'
collected: '2026-09-06'
category: Other
direction: 显微镜图像 · 重叠细胞实例分割
tags:
- Instance Segmentation
- Query-based Model
- Contrastive Learning
- Medical Image Analysis
- Computer Vision
one_liner: 提出基于查询的QCell模型，解决显微镜图像重叠细胞分割问题，性能超现有SOTA
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
显微镜下重叠细胞的半透明结构会产生弱边界、重叠区域视觉特征混杂问题，现有方法依赖局部感兴趣区域或形状先验，缺乏跨重叠对象的全局推理能力，分割精度受限。
### 方法关键点
1. 新增实例重组模块：在隐空间分解并重组查询表征，支撑重叠场景下的完整对象结构推理
2. 设计对比查询对齐目标：同时实现独特实例特征学习、重叠细胞查询的差异化区分
3. 开源全新Organoid数据集，作为重叠细胞分割的基准测试集
### 关键结果
在多个公开基准上性能超越SOTA，ISBI2014数据集上AP提升2.2、AJI提升2.7
