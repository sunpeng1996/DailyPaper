---
title: Score-Only Distillation for Compact Dense Retrieval
title_zh: 仅用打分蒸馏实现轻量化密集检索模型
authors:
- Kirill Dubovikov
- Martin Takac
- Salem Lahlou
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2607.11465'
url: https://arxiv.org/abs/2607.11465
pdf_url: https://arxiv.org/pdf/2607.11465
published: '2026-07-13'
collected: '2026-07-14'
category: RecSys
direction: 检索模型压缩 · 黑盒知识蒸馏
tags:
- Knowledge Distillation
- Dense Retrieval
- Model Compression
- PairMSE
- Embedding Model
one_liner: 仅用黑盒大检索模型的打分蒸馏轻量化检索器，降低推理成本同时保留大部分排序性能
practical_value: '- 工程上若已使用大参数量Embedding模型做召回/检索，可通过该方案蒸馏为小模型，query编码速度提升4-5倍、doc编码速度提升近10倍，大幅降低推理与索引更新成本

  - 训练时可直接复用行中心化PairMSE实现，无需显式构造所有两两pair，内存占用从O(k²)降至O(k)，训练效率更高，效果优于仅正负对对齐的MarginMSE

  - 蒸馏仅依赖黑盒教师的打分结果，无需对齐教师的Embedding空间、Tokenizer或架构，可直接融合多个异构大检索模型的打分作为监督信号

  - 上线前必须做域内验证：蒸馏候选行需与部署场景的语料、query类型对齐，跨域部署会出现明显效果退化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大参数量Embedding模型大幅提升密集检索排序效果，但在线推理成本高、索引更新慢、运维复杂度高；现有蒸馏方案大多需要对齐教师模型的隐状态或Embedding，限制了异构大模型作为教师的可能性，亟需探索仅依赖黑盒教师打分即可完成蒸馏的轻量化方案。

### 方法关键点
- 数据：每个query对应1个正样本和k个负样本组成候选行，仅需黑盒教师输出的每行query-doc对打分作为监督信号，无需教师任何内部状态
- 损失：提出行中心化PairMSE损失，对教师与学生的打分残差做行中心化后计算MSE，等价于全两两PairMSE但内存占用从O(k²)降至O(k)，规避了显式构造pair的开销
- 扩展：支持多教师打分融合、硬负样本挖掘、主动样本选择等扩展，无需修改核心训练流程

### 关键实验
在BEIR 8个公开检索数据集上测试，以Qwen3-Embedding-0.6B、E5-large-v2为学生，Qwen3 8B、NV-Embed v2为教师。核心结果：蒸馏后学生可恢复25%~50%的小模型基线到教师的性能差距；0.6B Qwen学生query编码速度比8B教师+NV-Embed融合方案快4.7倍，doc编码快9.7倍；行中心化PairMSE比MarginMSE的8任务macro NDCG@10高0.025，比仅用标签的对比学习高0.177。

仅用打分的蒸馏是检索模型降本的有效工具，但仅适用于与蒸馏数据分布匹配的部署场景，无法自动实现跨域迁移。
