---
title: 'TESSERA v2: Scaling Pixel-wise Earth Foundation Models'
title_zh: TESSERA v2：像素级地球基础模型的规模化训练方案
authors:
- Zhengpeng Feng
- Sadiq Jaffer
- Ira Shokar
- Jovana Knezevic
- Mark Elvers
- Clement Atzberger
- Robin Young
- Aneesh Naik
- Niall Robinson
- Andrew Blake
affiliations:
- University of Cambridge
- NVIDIA
- dClimate Labs
arxiv_id: '2607.03949'
url: https://arxiv.org/abs/2607.03949
pdf_url: https://arxiv.org/pdf/2607.03949
published: '2026-07-03'
collected: '2026-07-12'
category: Training
direction: 基础模型规模化训练·蒸馏与低维表征落地
tags:
- Scaling Law
- Model Distillation
- Matryoshka Representation
- Foundation Model
- Embedding Optimization
one_liner: 通过395组可控实验给出像素级基础模型规模化训练、算力分配与蒸馏部署的经验法则
practical_value: '- 大模型预训练阶段不要仅依赖预训练loss筛选最优checkpoint，需补充小样本下游任务验证，避免算力浪费

  - 算力分配可参考「编码器参数量、训练数据量同步扩容，投影头参数固定」的法则，平衡训练投入与下游效果

  - 落地阶段可对大模型做蒸馏生成Matryoshka表征，低维前缀即可保留大部分效果，大幅降低embedding存储与推理成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
像素级地球观测（EO）基础模型已达到SOTA效果，但规模化训练的算力分配策略、预训练效果与下游表现的关联规律尚未明确，预训练预算投入效率低。
### 方法关键点
开展业内最大规模EO模型可控缩放研究，基于1024块GH200超算芯片完成395组Barlow Twins架构训练，覆盖15个下游任务做全量验证；提出算力分配经验法则：随预训练预算提升同步扩容编码器参数量与训练数据量，投影头参数保持固定；训练0.5B/1B/2B系列基座模型后蒸馏为小参数学生模型，输出Matryoshka表征降低部署成本。
### 关键结果数字
预训练损失与下游效果皮尔逊相关系数绝对值<0.2，仅按损失选模型会浪费大量算力；21M参数的蒸馏模型效果超过所有测试的开源/专有大模型（部分参数量高出数个量级）；16维表征前缀即可保留128维全表征92%的效果，存储仅为原有的1/8。
