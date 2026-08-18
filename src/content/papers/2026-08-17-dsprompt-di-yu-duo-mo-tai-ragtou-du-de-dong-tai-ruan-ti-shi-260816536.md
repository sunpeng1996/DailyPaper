---
title: 'DSPrompt: Dynamic Soft Prompt Defense Against M-RAG Corruption'
title_zh: DSPrompt：抵御多模态RAG投毒的动态软提示防御框架
authors:
- Chang Liu
- Yuni Lai
- Mingyue Cui
- Cong Tian
- Yunyan Zhang
- Xian Wu
- Kai Zhou
- Bin Xiao
affiliations:
- 西安电子科技大学
- 香港理工大学
- 腾讯Jarvis Lab
arxiv_id: '2608.16536'
url: https://arxiv.org/abs/2608.16536
pdf_url: https://arxiv.org/pdf/2608.16536
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: 多模态RAG · 对抗投毒防御
tags:
- M-RAG
- Soft Prompt
- Adversarial Defense
- Retrieval Poisoning
- Prompt Tuning
one_liner: 通过<1%参数量的层间软提示微调冻结检索器，无查询侧开销即可抵御M-RAG投毒攻击
practical_value: '- 电商多模态导购Agent、商品图文检索等M-RAG应用可直接复用DSPrompt方案，仅需<1%额外参数、无需修改现有检索pipeline，几乎不增加查询时延就能显著提升抗恶意商品投毒、错误信息注入的能力

  - 可借鉴浅到深的软提示分配策略：给Transformer深层分配更多token，既集中防御能力在跨模态对齐关键层，又避免扰动浅层基础特征，平衡防御效果和业务检索精度

  - 动态min-max训练范式可复用：训练时在线生成对抗样本迭代优化防御策略，相比固定对抗样本训练泛化性更强，能适配未知的投毒攻击类型

  - 部署成本极低：仅需用微调后的检索器重训一次向量库，无需额外检测、重排模块，适合大规模电商商品库、商家知识库的RAG系统落地'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多模态RAG（M-RAG）已广泛应用于电商图文导购、多模态问答等场景，但攻击者可注入带微小扰动的图文毒样本，通过嵌入对齐欺骗检索器，诱导大模型输出错误、有害内容。现有防御方案依赖查询时的图文一致性检测、重排逻辑，不仅推理开销随query量和库规模线性增长，还对未知攻击泛化性差，难以适配开放部署场景。

### 方法关键点
- 冻结CLIP风格双模态编码器的主干参数，在视觉、文本分支的每一层插入可学习软提示，采用浅到深的提示长度分配策略，给负责跨模态对齐的深层分配更多token，总额外参数量<1%
- 动态min-max训练范式：内循环基于当前防御模型在线生成最强对抗毒样本，外循环优化软提示将毒样本挤出top-k检索结果，同时加入原编码器的锚定正则，保证良性样本的检索效果基本不受损
- 部署无侵入：仅需用优化后的编码器重跑一次知识库embedding建库，沿用原有向量检索流程，无需额外检测、重排模块，无查询侧额外开销

### 关键结果
在4个基准数据集、3类代表性投毒攻击下测试，对比RoCLIP基线：
1. 见过的PE-C类攻击下，Places365数据集攻击成功率（ASR）从81.15%降至6.66%，检索效用保留率（SUF@3）达98.84%，生成答案保真度（TF）达93.18%
2. 未见过的GPA全局攻击下，ASR从87%降至0.64%，TF达80.21%
3. 单查询时延仅为RoCLIP的60%，无向量库存储空间额外开销

针对RAG的投毒防御优先改造检索器语义空间，比查询时后处理的性价比高得多
