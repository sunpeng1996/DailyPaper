---
title: 'The Illusion of Grounding: Do Vision-Language Models Weigh Retrieved Text
  and Images Like an Ideal Observer?'
title_zh: “接地幻觉”研究：检索增强视觉语言模型的文本图像权重分配偏差
authors:
- Basavaraj R M
- Harshal Chandel
affiliations:
- eClerx
arxiv_id: '2611.23127'
url: https://arxiv.org/abs/2611.23127
pdf_url: https://arxiv.org/pdf/2611.23127
published: '2026-11-17'
collected: '2026-11-18'
category: Eval
direction: 多模态RAG效果评估与鲁棒性测试
tags:
- VLM
- Multimodal RAG
- Evaluation Dataset
- Bayesian Cue Combination
- Robustness Test
one_liner: 构建20万规模多模态压力测试数据集GIB-200K，量化检索增强VLM的模态权重偏差与接地幻觉程度
practical_value: '- 做电商图文导购Agent、多模态商品检索等业务时，可复用本文的知识惯性/感官捕获量化方法，判断模型是否过度依赖检索文本/图像，针对性优化模态融合权重

  - 多模态RAG系统上线前的压力测试可复用本文范式：引入检索硬负样本、图像降质、跨模态冲突三类场景，验证系统在真实噪声环境下的鲁棒性

  - 上线阶段可加入无检索一致性校验的零训练成本策略，过滤误导性检索文本导致的错误回答，在检索噪声场景下提升回答准确率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
检索增强VLM同时依赖检索文本、输入图像两类信息源，两类信息均存在噪声/错误风险，现有评估仅关注效果下降，未量化模型对两类模态的权重分配逻辑，也无法衡量回答是否真正基于图像接地。
### 方法关键点
1. 构建GIB-200K数据集，基于COCO、Visual Genome生成20万图文对，覆盖检索硬负噪声、图像降质、跨模态冲突三类压力场景；
2. 基于贝叶斯线索组合框架定义知识惯性（过度加权文本）、感官捕获（过度加权图像）两类偏差，用带测量误差校正的回归估计模态权重，提出接地幻觉得分衡量正确回答未基于图像的比例。
### 关键结果
4款开源模型干净输入准确率92.5%~94.2%，压力场景下准确率降至41.3%~59.9%；LLaVA系列过度加权文本（w_T/w_I=1.229~1.322），InternVL3更偏好图像（w_T/w_I=0.680）；34.8%~71.4%的干净正确回答会因误导性检索文本被推翻；无检索一致性校验可提升误导性文本场景的准确率，但会降低覆盖度。
