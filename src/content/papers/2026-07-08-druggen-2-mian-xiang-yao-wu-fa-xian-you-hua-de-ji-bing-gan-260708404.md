---
title: 'DrugGen 2: A disease-aware language model for enhancing drug discovery'
title_zh: DrugGen 2：面向药物发现优化的疾病感知语言模型
authors:
- Ali Motahharynia
- Mohammadreza Ghaffarzadeh-Esfahani
- Mahsa Sheikholeslami
- Navid Mazrouei
- Matin Irajpour
- Yousof Gheisari
- Hajar Sirous
affiliations:
- Regenerative Medicine Research Center, Isfahan University of Medical Sciences
- Isfahan Neuroscience Research Center, Isfahan University of Medical Sciences
- Department of Medicinal Chemistry, School of Pharmacy, Isfahan University of Medical
  Sciences
- Isfahan Cardiovascular Research Center, Isfahan University of Medical Sciences
- Bioinformatics Research Center, Isfahan University of Medical Sciences
arxiv_id: '2607.08404'
url: https://arxiv.org/abs/2607.08404
pdf_url: https://arxiv.org/pdf/2607.08404
published: '2026-07-08'
collected: '2026-07-12'
category: Other
direction: 药物发现 · 疾病感知生成式模型
tags:
- Generative Model
- GPT-2 Fine-tuning
- Reinforcement Learning
- GRPO
- Drug Discovery
one_liner: 融合疾病本体与靶点蛋白序列微调GPT-2，生成更高结合亲和力的药物小分子
practical_value: '- 两阶段微调（SFT+GRPO强化学习）的多约束生成思路可迁移到生成式推荐的多目标优化场景

  - 多维度加权奖励函数（有效性、新颖性、多样性、匹配度）的设计可复用在GenRec的RL调优环节

  - 多条件融合的条件生成框架可迁移到带多重业务约束的商品/营销文案生成任务'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有药物设计计算方法通常仅基于特定靶点或通用分子属性生成分子，忽略疾病上下文对靶点行为、治疗效果的影响，生成分子实际成药性存在短板。
### 方法关键点
基于预训练GPT-2微调，训练数据为关联了对应疾病、靶点的获批药物curated数据集；采用两阶段训练策略：先做监督微调，再通过group relative policy optimization (GRPO)做强化学习；奖励函数同时优化化学有效性、新颖性、多样性、预测结合亲和力4个维度。
### 关键结果
在糖尿病肾病相关5个蛋白靶点上评估，效果显著优于DrugGPT、DrugGen基线；生成独特分子的能力更优，与获批药物结构相似度更高，所有靶点的预测结合亲和力均有提升；分子对接验证显示候选配体最高结合亲和力达-9.917，优于基准药物依那普利的-8.283。
