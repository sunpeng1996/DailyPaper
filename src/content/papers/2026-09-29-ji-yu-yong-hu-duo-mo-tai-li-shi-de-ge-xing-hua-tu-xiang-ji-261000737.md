---
title: Personalized Image Generation with Reasoning and Reflection
title_zh: 基于用户多模态历史的个性化图像生成基准与推理反思框架
authors:
- Bo Ni
- Ngoc N. Tran
- Qinwen Ge
- Franck Dernoncourt
- Seunghyun Yoon
- Samyadeep Basu
- Sungchul Kim
- Puneet Mathur
- Nedim Lipka
- Tong Yu
affiliations:
- Vanderbilt University
- Adobe Systems
- University of Maryland, College Park
- University of Georgia
arxiv_id: '2610.00737'
url: https://arxiv.org/abs/2610.00737
pdf_url: https://arxiv.org/pdf/2610.00737
published: '2026-09-29'
collected: '2026-10-02'
category: GenRec
direction: 生成式推荐 · 个性化图像生成
tags:
- Personalized Generation
- Multimodal LLM
- Diffusion Model
- DPO
- E-commerce
one_liner: 提出首个用户多模态历史个性化图像生成基准PMH-IG及推理反思框架PEARL，个性化指标平均提升15%
practical_value: '- 电商商品主图个性化生成场景可复用PEARL的「推理规划→渲染→反思修正」架构，基于用户浏览/评论历史生成适配用户偏好的商品场景图，预期提升CTR

  - 个性化内容生成任务可复用PMH-IG的多轴评估方案：融合自动图像质量指标、检索式个性化指标、MLLM-as-Judge的综合评估，避免单一指标偏倚

  - 多模态个性化推理模块可基于开源MLLM用LoRA微调，搭配冻结的SDXL/Flux等图像生成模型，训练成本低，单4090即可完成，易落地

  - 可复用render-in-the-loop的DPO训练范式，不用标注大量偏好数据，基于下游任务的检索reward即可优化生成效果，降低标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有个性化图像生成依赖少量 curated 参考图复刻特定视觉概念，无法基于用户真实多模态历史（评论、帖子、浏览记录等）推理用户身份、生活方式与审美偏好，而电商个性化商品展示、社交平台个性化内容创作等场景亟需这类能力，此前也缺乏统一benchmark评估相关方案效果。

### 方法关键点
- 推出PMH-IG基准：包含两个落地场景任务，一是基于亚马逊用户评论历史的个性化场景生成（为指定商品生成适配用户偏好的场景图），二是基于Instagram用户帖子历史的个性化创意生成（按指定主题生成符合用户审美风格的内容图），配套多轴评估协议
- 设计PEARL框架：分为推理规划、渲染、反思修正三阶段，先用多模态Planner从用户历史提取偏好生成图像prompt，用冻结SDXL渲染初始图；再用Reflector对比初始图与用户历史识别个性化偏差，修正prompt后二次渲染得到最终图
- 训练采用两阶段方案：先蒸馏老师模型的silver轨迹做SFT，再用交替DPO做render-in-the-loop优化，基于任务对齐的检索reward更新Planner和Reflector参数，仅用LoRA微调MLLM部分

### 关键实验
在PMH-IG两个任务上对比PMG、Pigeon、LLaVA、LaVIT等基线，PEARL在个性化场景生成任务上H@5达0.2297、MRR达0.1639，MLLM Judge整体评分达3.92，均为最优；在个性化创意生成任务上Inter-cat R@1达0.876、Intra-cat R@1达0.701，分别比次优基线高出17.1%、6.4%，个性化指标平均提升15%。

### 核心结论
个性化生成的核心是推理用户的身份与偏好，而非简单复刻参考内容，引入推理-反思的闭环能大幅提升生成内容的用户匹配度
