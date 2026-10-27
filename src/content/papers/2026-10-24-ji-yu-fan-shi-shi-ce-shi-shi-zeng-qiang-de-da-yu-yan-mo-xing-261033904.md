---
title: Counterfactual Test-Time Augmentation for Shortcut Removal in Language Models
title_zh: 基于反事实测试时增强的大语言模型捷径消除方法
authors:
- Katie Matton
- Rosalind W. Picard
- John Guttag
- Maggie Makar
affiliations:
- MIT
- University of Michigan
arxiv_id: '2610.33904'
url: https://arxiv.org/abs/2610.33904
pdf_url: https://arxiv.org/pdf/2610.33904
published: '2026-10-24'
collected: '2026-10-27'
category: LLM
direction: 大语言模型鲁棒性 · 测试时增强
tags:
- Test-Time Augmentation
- Counterfactual Learning
- Shortcut Removal
- LLM Robustness
- Out-of-Distribution Generalization
one_liner: 无需访问模型权重与标注训练数据，测试时通过反事实增强消除LLM捷径依赖
practical_value: '- 电商场景中LLM分类/排序任务（如商品审核、评论情感分类、风险内容召回）遇到的已知捷径（如品牌、性别、价格偏见、用户诱导性意见），可直接复用CTTA框架，测试时做反事实编辑后聚合预测，无需微调模型，落地成本极低

  - 仅能访问LLM API、无法获取token似然时，优先使用Uniform CTTA：对所有捷径值生成反事实样本后均匀加权，理论上可保证与最优捷径不变预测器AUROC完全一致，完全满足排序类业务需求

  - Select-CTTA的三阶段无标签诊断流程可直接复用：先判断捷径强度，再检查权重塌陷，最后校验似然与分类器对齐度，自适应选择最优加权策略，无需业务标注数据即可落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM普遍依赖训练数据中的伪相关（捷径），如顺从用户意见、依赖选项顺序、性别刻板印象等，部署时分布偏移就会出现预测错误；现有捷径消除方法大多需在训练阶段实施，要求访问模型权重、标注训练数据、大量算力，普通业务使用者难以落地，亟需测试时无权重、无标注的轻量解决方案。

### 方法关键点
- 提出CTTA方法族：测试时对输入样本做反事实编辑，仅修改已知捷径的取值，保留标签相关内容不变，对不同编辑后的样本预测结果加权聚合得到最终输出，理论上保证预测结果与捷径无关
- 提供三类加权策略：Model-Weighted CTTA用LLM token似然加权，满足假设时可达最优预测效果；Fixed-Weight CTTA（均匀加权/中性值加权）无需权重估计，理论证明其与最优预测器排序完全一致，AUROC无损失；Select-CTTA通过3个无标签诊断测试自适应选择最优加权策略

### 关键实验
在数学批改（捷径为用户意见）、职业分类（捷径为性别）两个任务上测试6款不同大小的开源LLM，对比测试时校准、OOC提示等基线：在反转分布测试集上，Select-CTTA在微调场景下比无增强基线AUROC最高提升0.66，零样本场景下比最强基线AUROC高0.057，性能接近在均衡数据上微调的参考模型。

### 核心结论
只要可明确识别业务场景中的已知捷径，无需访问模型权重、无需标注训练数据，仅通过测试时反事实增强即可大幅提升LLM分布偏移下的鲁棒性，排序类场景用均匀加权即可拿到最优AUROC。
