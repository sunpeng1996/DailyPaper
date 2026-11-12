---
title: Ensemble Routing for Prompt-Adaptive Cost-Aware LLM Inference
title_zh: 支持Prompt自适应的成本感知LLM推理集成路由框架
authors:
- Saul Urso
- Emanuele Carlini
- Patrizio Dazzi
- Matteo Mordacchini
affiliations:
- Institute of Information Science and Technologies, CNR, Italy
- Institute of Informatics and Telematics, CNR, Italy
- University of Pisa, Department of Computer Science, Italy
arxiv_id: '2611.10193'
url: https://arxiv.org/abs/2611.10193
pdf_url: https://arxiv.org/pdf/2611.10193
published: '2026-11-05'
collected: '2026-11-12'
category: LLM
direction: LLM推理优化 · 成本感知路由
tags:
- LLM Routing
- Cost-Aware Inference
- LLM Ensembling
- Prompt Adaptation
- Inference Optimization
one_liner: 提出PISA单模型路由与PISA-E集成路由框架，支持推理时动态调整成本质量偏好无需重训练
practical_value: '- 多LLM服务场景（电商智能客服、Agent导购、生成式推荐文案）可直接复用PISA的软聚类+单模型能力预估逻辑，仅需历史请求的模型正确率和prompt
  embedding即可训练，实现轻量无负担的单模型路由。

  - 需平衡LLM调用成本与响应质量的业务，可复用PISA-E的动态集成规模选择逻辑，通过调整α参数在推理时直接切换成本优先级，无需重训练路由模型，可适配不同用户等级、场景的差异化需求。

  - 多模型响应聚合可采用文中的自加权BERTScore方法，无需额外训练排序模型，直接用各模型的预估能力加权计算相似度选最优响应，OOD场景下效果优于普通MBR解码。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM广泛部署于搜索、推荐、智能Agent等Web服务，需处理异构用户请求，平衡响应质量与推理成本。现有单模型路由无法利用多模型能力互补性，固定集成方案无法动态调整集成规模与成本，也无法在推理时灵活切换成本-质量偏好，适配不同场景需求。
### 方法关键点
- PISA单模型路由：对prompt embedding做X-means聚类，计算prompt对每个聚类的软归属度，为每个候选LLM训练独立的逻辑回归预测器，预估当前prompt下模型的正确率，结合平均调用成本与α参数（成本-质量偏好）选择最优单模型。
- PISA-E集成路由：复用PISA的单模型能力预估值，用泊松二项分布计算严格多数模型输出正确的概率作为集成效果代理指标，将模型按单模型效用排序后取奇数基数的前缀作为候选集成，选择效用最高的组合，最后用自加权BERTScore聚合多模型响应，α参数可在推理时任意调整无需重训练。
### 关键结果
在LLMRouterBench、RouterBench、FusionBench、SPROUT四个基准的ID与OOD场景下测试：
1. PISA单模型路由在8组benchmark-setting组合中6个排名第一，宏平均超体积比最优基线高1.63（ID）、1.52（OOD）。
2. PISA-E优先质量时（α=1），ID场景性能比最优集成基线高2.09pct，OOD高2.87pct；低成本点下，ID场景性能超基线同时推理成本降36%，OOD降25%。
### 最值得记住的结论
LLM路由无需固定单模型或固定集成规模，基于prompt自适应调整调用策略可同时实现更高性能与更低推理成本，成本-质量偏好可在推理时动态调整无需重训练。
