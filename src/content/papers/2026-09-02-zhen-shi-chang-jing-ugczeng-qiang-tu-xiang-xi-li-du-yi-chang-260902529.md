---
title: 'Fine-Grained Anomaly Perception in Wild UGC-Enhanced Images: A Comprehensive
  Dataset and Difference-Fusion Framework'
title_zh: 真实场景UGC增强图像细粒度异常感知：基准数据集与差异融合框架
authors:
- Yan Zhong
- Gefei Chen
- Qiufang Ma
- Zhen Wang
- Zhiwei Fan
- Lei Shi
- Tingting Jiang
affiliations:
- Peking University
- ByteDance Inc. (Douyin)
- Communication University of China
arxiv_id: '2609.02529'
url: https://arxiv.org/abs/2609.02529
pdf_url: https://arxiv.org/pdf/2609.02529
published: '2026-09-02'
collected: '2026-09-04'
category: Multimodal
direction: 多模态UGC内容质量异常检测
tags:
- UGC
- Image Anomaly Detection
- Benchmark Dataset
- Computer Vision
- Content Quality Assessment
one_liner: 定义UGC增强图像异常感知新任务，开源4k标注数据集，提出端到端差异融合检测框架
practical_value: '- 电商UGC商品图/短视频自动修图场景可复用DFAP-UGC框架，检测美颜/增强带来的人脸、文字、纹理异常，降低客诉率

  - 内容平台UGC质量审核链路可参考LADTP动态任务优先级训练策略，实现多任务端到端训练，减少多阶段推理开销

  - 构建自有业务场景图像异常检测数据集时，可复用UEAP-4k的细粒度标注规则（类别、空间位置、严重程度）'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
短视频/社交平台普遍对UGC图像做增强优化，但算法会引入人脸变形、文字扭曲、纹理失真等局部异常，现有IQA方法仅做整体质量打分，无法捕获真实场景中增强算法带来的细粒度局部异常。

### 方法关键点
1. 正式定义UEAP（UGC增强图像异常感知）新任务，开源首个业务场景构建的UEAP-4k基准数据集，标注包含异常类别、空间位置、严重程度三个维度的细粒度信息
2. 提出DFAP-UGC差异融合检测框架，通过原图像与增强图像的显式差异融合，结合密集空间查询、区域验证、质量感知排序，实现复杂场景下鲁棒异常识别
3. 提出LADTP局部感知动态任务优先级训练策略，解决子任务耦合问题，实现端到端训练，消除多阶段推理开销

### 关键结果
在UEAP-4k数据集上，DFAP-UGC性能大幅优于所有基于经典IQA方法适配的基线模型，核心任务指标领先10%以上。
