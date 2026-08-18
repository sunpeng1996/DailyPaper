---
title: 'AnchorScore: A CLIP-Based Diagnostic of MLLM Annotation Difficulty'
title_zh: AnchorScore：基于CLIP的多模态大模型标注难度诊断工具
authors:
- Yan Ma
- Lizhuo Zhang
affiliations:
- School of Foreign Studies
arxiv_id: '2608.16690'
url: https://arxiv.org/abs/2608.16690
pdf_url: https://arxiv.org/pdf/2608.16690
published: '2026-08-17'
collected: '2026-08-18'
category: Eval
direction: 多模态大模型评估 · 低成本难度预判
tags:
- CLIP
- MLLM
- Annotation
- Difficulty Estimation
- Cost Optimization
one_liner: 提出基于CLIP零样本准确率的AnchorScore，低成本预判MLLM各类别标注难度
practical_value: '- 多模态内容/商品标注场景可复用AnchorScore逻辑，用低成本CLIP预筛高难度标注类目，减少大模型调用量降低成本

  - 电商内容审核、商品属性标注的混合路由架构可直接参考：CLIP处理简单类目，MLLM仅处理高难度类目，实测可省44% MLLM成本同时精度提升23pp

  - 标注人工复核优先级可直接用AnchorScore排序，优先审核高难度类目，提升复核效率'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
MLLM广泛用于自动标注但不同类别准确率波动极大（跨类别12%~98%），直接调用MLLM全量评估标注难度成本极高（27B模型评估5k张图需14小时），低成本先验难度排序信号缺失。
### 方法关键点
基于CLIP零样本类级别准确率构造AnchorScore，作为先验诊断指标预判MLLM标注不可靠的类别，仅需3分钟即可完成5k张图的难度排序，无需提前调用MLLM。
### 关键结果
1. 课堂行为数据集上与MLLM类别准确率斯皮尔曼相关系数ρ=0.769，Stanford40动作数据集上ρ=0.817，显著优于DINOv2、ResNet-50等对比方案；
2. 基于AnchorScore的CLIP/MLLM混合路由比单用CLIP精度提升23pp，同时节省44% MLLM调用成本；
3. 效果在行为识别类数据最优，医疗、卫星影像上效果衰减。
