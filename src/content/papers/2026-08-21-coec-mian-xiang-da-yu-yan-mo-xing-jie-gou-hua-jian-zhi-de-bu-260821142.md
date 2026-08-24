---
title: 'COEC: Calibrated Orthogonal-Equivalence Compensation for Structured Pruning
  of Large Language Models'
title_zh: COEC：面向大语言模型结构化剪枝的校准正交等价补偿方法
authors:
- Peiqi Yu
- Nam Ling
- Wei Wang
- Wei Jiang
affiliations:
- Santa Clara University
- Futurewei Technologies, Inc.
arxiv_id: '2608.21142'
url: https://arxiv.org/abs/2608.21142
pdf_url: https://arxiv.org/pdf/2608.21142
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: LLM压缩 · 结构化剪枝无训练补偿
tags:
- LLM Pruning
- Structured Pruning
- Training-free Compression
- Orthogonal Rotation
- Post-pruning Compensation
one_liner: 无训练的LLM结构化剪枝后补偿框架，通过双正交旋转恢复剪枝损失的模型性能
practical_value: '- 业务侧部署自定义LLM（如Agent域内微调模型、推荐文案生成LLM）时，可直接用COEC对结构化剪枝后的模型做补偿，无需重训即可在30%稀疏度下恢复大部分精度，同时降低23-29%的推理内存与算力开销

  - 可复用COEC的GCV自适应正则化思路，在小校准集场景下避免过拟合，比如RAG的query重写模型微调、少样本用户偏好对齐任务

  - 注意力层间对齐惩罚的设计可迁移到多模态LLM、多Agent协作的状态对齐任务中，保证相邻模块的几何关系一致性，降低模块间适配成本

  - COEC的plug-in设计可直接接入现有Wanda-sp、FLAP等主流剪枝流程，无需改动原有剪枝逻辑，工程落地成本极低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM推理成本高是落地核心瓶颈，结构化剪枝删去权重列可直接生成更小的稠密模型，无需特殊稀疏内核支持，但剪枝后精度损失明显；现有无训练补偿方法仅加偏置或单侧正交旋转，无法修正输入方向的误差，高稀疏度下性能下降严重，且小校准集下容易过拟合。

### 方法关键点
- 采用双正交旋转框架：对剪枝保留的权重同时做左（输出侧）、右（输入侧）正交旋转，左旋转有闭式解，右旋转在简化Stiefel流形上迭代优化，无需反向传播和重训
- 引入GCV（广义交叉验证）的逐奇异值缩放：每层自动选择正则化强度，避免小校准集过拟合，同时保留预训练权重的谱结构
- 加入Gram矩阵谱调和、注意力层间对齐惩罚：平衡困惑度和零样本精度，保留相邻注意力投影层的几何关系，避免剪枝破坏层间匹配
- 完全插件化：兼容任意列剪枝的选择策略，不改变模型架构，仅需128条校准序列的二阶统计量即可完成补偿

### 关键实验
在Llama-3、Llama-3.1、Qwen2.5等多个7B-72B模型上测试，对比Wanda-sp、FLAP、RCPU三个SOTA基线：30%稀疏度下，COEC在所有模型上均降低困惑度，最高比基线低4.26（Qwen2.5-32B从13.90降到9.64），5/6的模型零样本精度提升，最高+6.6个点；稀疏度越高收益越大，30%稀疏度下相对RCPU的困惑度提升幅度是10%稀疏度的4倍以上；工程成本低，补偿7B-8B模型仅需45-86分钟单GPU算力，补偿后模型无额外推理开销。

结构化剪枝后的性能损失可通过无训练的双正交旋转补偿恢复大部分，无需重训即可实现低推理成本和高精度的平衡。
