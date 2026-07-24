---
title: 'MemTools: A Unified Research Framework for Interoperable Agent Memory'
title_zh: MemTools：支持互操作的Agent记忆统一研究框架
authors:
- Chengfeng Zhao
- Jinhui Chen
- Sirui Liang
- Shizhu He
- Yequan Wang
- Jun Zhao
- Kang Liu
affiliations:
- 中国科学院自动化研究所
- 中国科学院大学
- 北京人工智能研究院
- 中关村人工智能研究院
arxiv_id: '2607.21404'
url: https://arxiv.org/abs/2607.21404
pdf_url: https://arxiv.org/pdf/2607.21404
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: Agent记忆系统 · 模块化互操作框架
tags:
- Agent_Memory
- Modular_Framework
- Interoperability
- Heterogeneous_Memory
- LLM_Agent
one_liner: 提出解耦Agent记忆全生命周期的统一框架，支持跨系统组件组合与异质记忆统一管理
practical_value: '- 可复用声明式数据契约设计，将电商导购/推荐Agent记忆的生成、存储、检索、演进各阶段解耦，替换组件迭代无需全链路重构，降低记忆系统升级成本

  - 参考异质记忆统一管理架构，可把用户行为符号记忆（点击/收藏记录）、Neural记忆（LoRA参数、KV cache）、多模态记忆（商品图/短视频）统一调度，提升推荐Agent上下文理解能力

  - 借鉴评测协议与数据集解耦设计，业务中验证记忆模块效果时，可快速切换离线/流式等不同评测流程，准确定位性能瓶颈，避免评测逻辑带来的结果偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent记忆系统架构碎片化严重，各生命周期阶段深度耦合、评测逻辑与特定数据集绑定、异质记忆（符号/神经/多模态）管理缺乏统一接口，导致无法独立验证记忆模块设计效果，跨系统组件复用成本极高，阻碍Agent记忆的系统性研究与落地。

### 方法关键点
- 标准化记忆生命周期：通过声明式数据契约定义记忆生成、检索、演进、利用各阶段的输入输出字段，自动校验组件兼容性，无需手动修改代码即可跨系统组装记忆流水线
- 统一评测范式：将benchmark数据集与评测执行逻辑正交解耦，同一数据集可适配离线/批量/流式等多种评测协议，消除评测逻辑引入的性能评估偏差
- 异质记忆统一管理：封装符号、神经（KV cache、LoRA参数等）、多模态三类记忆为独立流水线，通过统一调度层并行查询、链式调用，支持混合记忆架构快速搭建

### 关键实验结果
- 跨系统组件集成：在ALFWorld数据集上，混合AWM记忆生成模块与A-Mem存储检索模块，成功率比原生AWM高2.98个百分点（43.28% vs 40.30%）
- 评测协议解耦验证：同一AWM流水线在批量协议下成功率40.30%，流式协议下仅33.58%，记忆更新时序对效果的影响可被独立度量
- 异质记忆协同：Mem-Gallery数据集上符号+多模态记忆协同F1达35.3，比单模高4.1~5.2个百分点；ALFWorld上符号+神经记忆协同成功率达51.5%，比单模高3~19.4个百分点
- 开发效率验证：搭建复合记忆流水线的代码量降低60.1%，自定义函数/类数量降低85.4%

### 核心结论
Agent记忆系统的性能差异很多时候并非来自模块本身的算法优劣，而是来自组件适配逻辑、评测时序、记忆类型搭配等易被忽略的变量，模块化解耦是精准迭代的核心前提
