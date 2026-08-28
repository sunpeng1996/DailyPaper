---
title: Rubrics as Visual-Repair Context for Self-Evolving UI-to-Code Generation
title_zh: 基于评分规则作为视觉修复上下文的自进化UI转代码生成框架
authors:
- Tianyi Xiong
- Zhengyuan Yang
- Xiaofei Wang
- Chung-Ching Lin
- Ruichun Ma
- Kevin Lin
- Zhendong Wang
- Linjie Li
- Chenxi Liu
- Ruibo Chen
affiliations:
- University of Maryland, College Park
- Microsoft
arxiv_id: '2608.24138'
url: https://arxiv.org/abs/2608.24138
pdf_url: https://arxiv.org/pdf/2608.24138
published: '2026-08-24'
collected: '2026-08-28'
category: Multimodal
direction: 多模态大模型 · 自进化优化
tags:
- VLM
- UI-to-Code
- Self-Evolution
- Visual Repair
- Rubric-Guided
one_liner: 提出RubSE评分引导自进化框架，解决UI转代码生成中局部修改引发的视觉修复耦合问题
practical_value: '- 自进化迭代优化场景可借鉴结构化rubric引导思路，限制单轮修改范围，避免修改扩散导致原有正确部分劣化，可复用在AIGC生成商品详情页、广告素材的迭代优化场景

  - 多角色分工优化架构可复用：用能力更强的模型生成修复引导规则，喂给推理成本更低的弱执行模型做改动，兼顾效果和部署成本

  - 迭代历史存储复用思路，可用于推荐系统排序结果迭代调优、Agent工具调用结果的迭代修正场景，避免重复修改或无效修改'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
VLM在UI-to-code生成任务中测试时自进化不稳定，核心障碍为**视觉修复耦合**：局部代码修改会通过布局、样式、组件依赖传播，修复一处视觉不一致的同时劣化原本匹配的区域。
## 方法关键点
提出RubSE评分引导自进化框架：1. 将视觉反馈抽象为结构化rubric作为修复上下文；2. 每轮迭代生成多类型候选rubric，仅选择优先级最高的单个修复目标；3. 存储历史选中的rubric作为迭代引导，限制单轮修改范围，避免重复或过度修改。
## 关键结果
在6个VLM、3个UI-to-code基准测试集上验证：相较朴素自进化方案，RubSE最终轮、最优轮效果均大幅提升，优化轨迹稳定性更高，轨迹级性能上限更优；严重视觉退化的恢复能力显著提升，可有效降低轨迹崩溃概率，强rubric生成器可向弱代码优化模型迁移有效修复引导。
