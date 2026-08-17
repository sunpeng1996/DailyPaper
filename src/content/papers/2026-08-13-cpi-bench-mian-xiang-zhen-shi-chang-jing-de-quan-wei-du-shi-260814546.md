---
title: 'CPI-Bench: A Comprehensive,Practical and Intelligent Benchmark for Real-World
  Image Editing'
title_zh: CPI-Bench：面向真实场景的全维度实用智能化图像编辑评测基准
authors:
- Qinye Zhou
- Jun Zheng
- Yongchao Du
- Yuan Wang
- Zhengrui Chen
- Zuan Gao
- Taihang Hu
- Chao Lin
- Yefeng Shen
- Xingjian Wang
affiliations:
- Alibaba Group
arxiv_id: '2608.14546'
url: https://arxiv.org/abs/2608.14546
pdf_url: https://arxiv.org/pdf/2608.14546
published: '2026-08-13'
collected: '2026-08-17'
category: Eval
direction: 多模态图像编辑能力评测基准
tags:
- Benchmark
- Image Editing
- Multimodal Evaluation
- Human Preference Alignment
- Real-world Deployment
one_liner: 提出覆盖通用任务/真实高频场景/推理型编辑的多图像编辑评测基准，与人类评估偏好对齐度领先
practical_value: '- 电商商品图/广告图AI编辑工具选型时，可直接复用CPI-Practical-Bench的高频真实场景用例做模型筛选，大幅降低自建测试集的成本

  - 内部多模态AIGC工具评测体系可参考其三子集构建逻辑，从通用能力、业务高频场景、高阶推理需求三层搭建，覆盖全场景评测需求

  - 可借鉴其与人类偏好排行榜对齐的验证方法，优化自家AIGC生成效果的自动评测指标，减少人工标注工作量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像编辑评测基准仅覆盖单图简单任务，评测维度有限，无法有效区分不同模型在多图编辑、高难度推理指令编辑、真实生产部署场景下的性能差异，无法匹配产业落地的评测需求。
### 方法关键点
构建三级评测子集：1）CPI-General-Bench覆盖全类型编辑任务，首次纳入多图编辑评测维度；2）CPI-Practical-Bench聚焦真实用户高频使用场景；3）CPI-Intelligent-Bench专门评测高要求的推理型编辑能力。
### 关键结果
对主流图像编辑模型的评测显示，CPI-Bench的模型排名与Arena图像编辑排行榜对齐度最高，可有效区分不同模型在通用编辑能力、落地效果、高阶推理能力上的差距，是替代人工评测的可靠方案。
