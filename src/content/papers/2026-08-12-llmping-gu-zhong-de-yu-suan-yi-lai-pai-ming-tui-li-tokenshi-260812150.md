---
title: 'Who Thinks Best Depends on How Long You Let Them: Budget-Dependent Rankings
  in LLM Evaluation'
title_zh: 《LLM评估中的预算依赖排名：推理token时长决定模型表现》
authors:
- Rodrigo Guedes de Souza
- Alison R. Panisson
affiliations:
- Federal University of Santa Catarina (UFSC)
arxiv_id: '2608.12150'
url: https://arxiv.org/abs/2608.12150
pdf_url: https://arxiv.org/pdf/2608.12150
published: '2026-08-12'
collected: '2026-08-13'
category: Eval
direction: LLM评估 · 预算感知模型路由与优化
tags:
- LLM Evaluation
- Inference Budget
- Model Routing
- Model Complementarity
- Reasoning LLM
one_liner: 验证LLM模型排名随推理token预算变化反转，提出预算感知路由可捕获14.1%的oracle增益
practical_value: '- 业务LLM选型不要盲目参考通用榜单，需结合自身部署的max_tokens限制（如实时客服、高并发推荐文案生成的token约束），实测对应预算下的模型表现，避免选到高预算才达标但业务场景下拉胯的模型

  - 搭建同域多模型路由系统时，必须将token预算作为核心特征输入，可带来1.6~5.7pp的效果提升；跨域路由场景不要直接复用训练域的预算特征规律，会导致1.2pp的效果下降，优先使用文本统计、语义嵌入等通用特征

  - 电商/广告场景的复杂推理任务（如复杂用户意图理解、个性化权益计算）可利用不同模型在不同预算下的能力互补性，做预算感知的模型 ensemble，最高有27.8pp的潜在效果提升空间

  - 部署带内部<think> token的推理模型时，需单独评估截断对效果的影响，避免把截断导致的错误误判为模型推理能力不足'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM评估默认模型排名不随推理条件变化，标注为SOTA的模型默认在所有部署场景最优。但实际业务中大量场景存在推理token预算约束（实时响应、边缘部署、高并发降本），且已有零散研究发现“过思考”（推理token越多效果越差）现象，缺乏系统的预算对评估结果影响的量化研究。
### 方法关键点
- 覆盖4个8B~70B参数量的开源推理模型，7档token预算（64~4096），在GSM8K、MATH-500、GPQA三个难度递增的推理基准上完成56476次确定性推理（temperature=0）
- 定义4类模型-样本行为：始终正确、单调提升、非单调（过思考，预算提升效果下降）、始终错误
- 设计预算感知路由：用XGBoost融合预算、文本统计特征、句子嵌入PCA特征，预测各模型在对应预算下的正确率，路由到最优模型
### 关键结果
- 3%~19%的样本存在非单调过思考行为，且86%~94%的过思考为模型专属，跨模型重叠仅6%~14%
- 所有基准上模型排名随预算发生统计显著反转（p<0.01），如GSM8K上256预算时LLaMA-3.3 70B准确率62.4%排第一，4096预算时GPT-OSS 20B准确率94.8%排第一
- 同域路由加入预算特征带来1.6~5.7pp提升，跨域路由预算特征会导致1.2pp下降；跨域路由可捕获14.1%的oracle增益，oracle最高增益可达27.8pp
### 最值得记住的一句话
不存在通用的“最优LLM”，哪个模型表现最好完全取决于你允许它用多少token思考。
