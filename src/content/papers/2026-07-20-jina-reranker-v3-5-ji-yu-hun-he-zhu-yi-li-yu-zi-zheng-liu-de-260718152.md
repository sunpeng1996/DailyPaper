---
title: 'jina-reranker-v3.5: An Efficient Listwise Reranker with Hybrid Attention and
  Self-Distillation'
title_zh: jina-reranker-v3.5：基于混合注意力与自蒸馏的高效列表式重排器
authors:
- Christina Nasika
- Feng Wang
- Antonis Krasakis
- Han Xiao
affiliations:
- Jina AI by Elastic
arxiv_id: '2607.18152'
url: https://arxiv.org/abs/2607.18152
pdf_url: https://arxiv.org/pdf/2607.18152
published: '2026-07-20'
collected: '2026-07-21'
category: RecSys
direction: 检索重排 · 列表式重排器效率与效果优化
tags:
- Reranker
- Listwise Ranking
- Hybrid Attention
- Knowledge Distillation
- Semi-structured Retrieval
one_liner: 0.6B参数列表式重排器，采用混合注意力与同规模自蒸馏，效果追平4B模型且推理提速最多1.56倍
practical_value: '- 架构优化：列表式重排场景可复用3L2G混合注意力方案，固定最后一层为全局注意力保障跨文档对比能力，其余层穿插滑动窗口注意力，长文本场景最多降1.56倍推理延迟，适配电商长商品描述、多属性商品重排需求

  - 训练技巧：全注意力模型迁移到稀疏注意力架构时，可复用三阶段自蒸馏方案：先训同规模全注意力教师，再分步做稀疏注意力适配，最后做多维度对齐蒸馏，无需大模型教师即可保留99%以上效果

  - 数据构造：电商半结构化检索场景，可参考其约束式合成数据方法：从商品属性采样约束生成query，修改1-2个属性构造硬负样本再经LLM校验，可大幅提升半结构化数据重排效果

  - 部署选型：Agent检索、电商搜索重排等成本敏感场景，可优先选择小参数域内专精的重排模型，无需盲目用大模型，0.6B规模即可达到4B通用模型的重排效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有列表式重排器是Agent检索、搜索推荐流程的核心组件，但生产部署需要同时满足低延迟、跨域鲁棒性、半结构化数据理解能力三个要求，此前的jina-reranker-v3采用全全局注意力，推理成本高，且在专业域、半结构化数据上效果不足，难以适配电商、法律、医疗等真实业务场景。

### 方法关键点
- 混合注意力架构：保留LBNL交互的最后一层全局注意力约束，其余层采用「3层滑动窗口+2层全局」的3L2G混合注意力调度，滑动窗口大小1024token，平衡长距离依赖与推理效率
- 多域训练数据集：针对性补充法律、医疗、金融、多语言、半结构化数据，重点优化半结构化场景，通过「约束采样→属性扰动造硬负→LLM校验」的流程合成高质量训练样本
- 三阶段自蒸馏：先训同参数规模的全注意力教师模型，再分步做稀疏注意力适配（先仅训注意力层，再全参数微调），最后通过排名、分数、隐状态、嵌入四层对齐的蒸馏损失把教师能力迁移到混合注意力学生模型

### 关键结果
0.6B参数的v3.5在BEIR上nDCG@10达63.20，追平4B参数的Qwen3-Reranker-4B，参数仅为其1/7；半结构化检索场景nDCG@10比v3高9.6个点；推理在短文本场景提速1.22倍，长文本场景提速1.56倍；多语言、专业域效果均明显优于v3及同规模基线。

**最值得记住的一句话**：小参数域内专精的重排模型，效果可以媲美远大于它的通用模型，且推理成本低得多，是生产部署的更优选择。
