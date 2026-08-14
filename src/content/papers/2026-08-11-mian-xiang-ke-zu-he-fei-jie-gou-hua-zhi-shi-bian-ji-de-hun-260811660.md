---
title: Hybrid-Policy Self-Editing for Composable Unstructured Knowledge Editing
title_zh: 面向可组合非结构化知识编辑的混合策略自编辑方法
authors:
- Tianci Liu
- Zihan Dong
- Tianchun Li
- Yi-Chung Chen
- Qiming Cao
- Xingchen Wang
- Shiyang Wang
- Zichen Miao
- Linjun Zhang
- Haoyu Wang
affiliations:
- University of Tennessee
- Rutgers University
- Purdue University
- University at Albany
arxiv_id: '2608.11660'
url: https://arxiv.org/abs/2608.11660
pdf_url: https://arxiv.org/pdf/2608.11660
published: '2026-08-11'
collected: '2026-08-14'
category: LLM
direction: LLM非结构化知识编辑优化
tags:
- Knowledge Editing
- LLM
- Self-Distillation
- Hybrid Policy
- Unstructured Knowledge
one_liner: 提出混合策略自编辑HPSE，解决非结构化知识编辑可组合性缺陷，即插即用适配各类梯度编辑器
practical_value: '- 电商/导购Agent场景下，需要快速更新LLM内置的商品参数、活动规则、商家介绍等非结构化新知识时，可将HPSE作为插件嵌入现有LoRA/FT-M等知识编辑流程，无需改造核心编辑逻辑即可提升知识的可拆解、可组合性，避免更新后只能整段复述、无法回答用户碎片化查询或多跳推理问题

  - 可复用HPSE的混合Rollout设计思路：在Agent的自蒸馏微调场景中，当需要教模型掌握其未见过的新知识时，触发带知识上下文的特权同模型在学生输出偏离时按Token介入修正，比纯自蒸馏的知识覆盖度更高、收敛速度更快

  - 做LLM知识更新的业务效果评估时，可复用论文提出的可组合性评测框架，除了整段知识召回准确率，额外增加原子事实召回、多跳推理准确率两个维度，更贴合用户实际查询场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有非结构化知识编辑（UKE）方法仅能让LLM整段复述注入的自由文本知识，无法拆解为原子事实回答碎片化查询，也无法组合多个新知识完成多跳推理，即缺失「可组合性」；而纯上下文自蒸馏因新知识未被模型预训练覆盖，生成轨迹容易偏离主题，覆盖度不足难以解决该问题。
## 方法关键点
- 提出HPSE混合策略自编辑框架，用带新知识上下文的同模型作为特权状态，构造混合生成轨迹：当学生模型输出与特权状态差距超过阈值τ、且特权状态置信度超过κ时，由特权状态输出Token修正轨迹，其余步骤保持学生自身输出。
- 训练损失结合混合轨迹的KL自蒸馏项与原编辑的NLL锚定项，无需外部监督或额外数据集，可即插即用适配所有梯度式知识编辑器。
## 关键结果
在UnKEBench（拆解能力评测）和MQuAKE-uns（组合能力评测）数据集上，适配LoRA、FT-M两种主流编辑器，跨4个主流LLM backbone验证：
- LoRA结合HPSE后，原子事实拆解召回准确率最高提升33.5%，多跳推理准确率最高提升70.9%，模型通用能力（MMLU）无明显下降。
- 连续编辑场景下，HPSE加持的LoRA平均得分最高相对提升149%，显著优于现有基线方法。
## 核心结论
非结构化知识编辑不能仅追求知识的成功注入，更要保证注入的知识能像预训练获得的知识一样被灵活拆解、组合使用
