---
title: Continual Learning in Transition
title_zh: 持续学习的范式转型
authors:
- Zhiyan Hou
- Dan Zhang
- Tao Feng
- Liyuan Wang
- Wei Li
- Xiangzhao Hao
- Hongyan An
- Junfeng Fang
- Haokai Ma
- Zhaohui Xu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- National University of Singapore
- Tsinghua University
- Shanghai Jiao Tong University
- Alibaba Group
arxiv_id: '2608.06216'
url: https://arxiv.org/abs/2608.06216
pdf_url: https://arxiv.org/pdf/2608.06216
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 持续学习 · 系统级适配范式演进
tags:
- Continual Learning
- Test-time Training
- On-policy Learning
- System-level Adaptation
- Incremental Learning
one_liner: 搭建When/How/Where三轴分析框架，系统性梳理持续学习从参数中心到系统级适配的演进
practical_value: '- 电商推荐/广告系统迭代可参考三轴框架选适配方案：冷启动用off-policy预训练，线上流量阶段引入on-policy实时更新，推理侧结合test-time训练适配实时用户反馈

  - Agent系统持续进化可跳出参数更新思路：通过外部记忆库、技能库等组件扩展能力边界，避免频繁微调带来的灾难性遗忘与资源消耗

  - 大模型推荐系统做增量更新时可按Where维度拆分：通用能力更新走内部参数微调，场景/品类专属规则更新走外部约束配置，平衡迭代效率与效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统持续学习完全围绕参数调整（训练策略、结构设计、权重适配）实现知识更新与留存，无法适配LLM、Agent等新兴场景对开放环境下持续进化的需求，原有范式已不适用。

### 方法关键点
从When/How/Where三个维度搭建分析框架：
- How维度：涵盖off-policy、on-policy、非梯度优化三类更新机制
- When维度：覆盖预训练、训练后、推理全生命周期的学习节点
- Where维度：区分内部参数更新、外部结构（记忆/技能库/交互协议）约束两类更新载体
基于该框架系统性梳理持续学习领域代表性工作，完整刻画从参数中心到系统级适配的转型路径。

### 关键结果
明确当前持续学习转型的三大核心挑战：系统模块化协同效率、跨阶段知识一致性、开放环境下的能力边界评估，指明了未来研究方向。
