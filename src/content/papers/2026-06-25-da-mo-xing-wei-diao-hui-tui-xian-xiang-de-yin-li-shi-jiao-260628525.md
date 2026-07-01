---
title: A Gravitational Interpretation of Fine-Tuning Reversion
title_zh: 大模型微调回退现象的引力视角解释
authors:
- Samuele Poppi
- Nils Lukas
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence (MBZUAI)
arxiv_id: '2606.28525'
url: https://arxiv.org/abs/2606.28525
pdf_url: https://arxiv.org/pdf/2606.28525
published: '2026-06-25'
collected: '2026-07-01'
category: LLM
direction: 大模型安全 · 微调回退机制解释
tags:
- Fine-tuning
- Alignment Safety
- Activation Geometry
- Model Drift
- Intervention
one_liner: 提出训练历史依赖的微调回退引力解释框架，识别回退方向v_rev，阻断该方向可降低安全退化且无明显任务损失
practical_value: '- 电商/广告垂域LLM微调（如客服模型、文案生成模型、生成式推荐模型）时，可先提取通用对齐模型到垂域对齐模型的v_rev方向，微调时加正则阻断该方向漂移，避免已对齐的合规、广告规范等规则失效，且几乎不影响垂域任务效果

  - 可复用论文的激活空间方向探测方法，监控推荐系统中LLM模块（如Query改写、候选生成、排序理由生成模块）的不可控漂移方向，提前做干预降低线上风险

  - 垂域LoRA微调也存在回退风险，不能仅依赖LoRA低秩约束保障对齐效果，需结合方向阻断正则进一步提升模型鲁棒性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大语言模型完成安全/规则对齐后，仅在良性数据上做后续微调，也常出现安全退化、已擦除的有害能力复现、合规规则失效等回退现象，现有研究多将这些现象视为独立的安全故障，缺乏统一的机制解释，也缺乏低成本的通用干预方案。
### 方法关键点
- 提出引力解释框架：大模型早期大规模预训练、通用对齐阶段会形成稳定的主导行为流形，后续安全对齐、垂域微调只是在该流形上的浅层偏移，后续微调时优化梯度会自然携带向主导流形回退的分量
- 定义可量化的回退方向v_rev：用对齐前的通用基准模型和对齐后模型在目标探测Prompt（如有害Prompt、合规校验Prompt）上的平均激活差，作为回退方向的代理
- 轻量干预方案：微调时增加辅助损失，当模型激活向v_rev方向漂移时施加惩罚，选择性阻断回退运动
### 关键结果
在Llama 3.1 8B、Llama 3.2 3B、Qwen2.5 3B等多个模型上验证：阻断v_rev方向后，Alpaca微调100步时的有害率从19.0%±4.0%降至8.5%±1.5%，任务困惑度几乎无变化；回退方向与激活漂移的余弦相似度在微调第1步就达0.429±0.052，第20步升至0.647±0.021，全部高于随机方向的p99阈值。
> 最值得记住的话：大模型微调的漂移不是随机的，而是存在向早期训练形成的主导行为流形回退的固有倾向，可通过方向阻断低成本抑制该效应
