---
title: Latent Trajectory Discrimination for AI-Generated Text Detection
title_zh: 基于隐轨迹区分的AI生成文本检测方法
authors:
- Gianluca Bonifazi
- Christopher Buratti
- Michele Marchetti
- Federica Parlapiano
- Giulia Quaglieri
- Davide Traini
- Domenico Ursino
- Luca Virgili
affiliations:
- Polytechnic University of Marche
- University of Modena and Reggio Emilia
arxiv_id: '2607.14967'
url: https://arxiv.org/abs/2607.14967
pdf_url: https://arxiv.org/pdf/2607.14967
published: '2026-07-16'
collected: '2026-07-17'
category: LLM
direction: LLM安全 · AI生成文本隐轨迹检测
tags:
- AIGTD
- Contrastive Learning
- Trajectory Modeling
- LLM Safety
- Autoregressive Generation
one_liner: 提出融合隐轨迹几何建模与对比学习的GTCL框架，大幅提升AI生成文本检测性能
practical_value: '- 电商UGC、AI生成商品文案的合规校验场景，可引入生成隐轨迹动态特征替代静态embedding，提升AI生成垃圾/违规文案的识别准确率

  - 生成式推荐、Agent调用LLM生成内容的质检环节，可复用GTCL的序列分段编码+对比学习范式，降低跨生成模型、跨内容域的检测适配成本

  - 用户行为序列建模、长会话推荐场景，可借鉴轨迹几何特征提取思路，挖掘序列动态演化规律替代全局聚合特征，提升序列建模效果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有AI生成文本检测（AIGTD）方法大多将文本视为静态对象，基于全局统计特征或压缩embedding判断，忽略了自回归生成过程中内容在隐空间逐步演化的动态特性，跨模型、跨域泛化能力差。
### 方法关键点
将AIGTD重构为隐生成轨迹二分类问题，提出GTCL框架：1）将长文本切分为有序局部单元，逐单元编码后构建序列级结构化轨迹表示；2）通过对比学习学习自回归生成对应的轨迹几何规律，不依赖静态文本特征。
### 关键结果
在3个不同域的公开基准集上持续优于所有基线检测方案，验证了序列动态建模可提供跨生成模型、跨内容域的鲁棒判别信号，检测精度显著高于静态特征方案
